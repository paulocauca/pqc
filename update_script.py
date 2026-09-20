
import sys
sys.path.append('/home/rycz/pqc/scripts')
from daily_updater import update_repo

day_str = "27"
date_str = "2026-09-20"
topic_en = "PQC in QUIC and HTTP/3: Securing the Next-Generation Internet"
topic_pt = "PQC em QUIC e HTTP/3: Protegendo a Próxima Geração da Internet"
file_name_prefix = "pqc_quic_http3_integration"
category_en = "Network Protocol Integration"
category_pt = "Integração em Protocolos de Rede"
content_en = """<h2>PQC in QUIC and HTTP/3: Securing the Next-Generation Internet</h2>
<p>As the internet transitions to faster and more efficient protocols like QUIC and HTTP/3, ensuring their cryptographic foundations are secure against future quantum threats is paramount. The integration of Post-Quantum Cryptography (PQC) into these modern protocols presents unique challenges and opportunities, primarily centered around maintaining low latency and high performance.</p>

<h3>The Challenge: Latency in Connection Establishment</h3>
<p>QUIC, which runs over UDP, is designed to reduce connection establishment latency compared to traditional TCP+TLS. A standard TLS 1.3 handshake requires one round-trip time (1-RTT). QUIC improves this with a 0-RTT connection resumption feature. The introduction of larger PQC key encapsulation mechanisms (KEMs) and digital signatures can increase the size of handshake packets, potentially negating QUIC's low-latency benefits.</p>
<div class="highlight-box">
  <p><strong>Key Consideration:</strong> The larger ciphertext and public key sizes of ML-KEM, and especially the large signature sizes of SLH-DSA, can increase the amount of data exchanged during the initial handshake, which could lead to packet fragmentation and retransmissions, thereby increasing latency.</p>
</div>

<h3>Hybrid Key Exchange: The Pragmatic Approach</h3>
<p>Similar to TLS 1.3, the initial strategy for integrating PQC into QUIC is the hybrid key exchange model. This approach combines a classical key exchange algorithm (like X25519) with a post-quantum one (like ML-KEM-768). This ensures that the connection remains secure against classical attacks, while also providing protection against quantum adversaries.</p>
<ul>
  <li><strong>Benefit 1 (Security):</strong> It provides a safety net. If a flaw is discovered in the PQC algorithm, the connection is still protected by the well-vetted classical cryptography.</li>
  <li><strong>Benefit 2 (Compliance):</strong> It allows for a gradual transition, meeting current security requirements while preparing for future ones.</li>
</ul>

<h3>Performance Metrics: PQC's Impact on QUIC</h3>
<p>Recent research and experiments from organizations like Cloudflare and Google have focused on quantifying the impact of PQC on QUIC's performance. The table below summarizes the expected overhead.</p>

<table class="comparison-table">
  <thead>
    <tr>
      <th>Key Exchange Mechanism</th>
      <th>Added Handshake Latency (ms)</th>
      <th>Increase in Handshake Size (Bytes)</th>
      <th>Primary Use Case</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>X25519 (Classical)</td>
      <td>Baseline</td>
      <td>Baseline (~100 B)</td>
      <td>Standard TLS/QUIC</td>
    </tr>
    <tr>
      <td>X25519 + ML-KEM-768 (Hybrid)</td>
      <td>+5-15 ms</td>
      <td>~1,200 B</td>
      <td>Balanced Security and Performance</td>
    </tr>
    <tr>
      <td>X25519 + ML-KEM-1024 (Hybrid)</td>
      <td>+10-25 ms</td>
      <td>~1,600 B</td>
      <td>Higher Security, Moderate Performance Cost</td>
    </tr>
  </tbody>
</table>
<p><em>Note: Latency figures are estimates and can vary significantly based on network conditions and server proximity.</em></p>

<h3>The Road Ahead: Signatures and Authentication</h3>
<p>While key exchange is the primary focus, server authentication using PQC digital signatures (ML-DSA, SLH-DSA) is the next frontier. The larger size of PQC signatures, particularly stateless hash-based ones like SLH-DSA, poses a more significant challenge for QUIC's performance goals. Research is ongoing to optimize certificate chains and signature aggregation to minimize this impact.</p>

<h3>Daily Quiz</h3>
<ol>
    <li>What is the primary challenge when integrating PQC into QUIC and HTTP/3?</li>
    <li>Why is a hybrid key exchange model considered the most pragmatic approach for the initial PQC integration in QUIC?</li>
    <li>According to the comparison table, what is the estimated increase in handshake size when using a hybrid approach with X25519 and ML-KEM-768?</li>
</ol>"""
content_pt = """<h2>PQC em QUIC e HTTP/3: Protegendo a Próxima Geração da Internet</h2>
<p>À medida que a internet transita para protocolos mais rápidos e eficientes como QUIC e HTTP/3, garantir que suas bases criptográficas sejam seguras contra futuras ameaças quânticas é fundamental. A integração da Criptografia Pós-Quântica (PQC) nesses protocolos modernos apresenta desafios e oportunidades únicas, centrados principalmente na manutenção de baixa latência e alto desempenho.</p>

<h3>O Desafio: Latência no Estabelecimento da Conexão</h3>
<p>O QUIC, que opera sobre UDP, foi projetado para reduzir a latência no estabelecimento de conexões em comparação com o tradicional TCP+TLS. Um handshake padrão do TLS 1.3 requer um tempo de ida e volta (1-RTT). O QUIC melhora isso com um recurso de retomada de conexão de 0-RTT. A introdução de mecanismos de encapsulamento de chave (KEMs) e assinaturas digitais PQC, que são maiores, pode aumentar o tamanho dos pacotes de handshake, potencialmente anulando os benefícios de baixa latência do QUIC.</p>
<div class="highlight-box">
  <p><strong>Consideração Chave:</strong> Os tamanhos maiores de chaves públicas e textos cifrados do ML-KEM, e especialmente os tamanhos grandes de assinatura do SLH-DSA, podem aumentar a quantidade de dados trocados durante o handshake inicial, o que pode levar à fragmentação de pacotes e retransmissões, aumentando assim a latência.</p>
</div>

<h3>Troca de Chaves Híbrida: A Abordagem Pragmática</h3>
<p>Semelhante ao TLS 1.3, a estratégia inicial para integrar PQC ao QUIC é o modelo de troca de chaves híbrida. Esta abordagem combina um algoritmo de troca de chaves clássico (como o X25519) com um pós-quântico (como o ML-KEM-768). Isso garante que a conexão permaneça segura contra ataques clássicos, ao mesmo tempo que oferece proteção contra adversários quânticos.</p>
<ul>
  <li><strong>Benefício 1 (Segurança):</strong> Oferece uma rede de segurança. Se uma falha for descoberta no algoritmo PQC, a conexão ainda estará protegida pela criptografia clássica bem estabelecida.</li>
  <li><strong>Benefício 2 (Conformidade):</strong> Permite uma transição gradual, atendendo aos requisitos de segurança atuais enquanto se prepara para os futuros.</li>
</ul>

<h3>Métricas de Desempenho: O Impacto da PQC no QUIC</h3>
<p>Pesquisas e experimentos recentes de organizações como Cloudflare e Google focaram em quantificar o impacto da PQC no desempenho do QUIC. A tabela abaixo resume a sobrecarga esperada.</p>

<table class="comparison-table">
  <thead>
    <tr>
      <th>Mecanismo de Troca de Chave</th>
      <th>Latência Adicionada no Handshake (ms)</th>
      <th>Aumento no Tamanho do Handshake (Bytes)</th>
      <th>Caso de Uso Principal</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>X25519 (Clássico)</td>
      <td>Linha de Base</td>
      <td>Linha de Base (~100 B)</td>
      <td>TLS/QUIC Padrão</td>
    </tr>
    <tr>
      <td>X25519 + ML-KEM-768 (Híbrido)</td>
      <td>+5-15 ms</td>
      <td>~1.200 B</td>
      <td>Segurança e Desempenho Balanceados</td>
    </tr>
    <tr>
      <td>X25519 + ML-KEM-1024 (Híbrido)</td>
      <td>+10-25 ms</td>
      <td>~1.600 B</td>
      <td>Segurança Mais Alta, Custo Moderado de Desempenho</td>
    </tr>
  </tbody>
</table>
<p><em>Nota: Os valores de latência são estimativas e podem variar significativamente com base nas condições da rede e na proximidade do servidor.</em></p>

<h3>O Caminho a Seguir: Assinaturas e Autenticação</h3>
<p>Embora a troca de chaves seja o foco principal, a autenticação do servidor usando assinaturas digitais PQC (ML-DSA, SLH-DSA) é a próxima fronteira. O tamanho maior das assinaturas PQC, particularmente as baseadas em hash sem estado como o SLH-DSA, representa um desafio mais significativo para as metas de desempenho do QUIC. Pesquisas estão em andamento para otimizar cadeias de certificados e agregação de assinaturas para minimizar esse impacto.</p>

<h3>Auto-avaliação Diária</h3>
<ol>
    <li>Qual é o principal desafio ao integrar a PQC no QUIC e no HTTP/3?</li>
    <li>Por que um modelo de troca de chaves híbrido é considerado a abordagem mais pragmática para a integração inicial da PQC no QUIC?</li>
    <li>De acordo com a tabela de comparação, qual é o aumento estimado no tamanho do handshake ao usar uma abordagem híbrida com X25519 e ML-KEM-768?</li>
</ol>"""
references_md = "[No new references for today]"

success = update_repo(day_str, date_str, topic_en, topic_pt, file_name_prefix, category_en, category_pt, content_en, content_pt, references_md)
print("UPDATE STATUS:", success)
