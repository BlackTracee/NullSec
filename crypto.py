import secrets
from base64 import urlsafe_b64encode as b64e, urlsafe_b64decode as b64d

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

backend = default_backend()
iteracoes = 100_000

def _derivar_chave(senha: bytes, sal: bytes, iteracoes: int = iteracoes) -> bytes:
    """Deriva uma chave secreta a partir de uma senha e um sal"""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(), length=32, salt=sal,
        iterations=iteracoes, backend=backend)
    return b64e(kdf.derive(senha))

def senha_criptografar(mensagem: str, senha: str, iteracoes: int = iteracoes) -> str:
    _mensagem = mensagem.encode() 
    sal = secrets.token_bytes(16)
    chave = _derivar_chave(senha.encode(), sal, iteracoes)
    return b64e(
        b'%b%b%b' % (
            sal,
            iteracoes.to_bytes(4, 'big'),
            b64d(Fernet(chave).encrypt(_mensagem)),
        )
    ).decode()

def senha_descriptografar(token: str, senha: str) -> str:
    _token = token.encode()
    decodificado = b64d(_token)
    sal, iter, _token = decodificado[:16], decodificado[16:20], b64e(decodificado[20:])
    iteracoes = int.from_bytes(iter, 'big')
    chave = _derivar_chave(senha.encode(), sal, iteracoes)
    return Fernet(chave).decrypt(_token).decode()
