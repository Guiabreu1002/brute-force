
import requests
import time

URL = "http://127.0.0.1:8000/api/login"
EMAIL = "marco05@example.org"

senhas_teste = [
    "senha_errada_01",
    "senha_errada_02",
    "senha_errada_03",
    "senha_errada_04",
    "password",
    "senha_errada_06",
    "senha_errada_07",
    "senha_errada_08",
    "senha_errada_09",
    "senha_errada_10"
]

print("=" * 50)
print("       TESTE DE RATE LIMITING - LARAVEL")
print("=" * 50)

sucesso = 0
bloqueios = 0

for numero, senha in enumerate(senhas_teste, start=1):
    try:
        resposta = requests.post(
            URL,
            json={
                "email": EMAIL,
                "password": senha
            },
            timeout=5
        )

        print(
            f"Tentativa {numero:02d} | "
            f"HTTP {resposta.status_code} | ",
            end=""
        )

        if resposta.status_code == 401:
            print("Credenciais incorretas")
            sucesso += 1

        elif resposta.status_code == 429:
            print("RATE LIMIT ATIVADO!")
            bloqueios += 1
            break

        elif resposta.status_code == 422:
            print("Erro de validação")

        else:
            print(resposta.text[:150])

    except requests.RequestException as erro:
        print(f"\nErro de conexão: {erro}")
        break

    time.sleep(0.2)

print("\n" + "=" * 50)
print("RESULTADO DO TESTE")
print("=" * 50)
print(f"Respostas de credenciais inválidas: {sucesso}")
print(f"Bloqueios HTTP 429: {bloqueios}")

if bloqueios:
    print("Proteção contra excesso de tentativas funcionando!")
else:
    print("O limite não foi atingido durante este teste.")
