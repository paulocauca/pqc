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

Hoje damos mais um passo crucial em nossa jornada pós-quântica! O material de estudo do *Dia 06* foi gerado, compilado e publicado com sucesso! 🖥️🔒

O tema de hoje é extremamente importante para a segurança da cadeia de suprimentos de software: *Assinatura de Código e Atualizações de Software Pós-Quânticas: Protegendo a Cadeia de Suprimentos de Software com ML-DSA e SLH-DSA*.

Analisamos o problema da integridade de longo prazo para dispositivos com ciclos de vida operacionais longos (como IoT, dispositivos médicos e veículos). Se as chaves clássicas forem quebradas, todas as atualizações de firmware futuras e passadas perdem a garantia de autenticidade! Aprendemos a contrastar os dois grandes novos padrões do NIST:
• *ML-DSA (FIPS 204):* Baseado em reticulados modulares, com assinaturas e verificações ultrarrápidas, perfeito para distribuições gerais de software e pipelines CI/CD automatizados.
• *SLH-DSA (FIPS 205):* Baseado em hash sem estado, sem nenhuma suposição algébrica estruturada (imune a futuros avanços em criptoanálise de reticulados). Embora as assinaturas sejam maiores e o tempo de geração seja lento, sua chave pública tem apenas 32 bytes — o tamanho ideal para armazenar em fusíveis de hardware (OTP/ROM) em Secure Boot!

Aqui estão os links diretos para os PDFs de hoje no GitHub:
📄 *English (EN):* https://github.com/paulocauca/pqc/blob/main/en/2026-07-13-code_signing_pqc_transition.pdf
📄 *Português (PT-BR):* https://github.com/paulocauca/pqc/blob/main/pt-BR/2026-07-13-code_signing_pqc_transition.pdf

🐙 *Repositório GitHub:* https://github.com/paulocauca/pqc

Não deixe de ler o material completo e testar sua compreensão com o nosso *Quiz Diário de 3 perguntas* ao final do guia de hoje! Desafie seus conhecimentos! 🧠💡

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
