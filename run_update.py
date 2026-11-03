
import sys
sys.path.append('/home/rycz/pqc/scripts')
from daily_updater import update_repo

day_str = "36"
date_str = "2026-10-21"
topic_en = "PQC's Impact on Blockchain and Cryptocurrencies"
topic_pt = "O Impacto da PQC em Blockchain e Criptomoedas"
file_name_prefix = "pqc_blockchain_impact"
category_en = "PQC Adoption & Industry Status"
category_pt = "Adoção da PQC e Status da Indústria"
content_en = """<h2>PQC's Impact on Blockchain and Cryptocurrencies</h2>
<p>As quantum computers become more powerful, the cryptographic foundations of blockchain and cryptocurrencies face an existential threat. This study explores the vulnerabilities and the ongoing transition to quantum-resistant solutions.</p>

<h3>The Quantum Threat to Blockchain</h3>
<p>Blockchain's security relies heavily on classical cryptographic algorithms, primarily the Elliptic Curve Digital Signature Algorithm (ECDSA) for digital signatures. These signatures are used to authorize transactions and prove ownership of assets. Shor's algorithm, which can run on a sufficiently powerful quantum computer, can break ECDSA, allowing malicious actors to forge signatures and steal funds.</p>

<div class="highlight-box">
  <p><strong>Key Vulnerability:</strong> Address reuse. When a cryptocurrency address is used multiple times, its public key is exposed, making it a target for quantum attacks.</p>
</div>

<h3>Transitioning to Quantum-Resistant Blockchains</h3>
<p>The blockchain community is actively researching and developing quantum-resistant solutions. The primary approach is to replace ECDSA with PQC digital signature algorithms like ML-DSA and SLH-DSA.</p>

<h4>Key Challenges in the Transition</h4>
<ul>
    <li><b>Signature Size:</b> PQC signature algorithms often have larger signature sizes compared to ECDSA, which can increase transaction size and fees.</li>
    <li><b>Verification Time:</b> PQC algorithms may have different performance characteristics, impacting transaction verification times and overall network throughput.</li>
    <li><b>Forking:</b> Upgrading a blockchain to be quantum-resistant often requires a hard fork, which can be a contentious and disruptive process.</li>
</ul>

<table class="comparison-table">
  <caption>ECDSA vs. PQC Signatures (Illustrative)</caption>
  <thead>
    <tr>
      <th>Algorithm</th>
      <th>Key Size (bytes)</th>
      <th>Signature Size (bytes)</th>
      <th>Quantum Resistance</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>ECDSA (secp256k1)</td>
      <td>32 (private), 65 (uncompressed public)</td>
      <td>64-72</td>
      <td>No</td>
    </tr>
    <tr>
      <td>ML-DSA-44</td>
      <td>~1.3KB (private), ~1.3KB (public)</td>
      <td>~2.4KB</td>
      <td>Yes</td>
    </tr>
     <tr>
      <td>SLH-DSA-128s</td>
      <td>~32 (private), ~16 (public)</td>
      <td>~7.8KB</td>
      <td>Yes</td>
    </tr>
  </tbody>
</table>

<h3>Daily Quiz</h3>
<ol>
  <li>What is the primary quantum threat to cryptocurrencies like Bitcoin?</li>
  <li>What is one of the main challenges of transitioning a blockchain to use PQC algorithms?</li>
  <li>Which NIST-standardized PQC algorithm is a candidate for replacing ECDSA in blockchains?</li>
</ol>"""
content_pt = """<h2>O Impacto da PQC em Blockchain e Criptomoedas</h2>
<p>À medida que os computadores quânticos se tornam mais poderosos, as bases criptográficas do blockchain e das criptomoedas enfrentam uma ameaça existencial. Este estudo explora as vulnerabilidades e a transição em andamento para soluções quântico-resistentes.</p>

<h3>A Ameaça Quântica ao Blockchain</h3>
<p>A segurança do blockchain depende fortemente de algoritmos criptográficos clássicos, principalmente o Elliptic Curve Digital Signature Algorithm (ECDSA) para assinaturas digitais. Essas assinaturas são usadas para autorizar transações e provar a propriedade de ativos. O algoritmo de Shor, que pode ser executado em um computador quântico suficientemente poderoso, pode quebrar o ECDSA, permitindo que agentes mal-intencionados falsifiquem assinaturas e roubem fundos.</p>

<div class="highlight-box">
  <p><strong>Principal Vulnerabilidade:</strong> Reutilização de endereços. Quando um endereço de criptomoeda é usado várias vezes, sua chave pública é exposta, tornando-o um alvo para ataques quânticos.</p>
</div>

<h3>Transição para Blockchains Quântico-Resistentes</h3>
<p>A comunidade blockchain está pesquisando e desenvolvendo ativamente soluções quântico-resistentes. A abordagem principal é substituir o ECDSA por algoritmos de assinatura digital PQC como ML-DSA e SLH-DSA.</p>

<h4>Principais Desafios na Transição</h4>
<ul>
    <li><b>Tamanho da Assinatura:</b> Os algoritmos de assinatura PQC geralmente têm tamanhos de assinatura maiores em comparação com o ECDSA, o que pode aumentar o tamanho da transação e as taxas.</li>
    <li><b>Tempo de Verificação:</b> Os algoritmos PQC podem ter características de desempenho diferentes, impactando os tempos de verificação de transações e o rendimento geral da rede.</li>
    <li><b>Forking:</b> A atualização de um blockchain para ser quântico-resistente geralmente requer um hard fork, que pode ser um processo controverso e disruptivo.</li>
</ul>

<table class="comparison-table">
  <caption>ECDSA vs. Assinaturas PQC (Ilustrativo)</caption>
  <thead>
    <tr>
      <th>Algoritmo</th>
      <th>Tamanho da Chave (bytes)</th>
      <th>Tamanho da Assinatura (bytes)</th>
      <th>Resistência Quântica</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>ECDSA (secp256k1)</td>
      <td>32 (privada), 65 (pública não comprimida)</td>
      <td>64-72</td>
      <td>Não</td>
    </tr>
    <tr>
      <td>ML-DSA-44</td>
      <td>~1.3KB (privada), ~1.3KB (pública)</td>
      <td>~2.4KB</td>
      <td>Sim</td>
    </tr>
     <tr>
      <td>SLH-DSA-128s</td>
      <td>~32 (privada), ~16 (pública)</td>
      <td>~7.8KB</td>
      <td>Sim</td>
    </tr>
  </tbody>
</table>

<h3>Auto-avaliação</h3>
<ol>
  <li>Qual é a principal ameaça quântica para criptomoedas como o Bitcoin?</li>
  <li>Qual é um dos principais desafios da transição de um blockchain para usar algoritmos PQC?</li>
  <li>Qual algoritmo PQC padronizado pelo NIST é um candidato para substituir o ECDSA em blockchains?</li>
</ol>"""
references_md = ""

success = update_repo(day_str, date_str, topic_en, topic_pt, file_name_prefix, category_en, category_pt, content_en, content_pt, references_md)
print("UPDATE STATUS:", success)
