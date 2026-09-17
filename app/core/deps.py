from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import jwt, JWTError
from app.database import get_db
from app.core.security import SECRET_KEY, ALGORITHM
from app.models.user import Usuarios

oauth2_schema = OAuth2PasswordBearer(tokenUrl="login")

def get_usuario_atual(token:str = Depends(oauth2_schema), db:Session = Depends(get_db)):
    try:
        token_decodificado = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido!")

    email_usuario = token_decodificado.get("sub")
    if (email_usuario is None):
        raise HTTPException(status_code=401, detail="Usuario inválido!")
    usuario = db.query(Usuarios).filter(Usuarios.email == email_usuario).first()
    if (usuario is None):
            raise HTTPException(status_code=401, detail="Usuario não encontrado.")

    return usuario