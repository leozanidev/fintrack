from fastapi.testclient import TestClient
from app.main import app
import uuid

client = TestClient(app)


def criar_usuario_teste():
    """Helper: cria um usuário de teste e retorna (email, senha)."""
    email = f"login_{uuid.uuid4()}@email.com"
    senha = "Senha123"
    client.post("/users", json={"nome": "Usuario Login", "email": email, "senha": senha})
    return email, senha


def test_login_sucesso():
    email, senha = criar_usuario_teste()
    response = client.post("/login", json={"email": email, "senha": senha})
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"


def test_login_senha_errada():
    email, _ = criar_usuario_teste()
    response = client.post("/login", json={"email": email, "senha": "SenhaErrada"})
    assert response.status_code == 401


def test_login_email_inexistente():
    response = client.post("/login", json={"email": "naoexiste@email.com", "senha": "Senha123"})
    assert response.status_code == 401


def test_users_me_sem_token():
    response = client.get("/users/me")
    assert response.status_code == 401


def test_users_me_com_token():
    email, senha = criar_usuario_teste()
    login = client.post("/login", json={"email": email, "senha": senha})
    token = login.json()["access_token"]

    response = client.get("/users/me", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.json()["email"] == email
