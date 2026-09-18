# Login e captura do token
$loginResponse = Invoke-RestMethod -Uri "http://127.0.0.1:8000/login" -Method Post -ContentType "application/json" -Body '{"email": "teste2@email.com", "senha": "Senha123"}'
$token = $loginResponse.access_token

# Monta o header de autorização uma vez só, reutilizável
$headers = @{Authorization = "Bearer $token"}

Write-Host "Token obtido:" $token

# Exemplo: listar transações
$transacoes = Invoke-RestMethod -Uri "http://127.0.0.1:8000/transactions" -Method Get -Headers $headers
$transacoes

# Exemplo: criar uma transação nova
$novaTransacao = Invoke-RestMethod -Uri "http://127.0.0.1:8000/transactions" -Method Post -ContentType "application/json" -Headers $headers -Body '{"descricao": "Teste script", "valor": 50, "tipo": "Despesa", "data": "2026-09-15T10:00:00", "category_id": 1}'
$novaTransacao

# Exemplo: buscar uma transação pelo ID
$transacaoId = Invoke-RestMethod -Uri "http://127.0.0.1:8000/transactions/1" -Method Get -Headers $headers
$transacaoId

# Exemplo: Editar uma transação
$transacaoEditada = Invoke-RestMethod -Uri "http://127.0.0.1:8000/transactions/1" -Method Put -ContentType "application/json" -Headers $headers -Body '{"descricao": "Mercado editado"}'
$transacaoEditada

# Exemplo: Apagar uma transação
Invoke-RestMethod -Uri "http://127.0.0.1:8000/transactions/2" -Method Delete -Headers $headers