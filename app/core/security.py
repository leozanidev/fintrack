from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
from app.core.config import Settings

SECRET_KEY = Settings.secret_key
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_senha(senha: str) -> str:
    return pwd_context.hash(senha)

def verifica_senha(senha_texto: str, senha_hash: str) -> bool:
    return pwd_context.verify(senha_texto, senha_hash)

def cria_access_token(dados: dict) -> str:
    dados_crus = dados.copy()
    expira_em = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    dados_crus.update({"exp": expira_em})
    token = jwt.encode(dados_crus, SECRET_KEY, algorithm=ALGORITHM)
    return token 