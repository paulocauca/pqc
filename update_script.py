
import sys
sys.path.append('/home/rycz/pqc/scripts')
from daily_updater import update_repo

day_str = "11"
date_str = "2026-07-19"
topic_en = "PQC Adoption Gap in 2026: Browser Readiness vs. Server-Side Lag"
topic_pt = "O Hiato na Adoção da PQC em 2026: Prontidão dos Navegadores vs. Atraso no Lado do Servidor"
file_name_prefix = "pqc_adoption_gap_2026"
category_en = "PQC Adoption & Industry Status"
category_pt = "Adoção da PQC e Status da Indústria"
content_en = """<h2>The PQC Adoption Gap of 2026</h2>
<p>As of mid-2026, the internet is in a critical transitional phase for post-quantum cryptography. While major web browsers have successfully rolled out support for hybrid key exchange mechanisms, the vast majority of web servers and enterprise systems are lagging significantly. This disparity has created a "PQC Adoption Gap," where the client-side is ready for a quantum-resistant future, but the server-side infrastructure remains vulnerable.</p>

<h3>Client-Side Success: Browsers are PQC-Ready</h3>
<p>All major web browsers, including Chrome, Firefox, Safari, and Edge, now enable hybrid key exchange by default. They typically use the <strong>X25519Kyber768</strong> mechanism, which combines the classical Elliptic Curve Diffie-Hellman (X25519) with the NIST-standardized ML-KEM (Kyber). This hybrid approach ensures that connections are protected against both classical and future quantum attacks. If a quantum computer were to break one algorithm, the other would still secure the connection.</p>
<div class="highlight-box">
  <h4>Applicability to Internet Protocols</h4>
  <p>This hybrid key exchange is primarily implemented within the <strong>TLS 1.3</strong> protocol, which secures the vast majority of web traffic (HTTPS). The browser's ability to negotiate a quantum-resistant key exchange is the first and most crucial step in protecting everyday internet activities like browsing, online banking, and e-commerce from the "Harvest Now, Decrypt Later" (HNDL) threat.</p>
</div>

<h3>Server-Side Lag: The Root of the Gap</h3>
<p>Despite browser readiness, studies show that server-side adoption is dangerously low. While nearly all major tech giants (Google, Cloudflare, etc.) have updated their servers, the broader internet has not. Estimates from mid-2026 indicate:</p>
<ul>
    <li>Around 40% of the top 100 websites support hybrid PQC.</li>
    <li>This number drops to less than 10% for the top 1 million websites.</li>
    <li>Internal enterprise systems and smaller organizations are estimated to have less than 2% adoption.</li>
</ul>
<p>This lag is due to the operational complexity, cost, and compatibility challenges associated with upgrading server software, network appliances, and cryptographic libraries. Many organizations are waiting for clearer guidance or are struggling to prioritize the migration amidst other business needs.</p>

<h3>Adoption Status Comparison (Mid-2026)</h3>
<table class="comparison-table">
  <thead>
    <tr>
      <th>Component</th>
      <th>PQC Readiness Status</th>
      <th>Primary Mechanism</th>
      <th>Key Takeaway</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Major Web Browsers</td>
      <td style="color: green;"><strong>High</strong></td>
      <td>X25519Kyber768 (Default Enabled)</td>
      <td>The client-side is largely prepared and actively attempting PQC negotiations.</td>
    </tr>
    <tr>
      <td>Large Tech/CDN Servers</td>
      <td style="color: orange;"><strong>Medium-High</strong></td>
      <td>ML-KEM support is widespread</td>
      <td>The backbone of the modern web is quickly becoming quantum-resistant.</td>
    </tr>
    <tr>
      <td>General Web Servers (Top 1M)</td>
      <td style="color: red;"><strong>Very Low</strong></td>
      <td>Primarily classical (RSA/ECDH)</td>
      <td>The "long tail" of the internet remains highly vulnerable to HNDL attacks.</td>
    </tr>
    <tr>
      <td>Enterprise Internal Systems</td>
      <td style="color: red;"><strong>Critically Low</strong></td>
      <td>Legacy classical algorithms</td>
      <td>Represents a significant risk for corporate data and critical infrastructure.</td>
    </tr>
  </tbody>
</table>

<h3>Daily Quiz</h3>
<p>Test your knowledge of today's topic:</p>
<ol>
    <li>What is the "PQC Adoption Gap"?</li>
    <li>What specific hybrid key exchange mechanism is commonly used by modern browsers?</li>
    <li>Why does the server-side lag in PQC adoption pose a significant risk even if browsers are ready?</li>
</ol>"""
content_pt = """<h2>O Hiato na Adoção da PQC em 2026</h2>
<p>Em meados de 2026, a internet encontra-se em uma fase de transição crítica para a criptografia pós-quântica. Embora os principais navegadores web já tenham implementado com sucesso o suporte a mecanismos de troca de chaves híbrida, a grande maioria dos servidores web e sistemas corporativos está significativamente atrasada. Essa disparidade criou um "Hiato na Adoção da PQC", onde o lado do cliente está pronto para um futuro quântico-resistente, mas a infraestrutura do lado do servidor permanece vulnerável.</p>

<h3>Sucesso no Lado do Cliente: Navegadores Estão Prontos para a PQC</h3>
<p>Todos os principais navegadores, incluindo Chrome, Firefox, Safari e Edge, agora habilitam a troca de chaves híbrida por padrão. Eles normalmente utilizam o mecanismo <strong>X25519Kyber768</strong>, que combina o clássico Elliptic Curve Diffie-Hellman (X25519) com o ML-KEM (Kyber), padronizado pelo NIST. Essa abordagem híbrida garante que as conexões estejam protegidas tanto contra ataques clássicos quanto futuros ataques quânticos. Se um computador quântico quebrar um dos algoritmos, o outro ainda garantirá a segurança da conexão.</p>
<div class="highlight-box">
  <h4>Aplicabilidade a Protocolos de Internet</h4>
  <p>Essa troca de chaves híbrida é implementada primariamente no protocolo <strong>TLS 1.3</strong>, que protege a grande maioria do tráfego web (HTTPS). A capacidade do navegador de negociar uma troca de chaves quântico-resistente é o primeiro e mais crucial passo para proteger atividades diárias na internet, como navegação, transações bancárias online e e-commerce, da ameaça "Harvest Now, Decrypt Later" (HNDL).</p>
</div>

<h3>Atraso no Lado do Servidor: A Raiz do Hiato</h3>
<p>Apesar da prontidão dos navegadores, estudos mostram que a adoção no lado do servidor é perigosamente baixa. Enquanto quase todas as gigantes de tecnologia (Google, Cloudflare, etc.) já atualizaram seus servidores, a internet em geral ainda não o fez. Estimativas de meados de 2026 indicam:</p>
<ul>
    <li>Cerca de 40% dos 100 principais websites suportam PQC híbrida.</li>
    <li>Esse número cai para menos de 10% para o top 1 milhão de websites.</li>
    <li>Sistemas corporativos internos e organizações menores têm uma adoção estimada inferior a 2%.</li>
</ul>
<p>Esse atraso deve-se à complexidade operacional, custo e desafios de compatibilidade associados à atualização de software de servidor, dispositivos de rede e bibliotecas criptográficas. Muitas organizações estão aguardando orientações mais claras ou têm dificuldade em priorizar a migração em meio a outras necessidades de negócio.</p>

<h3>Comparativo do Status de Adoção (Meados de 2026)</h3>
<table class="comparison-table">
  <thead>
    <tr>
      <th>Componente</th>
      <th>Status de Prontidão PQC</th>
      <th>Mecanismo Principal</th>
      <th>Principal Conclusão</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Principais Navegadores Web</td>
      <td style="color: green;"><strong>Alto</strong></td>
      <td>X25519Kyber768 (Habilitado por Padrão)</td>
      <td>O lado do cliente está amplamente preparado e tentando ativamente negociações PQC.</td>
    </tr>
    <tr>
      <td>Servidores de Grandes Tech/CDNs</td>
      <td style="color: orange;"><strong>Médio-Alto</strong></td>
      <td>Suporte a ML-KEM é generalizado</td>
      <td>A espinha dorsal da web moderna está se tornando rapidamente quântico-resistente.</td>
    </tr>
    <tr>
      <td>Servidores Web em Geral (Top 1M)</td>
      <td style="color: red;"><strong>Muito Baixo</strong></td>
      <td>Primariamente clássico (RSA/ECDH)</td>
      <td>A "cauda longa" da internet permanece altamente vulnerável a ataques HNDL.</td>
    </tr>
    <tr>
      <td>Sistemas Internos Corporativos</td>
      <td style="color: red;"><strong>Criticamente Baixo</strong></td>
      <td>Algoritmos clássicos legados</td>
      <td>Representa um risco significativo para dados corporativos e infraestrutura crítica.</td>
    </tr>
  </tbody>
</table>

<h3>Auto-avaliação</h3>
<p>Teste seu conhecimento sobre o tópico de hoje:</p>
<ol>
    <li>O que é o "Hiato na Adoção da PQC"?</li>
    <li>Qual mecanismo específico de troca de chaves híbrida é comumente usado pelos navegadores modernos?</li>
    <li>Por que o atraso na adoção da PQC no lado do servidor representa um risco significativo, mesmo que os navegadores estejam prontos?</li>
</ol>"""
references_md = "*   [Measurement Study of Post-Quantum Readiness of Internet: 2026 (arxiv.org)](https://arxiv.org/html/2606.16473)\\n*   [Post-Quantum Cryptography 2026: Real Status of PQC Adoption (tigertrust.io)](https://www.tigertrust.io/blog/post-quantum-cryptography-2026-status)\\n*   [The State of Post-Quantum Cryptography Adoption in 2026 (cybertechnologyinsights.com)](https://cybertechnologyinsights.com/whitepaper/the-state-of-post-quantum-cryptography-adoption-in-2026/)"

success = update_repo(day_str, date_str, topic_en, topic_pt, file_name_prefix, category_en, category_pt, content_en, content_pt, references_md)
print("UPDATE STATUS:", success)
