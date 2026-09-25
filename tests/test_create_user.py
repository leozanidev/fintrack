from fastapi.testclient import TestClient
from app.main import app
import uuid

client = TestClient(app)

email_unico = f"test_{uuid.uuid4()}@email.com" 

def test_criar_usuario():
    response = client.post("/users", json={"nome": "Teste", "email": email_unico, "senha": "senha"})
    assert response.status_code == 200
    assert response.json()["id"] is not None
    assert response.json()["email"] == email_unico