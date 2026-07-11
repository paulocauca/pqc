import os
import urllib.request
import json

# Load env variables
token = ""
if os.path.exists('/home/rycz/.hermes/.env'):
    with open('/home/rycz/.hermes/.env', 'r') as f:
        for line in f:
            if line.startswith('SLACK_BOT_TOKEN='):
                token = line.split('=', 1)[1].strip()

if not token:
    print("SLACK_BOT_TOKEN not found in .env")
    exit(1)

# Prepare message
msg = """🚀 *Olá Paulo!* Tudo bem?

Hoje é dia de avançar ainda mais na nossa jornada rumo à criptografia pós-quântica! O material de estudo do *Dia 03* foi gerado e publicado com sucesso! 🔒🖥️

Estudamos sobre o *Endurecimento Pós-Quântico do SSH em 2026: A Transição para mlkem768x25519-sha256 no OpenSSH*. Compreendemos como o protocolo SSH (espinha dorsal da administração de servidores na nuvem) está se protegendo contra ameaças de "Coletar Agora, Decifrar Depois" (HNDL) usando trocas de chaves híbridas baseadas em ML-KEM-768 e X25519. Vimos também como essa implementação já vem habilitada por padrão no OpenSSH 9.9 e em sistemas operacionais modernos como o Ubuntu 26.04 LTS!

Aqui estão os links diretos para os PDFs de hoje no GitHub:
📄 *English (EN):* https://github.com/paulocauca/pqc/blob/main/en/2026-07-10-openssh_pq_hardening_mlkem768.pdf
📄 *Português (PT-BR):* https://github.com/paulocauca/pqc/blob/main/pt-BR/2026-07-10-openssh_pq_hardening_mlkem768.pdf

🐙 *Repositório GitHub:* https://github.com/paulocauca/pqc

Não deixe de ler o material completo e desafiar-se com o *Quiz Diário de 3 perguntas* incluído no final do guia de hoje para testar seus conhecimentos! 🧠💡

Bons estudos e até amanhã! 🎓✨"""

url = "https://slack.com/api/chat.postMessage"
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json; charset=utf-8"
}
data = {
    "channel": "C0BFMMTKF9V",
    "text": msg
}

req = urllib.request.Request(
    url,
    data=json.dumps(data).encode('utf-8'),
    headers=headers,
    method='POST'
)

try:
    with urllib.request.urlopen(req) as res:
        response_data = json.loads(res.read().decode('utf-8'))
        print("Slack Response:", response_data)
except Exception as e:
    print("Slack Error:", e)
