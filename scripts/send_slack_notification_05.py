import os
import urllib.request
import json

# Load env variables
token = ""
if os.path.exists('/home/rycz/.env'):
    with open('/home/rycz/.env', 'r') as f:
        for line in f:
            if line.startswith('SLACK_BOT_TOKEN='):
                token = line.split('=', 1)[1].strip()
elif os.path.exists('/home/rycz/.hermes/.env'):
    with open('/home/rycz/.hermes/.env', 'r') as f:
        for line in f:
            if line.startswith('SLACK_BOT_TOKEN='):
                token = line.split('=', 1)[1].strip()

if not token:
    print("SLACK_BOT_TOKEN not found in .env")
    exit(1)

# Prepare message
msg = """🚀 *Olá Paulo!* Tudo bem?

Hoje é dia de avançar ainda mais na nossa jornada rumo à criptografia pós-quântica! O material de estudo do *Dia 05* foi gerado, compilado e publicado com sucesso! 🔒🖥️

Estudamos sobre a *Criptografia Pós-Quântica em Navegadores Web e PKI: A Adoção no Client-Side e o Cronograma das ACs em 2026*. Compreendemos a enorme lacuna entre o suporte quase universal nos navegadores (como Chrome, Firefox e Safari negociando trocas híbridas X25519+ML-KEM por padrão) e o atraso na adoção em servidores (~8.6% do top 1M) e na infraestrutura de chaves públicas (PKI), onde as ACs preveem os primeiros certificados pós-quânticos apenas para o final de 2026/2027 devido aos grandes tamanhos de assinatura e fragmentação de pacotes TCP.

Aqui estão os links diretos para os PDFs de hoje no GitHub:
📄 *English (EN):* https://github.com/paulocauca/pqc/blob/main/en/2026-07-12-browser_pqc_pki_transition.pdf
📄 *Português (PT-BR):* https://github.com/paulocauca/pqc/blob/main/pt-BR/2026-07-12-browser_pqc_pki_transition.pdf

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
