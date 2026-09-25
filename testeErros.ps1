# Login (ajuste o email/senha conforme seu usuário de teste já criado)
$loginResponse = Invoke-RestMethod -Uri "http://127.0.0.1:8000/login" -Method Post -ContentType "application/json" -Body '{"email": "teste2@email.com", "senha": "Senha123"}'
$headers = @{Authorization = "Bearer $($loginResponse.access_token)"}

Write-Host "`n=== Teste: cadastro de usuario com email duplicado (espera 409) ==="
try {
    Invoke-RestMethod -Uri "http://127.0.0.1:8000/users" -Method Post -ContentType "application/json" -Body '{"nome": "Teste", "email": "teste2@email.com", "senha": "Senha123"}'
} catch {
    Write-Host "Status recebido:" $_.Exception.Response.StatusCode.value__
    Write-Host $_.ErrorDetails.Message
}