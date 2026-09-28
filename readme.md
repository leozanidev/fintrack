# FinTrack API

API REST para gerenciamento financeiro pessoal — cadastro de receitas e despesas, categorias, filtros e um dashboard com resumo geral e mensal. Projeto de portfólio construído do zero, com foco em boas práticas de backend profissional.

## Stack

- **Python** + **FastAPI**
- **PostgreSQL** + **SQLAlchemy** (ORM)
- **Alembic** (migrations)
- **Pydantic** (validação de dados)
- **JWT** (autenticação, via `python-jose`)
- **Passlib / bcrypt** (hash de senha)
- **Pytest** (testes automatizados)
- **Docker** + **Docker Compose**

## Funcionalidades

- Cadastro e autenticação de usuários (JWT)
- CRUD completo de transações (receitas e despesas)
- Categorias personalizadas por usuário
- Filtros por tipo, categoria e período, com paginação
- Dashboard com totais gerais e resumo mensal (receita, despesa, saldo)
- Tratamento de erros, logging estruturado e testes automatizados

## Endpoints

| Método | Rota                 | Descrição                                       |
| ------ | -------------------- | ----------------------------------------------- |
| GET    | `/health`            | Health check                                    |
| POST   | `/users`             | Cadastro de usuário                             |
| POST   | `/login`             | Login (retorna JWT)                             |
| GET    | `/users/me`          | Dados do usuário autenticado                    |
| POST   | `/categories`        | Criar categoria                                 |
| POST   | `/transactions`      | Criar transação                                 |
| GET    | `/transactions`      | Listar transações (com filtros e paginação)     |
| GET    | `/transactions/{id}` | Buscar transação por id                         |
| PUT    | `/transactions/{id}` | Editar transação (parcial)                      |
| DELETE | `/transactions/{id}` | Excluir transação                               |
| GET    | `/dashboard`         | Totais gerais (receitas, despesas, saldo)       |
| GET    | `/dashboard/monthly` | Resumo mensal (receita, despesa, saldo por mês) |

Documentação interativa disponível em `/docs` (Swagger UI) após subir o projeto.

## Como rodar

### Com Docker (recomendado)

```bash
git clone https://github.com/leozanidev/fintrack.git
cd fintrack
cp .env.example .env   # preencha as variáveis
docker-compose up
```

Em outro terminal, aplique as migrations na primeira vez:

```bash
docker-compose exec api alembic upgrade head
```

A API estará disponível em `http://localhost:8000`.

### Localmente (sem Docker)

```bash
python -m venv venv
venv\Scripts\Activate.ps1   # Windows
pip install -r requirements.txt
alembic upgrade head
uvicorn app.main:app --reload
```

Requer um PostgreSQL rodando localmente e um `.env` configurado.

## Testes

```bash
python -m pytest -v
```

Os testes rodam contra um banco de dados de teste separado, configurado em `tests/conftest.py`.

## Estrutura do projeto

```
app/
├── core/          # config, segurança, dependências
├── models/        # models do SQLAlchemy
├── schemas/       # schemas do Pydantic
├── routers/       # rotas da API
├── database.py
└── main.py
alembic/           # migrations
tests/             # testes automatizados (Pytest)
Dockerfile
docker-compose.yml
```

## Sobre o projeto

Construído com foco em aprender backend na prática — autenticação real com JWT, modelagem relacional, tratamento de erros, testes automatizados e containerização, sem pular etapas.
