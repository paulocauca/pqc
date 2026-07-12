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
msg = """🎉 *Grande Paulo! Tudo excelente por aí?*

Hoje celebramos o *Dia 04* da nossa trilha especializada de criptografia pós-quântica! O novo material de estudos bilíngue foi estruturado, compilado em PDF e publicado com absoluto sucesso! 🖥️🛡️

Focamos em: *Criptografia Pós-Quântica em Redes Privadas Virtuais (VPNs): A Transição para WireGuard Híbrido e PQPSK*.

Analisamos como os túneis de VPN (alvos principais de ataques de interceptação retroativa "Harvest Now, Decrypt Later") estão evoluindo. Compreendemos o uso de chaves pré-compartilhadas pós-quânticas (PQPSKs) injetadas no handshake Noise do WireGuard (`Noise_IKpsk2_25519_ChaChaPoly_BLAKE2s`), fornecendo um escudo simétrico de 256 bits imune a ataques quânticos. Vimos também os handshakes híbridos nativos de 2026 que automatizam o processo combinando ML-KEM-768 com a Curve25519 clássica, eliminando os complexos desafios de gerenciamento de chaves manuais em larga escala!

Confira os materiais exclusivos de hoje diretamente no GitHub:
📄 *English (EN):* https://github.com/paulocauca/pqc/blob/main/en/2026-07-11-wireguard_pqc_transition.pdf
📄 *Português (PT-BR):* https://github.com/paulocauca/pqc/blob/main/pt-BR/2026-07-11-wireguard_pqc_transition.pdf

🐙 *Repositório Completo no GitHub:* https://github.com/paulocauca/pqc

Não deixe de ler este guia aprofundado, comparar as métricas e colocar seus conhecimentos à prova com o *Quiz Diário de 3 perguntas* ao final do material! 🧠🔥

Bons estudos, continue firme nessa jornada quântica e até amanhã! 🚀✨"""

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
