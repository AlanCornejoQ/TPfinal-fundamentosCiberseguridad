import os, sqlite3, time, secrets
from typing import Optional, List, Dict
from src.crypto_utils import hashClaveMaestra, verificarClaveMaestra, derivarClaveDesdeContrasena
from src.crypto_utils import (
    hashClaveMaestra, verificarClaveMaestra, derivarClaveDesdeContrasena,
    cifrarAESGCM, descifrarAESGCM
)

RUTA_DB = os.path.join(os.path.dirname(__file__), "..", "vault.sqlite3")

# ---- estado de modulo ----
_conexion: Optional[sqlite3.Connection] = None
_hashMaestro: Optional[bytes] = None
_salKdf: Optional[bytes] = None
_claveDatos: Optional[bytes] = None
_abierta: bool = False

# ---------- infra ----------
def bovedaExiste(ruta_db: str = RUTA_DB) -> bool:
    return os.path.exists(os.path.abspath(ruta_db))

def _conectar(ruta_db: str = RUTA_DB):
    global _conexion
    if _conexion is None:
        os.makedirs(os.path.dirname(os.path.abspath(ruta_db)), exist_ok=True)
        _conexion = sqlite3.connect(os.path.abspath(ruta_db))
        _conexion.execute("PRAGMA foreign_keys = ON")

def _configurarEsquema():
    _conexion.execute("""
    CREATE TABLE IF NOT EXISTS meta(
      id INTEGER PRIMARY KEY CHECK(id=1),
      hash_maestro BLOB NOT NULL,
      sal_kdf     BLOB NOT NULL,
      creado_en   REAL NOT NULL
    )""")
    _conexion.execute("""
    CREATE TABLE IF NOT EXISTS entradas(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      servicio    TEXT NOT NULL,
      usuario     TEXT NOT NULL,
      nonce       BLOB NOT NULL,
      cifrado     BLOB NOT NULL,
      creado_en   REAL NOT NULL,
      actualizado_en REAL NOT NULL
    )""")
    _conexion.commit()

# ---------- meta / apertura ----------
def inicializarBoveda(clave_maestra: str, ruta_db: str = RUTA_DB):
    if bovedaExiste(ruta_db):
        raise RuntimeError("ya existe una boveda")
    _conectar(ruta_db); _configurarEsquema()
    h = hashClaveMaestra(clave_maestra)
    sal = secrets.token_bytes(16)
    _conexion.execute(
        "INSERT INTO meta(id, hash_maestro, sal_kdf, creado_en) VALUES(1,?,?,?)",
        (h, sal, time.time())
    )
    _conexion.commit()
    _cargarEstado(h, sal)
    _derivarClaveDatos(clave_maestra, sal)

def abrirBoveda(clave_maestra: str, ruta_db: str = RUTA_DB) -> bool:
    if not bovedaExiste(ruta_db):
        return False
    _conectar(ruta_db); _configurarEsquema()
    fila = _conexion.execute("SELECT hash_maestro, sal_kdf FROM meta WHERE id=1").fetchone()
    if not fila:
        return False
    h, sal = fila
    if not verificarClaveMaestra(clave_maestra, h):
        return False
    _cargarEstado(h, sal)
    _derivarClaveDatos(clave_maestra, sal)
    return True

def _cargarEstado(hash_maestro: bytes, sal_kdf: bytes):
    global _hashMaestro, _salKdf
    _hashMaestro = hash_maestro
    _salKdf = sal_kdf

def _derivarClaveDatos(clave_maestra: str, sal_kdf: bytes):
    global _claveDatos, _abierta
    _claveDatos = derivarClaveDesdeContrasena(clave_maestra, sal_kdf)
    _abierta = True

def estaAbierta() -> bool:
    return bool(_abierta)

def cerrarBoveda():
    global _conexion, _claveDatos, _abierta
    if _conexion:
        _conexion.close()
    _conexion = None
    _claveDatos = None
    _abierta = False

def agregarEntrada(servicio: str, usuario: str, secreto: str):
    if not _abierta or _conexion is None or _claveDatos is None:
        raise RuntimeError("boveda no abierta")
    if not servicio or not usuario or not secreto:
        raise ValueError("servicio/usuario/secreto no pueden ser vacios")

    nonce, ct = cifrarAESGCM(_claveDatos, secreto.encode("utf-8"))
    ts = time.time()
    _conexion.execute(
        "INSERT INTO entradas(servicio, usuario, nonce, cifrado, creado_en, actualizado_en) VALUES(?,?,?,?,?,?)",
        (servicio, usuario, nonce, ct, ts, ts)
    )
    _conexion.commit()