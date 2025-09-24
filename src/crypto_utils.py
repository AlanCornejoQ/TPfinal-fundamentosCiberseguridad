import bcrypt
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt

def hashClaveMaestra(clave: str) -> bytes:
    return bcrypt.hashpw(clave.encode("utf-8"), bcrypt.gensalt(rounds=12))

def verificarClaveMaestra(clave: str, hash_guardado: bytes) -> bool:
    return bcrypt.checkpw(clave.encode("utf-8"), hash_guardado)

def derivarClaveDesdeContrasena(contrasena: str, sal: bytes, longitud: int = 32) -> bytes:
    kdf = Scrypt(salt=sal, length=longitud, n=2**14, r=8, p=1)
    return kdf.derive(contrasena.encode("utf-8"))