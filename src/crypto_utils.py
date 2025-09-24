import bcrypt
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
def hashClaveMaestra(clave: str) -> bytes:
    return bcrypt.hashpw(clave.encode("utf-8"), bcrypt.gensalt(rounds=12))

def verificarClaveMaestra(clave: str, hash_guardado: bytes) -> bool:
    return bcrypt.checkpw(clave.encode("utf-8"), hash_guardado)

def derivarClaveDesdeContrasena(contrasena: str, sal: bytes, longitud: int = 32) -> bytes:
    kdf = Scrypt(salt=sal, length=longitud, n=2**14, r=8, p=1)
    return kdf.derive(contrasena.encode("utf-8"))
def cifrarAESGCM(clave: bytes, claro: bytes, aad: bytes | None = None) -> tuple[bytes, bytes]:
    nonce = os.urandom(12)  # requerido por AESGCM
    ct = AESGCM(clave).encrypt(nonce, claro, aad)
    return nonce, ct

def descifrarAESGCM(clave: bytes, nonce: bytes, cifrado: bytes, aad: bytes | None = None) -> bytes:
    return AESGCM(clave).decrypt(nonce, cifrado, aad)