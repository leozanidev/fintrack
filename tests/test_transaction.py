from fastapi.testclient import TestClient
from app.main import app
import uuid

client = TestClient(app)


def criar_usuario_e_token():
    """Helper: cria um usuário, faz login, e retorna o header de autorização."""
    email = f"trans_{uuid.uuid4()}@email.com"
    senha = "Senha123"
    client.post("/users", json={"nome": "Usuario Transacao", "email": email, "senha": senha})
    login = client.post("/login", json={"email": email, "senha": senha})
    token = login.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}


def criar_categoria(headers, nome="Categoria Teste"):
    response = client.post("/categories", json={"nome": nome}, headers=headers)
    return response.json()["id"]


def test_criar_categoria():
    headers = criar_usuario_e_token()
    response = client.post("/categories", json={"nome": "Alimentacao"}, headers=headers)
    assert response.status_code == 200
    assert response.json()["nome"] == "Alimentacao"


def test_criar_transacao():
    headers = criar_usuario_e_token()
    category_id = criar_categoria(headers)

    response = client.post(
        "/transactions",
        json={
            "descricao": "Mercado",
            "valor": 150.50,
            "tipo": "Despesa",
            "data": "2026-09-15T10:00:00",
            "category_id": category_id,
        },
        headers=headers,
    )
    assert response.status_code == 200
    assert response.json()["descricao"] == "Mercado"
    assert response.json()["tipo"] == "Despesa"


def test_listar_transacoes():
    headers = criar_usuario_e_token()
    category_id = criar_categoria(headers)
    client.post(
        "/transactions",
        json={"descricao": "Salario", "valor": 3000, "tipo": "Receita", "data": "2026-09-01T10:00:00", "category_id": category_id},
        headers=headers,
    )

    response = client.get("/transactions", headers=headers)
    assert response.status_code == 200
    assert len(response.json()) >= 1


def test_buscar_transacao_inexistente():
    headers = criar_usuario_e_token()
    response = client.get("/transactions/999999", headers=headers)
    assert response.status_code == 404


def test_editar_transacao():
    headers = criar_usuario_e_token()
    category_id = criar_categoria(headers)
    criada = client.post(
        "/transactions",
        json={"descricao": "Original", "valor": 100, "tipo": "Despesa", "data": "2026-09-15T10:00:00", "category_id": category_id},
        headers=headers,
    ).json()

    response = client.put(f"/transactions/{criada['id']}", json={"descricao": "Editada"}, headers=headers)
    assert response.status_code == 200
    assert response.json()["descricao"] == "Editada"
    assert float(response.json()["valor"]) == 100  # campo não enviado permanece igual


def test_excluir_transacao():
    headers = criar_usuario_e_token()
    category_id = criar_categoria(headers)
    criada = client.post(
        "/transactions",
        json={"descricao": "Para excluir", "valor": 50, "tipo": "Despesa", "data": "2026-09-15T10:00:00", "category_id": category_id},
        headers=headers,
    ).json()

    response = client.delete(f"/transactions/{criada['id']}", headers=headers)
    assert response.status_code == 204

    # confirma que não existe mais
    busca = client.get(f"/transactions/{criada['id']}", headers=headers)
    assert busca.status_code == 404


def test_usuario_nao_ve_transacao_de_outro():
    headers_a = criar_usuario_e_token()
    headers_b = criar_usuario_e_token()

    category_id = criar_categoria(headers_a)
    criada = client.post(
        "/transactions",
        json={"descricao": "Do usuario A", "valor": 50, "tipo": "Despesa", "data": "2026-09-15T10:00:00", "category_id": category_id},
        headers=headers_a,
    ).json()

    # usuario B tenta acessar a transação do usuario A
    response = client.get(f"/transactions/{criada['id']}", headers=headers_b)
    assert response.status_code == 404
