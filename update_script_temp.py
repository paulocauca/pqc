
import sys
sys.path.append('/home/rycz/pqc/scripts')
from daily_updater import update_repo

day_str = "12"
date_str = "2026-07-20"
topic_en = "PQC Adoption Gap in 2026: Browser Readiness vs. Server-Side Lag"
topic_pt = "O Hiato na Adoção da PQC em 2026: Prontidão dos Navegadores vs. Atraso no Lado do Servidor"
file_name_prefix = "pqc_adoption_gap_2026"
category_en = "PQC Adoption & Industry Status"
category_pt = "Adoção da PQC e Status da Indústria"
content_en = """<h2>PQC Adoption in 2026: The Gap Between Browser and Server-Side Readiness</h2>
<p>In 2026, the transition to Post-Quantum Cryptography (PQC) has reached a critical and somewhat uneven phase. While major web browsers have become quantum-ready, the broader server-side infrastructure is lagging significantly. This creates a notable gap, where the full security benefits of PQC cannot be realized until both clients and servers are in sync. Today, we'll explore this adoption gap, analyze the metrics, and discuss its implications for internet security.</p>

<h3>Client-Side Success: Browsers Lead the Charge</h3>
<p>The client-side of the PQC transition has been a remarkable success. All major web browsers now ship with hybrid post-quantum key exchange enabled by default. This proactive approach ensures that a significant portion of internet users have the capability to establish quantum-resistant connections.</p>
<div class="highlight-box">
  <p>The primary hybrid mechanism in use is <strong>X25519Kyber768</strong>, which combines the classical Elliptic Curve Diffie-Hellman (ECDH) key exchange (X25519) with the NIST-selected PQC algorithm ML-KEM (formerly Kyber). This ensures that even if one algorithm is compromised, the connection remains secure.</p>
</div>

<h3>Server-Side Lag: The Root of the Adoption Gap</h3>
<p>While browsers are ready, they can only establish a PQC-secured connection if the web server they are communicating with also supports the new hybrid cipher suites. This is where the adoption gap becomes apparent. The rollout of PQC on the server-side is far slower and more complex, influenced by factors like software update cycles, hardware limitations, and risk management priorities.</p>

<table class="comparison-table">
  <caption>PQC Adoption Metrics (Mid-2026 Estimates)</caption>
  <thead>
    <tr>
      <th>Domain</th>
      <th>Browser Support (Client-Side)</th>
      <th>Server Support (PQC Key Exchange)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Chrome, Firefox, Safari, Edge</td>
      <td>~100% (Default Enabled)</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>Top 100 Websites</td>
      <td>N/A</td>
      <td>~40%</td>
    </tr>
    <tr>
      <td>Top 1 Million Websites</td>
      <td>N/A</td>
      <td>~8.6%</td>
    </tr>
    <tr>
      <td>Enterprise Internal Services</td>
      <td>N/A</td>
      <td>&lt; 2%</td>
    </tr>
  </tbody>
</table>

<h3>Why Does This Gap Matter?</h3>
<p>This discrepancy has several critical implications for cybersecurity:</p>
<ul>
  <li><strong>Incomplete Protection:</strong> A browser's PQC capability is dormant until it connects to a PQC-enabled server. This means that a large portion of web traffic remains vulnerable to "Harvest Now, Decrypt Later" (HNDL) attacks, where adversaries store encrypted data today to decrypt it with a future quantum computer.</li>
  <li><strong>Uneven Security Landscape:</strong> The gap creates a two-tiered internet. Connections to major tech platforms (Google, Cloudflare, etc.) are increasingly quantum-resistant, while connections to smaller businesses, public sector services, and internal enterprise applications are often not.</li>
  <li><strong>Delayed Certificate Transition:</strong> The focus so far has been on hybrid key exchange in TLS 1.3. The next major step, issuing publicly trusted PQC digital certificates (using ML-DSA/SLH-DSA), has not yet begun. This transition is expected to start with pilot programs in late 2026 and gain traction in 2027.</li>
</ul>

<h3>Daily Quiz</h3>
<ol>
    <li>What is the primary hybrid key exchange mechanism being adopted by major web browsers in 2026?</li>
    <li>What does the term "Harvest Now, Decrypt Later" (HNDL) refer to, and why is it relevant to the PQC adoption gap?</li>
    <li>According to 2026 estimates, what percentage of the top 1 million websites have enabled server-side support for PQC hybrid key exchange?</li>
</ol>"""
content_pt = """<h2>Adoção da PQC em 2026: O Hiato Entre a Prontidão dos Navegadores e do Lado do Servidor</h2>
<p>Em 2026, a transição para a Criptografia Pós-Quântica (PQC) atingiu uma fase crítica e um tanto desigual. Enquanto os principais navegadores de internet já estão prontos para a era quântica, a infraestrutura de servidores em geral está significativamente atrasada. Isso cria um hiato notável, onde os benefícios completos de segurança da PQC não podem ser realizados até que tanto clientes quanto servidores estejam em sincronia. Hoje, exploraremos esse hiato de adoção, analisaremos as métricas e discutiremos suas implicações para a segurança da internet.</p>

<h3>Sucesso no Lado do Cliente: Navegadores Lideram a Transição</h3>
<p>O lado do cliente na transição para a PQC tem sido um sucesso notável. Todos os principais navegadores web agora são distribuídos com a troca de chaves pós-quântica híbrida habilitada por padrão. Essa abordagem proativa garante que uma parcela significativa dos usuários da internet tenha a capacidade de estabelecer conexões resistentes a ataques quânticos.</p>
<div class="highlight-box">
  <p>O principal mecanismo híbrido em uso é o <strong>X25519Kyber768</strong>, que combina a troca de chaves clássica de Curva Elíptica Diffie-Hellman (ECDH) (X25519) com o algoritmo PQC selecionado pelo NIST, o ML-KEM (anteriormente Kyber). Isso garante que, mesmo que um dos algoritmos seja comprometido, a conexão permaneça segura.</p>
</div>

<h3>Atraso no Lado do Servidor: A Raiz do Hiato de Adoção</h3>
<p>Embora os navegadores estejam prontos, eles só podem estabelecer uma conexão segura com PQC se o servidor web com o qual estão se comunicando também suportar as novas suítes de cifras híbridas. É aqui que o hiato de adoção se torna aparente. A implementação da PQC no lado do servidor é muito mais lenta e complexa, influenciada por fatores como ciclos de atualização de software, limitações de hardware e prioridades de gerenciamento de risco.</p>

<table class="comparison-table">
  <caption>Métricas de Adoção da PQC (Estimativas de Meados de 2026)</caption>
  <thead>
    <tr>
      <th>Domínio</th>
      <th>Suporte em Navegadores (Lado do Cliente)</th>
      <th>Suporte em Servidores (Troca de Chaves PQC)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Chrome, Firefox, Safari, Edge</td>
      <td>~100% (Habilitado por Padrão)</td>
      <td>N/A</td>
    </tr>
    <tr>
      <td>Top 100 Websites</td>
      <td>N/A</td>
      <td>~40%</td>
    </tr>
    <tr>
      <td>Top 1 Milhão de Websites</td>
      <td>N/A</td>
      <td>~8.6%</td>
    </tr>
    <tr>
      <td>Serviços Internos Corporativos</td>
      <td>N/A</td>
      <td>&lt; 2%</td>
    </tr>
  </tbody>
</table>

<h3>Por Que Esse Hiato é Importante?</h3>
<p>Essa discrepância tem várias implicações críticas para a cibersegurança:</p>
<ul>
  <li><strong>Proteção Incompleta:</strong> A capacidade PQC de um navegador fica inativa até que ele se conecte a um servidor habilitado para PQC. Isso significa que uma grande parte do tráfego da web permanece vulnerável a ataques do tipo "Harvest Now, Decrypt Later" (HNDL), onde adversários armazenam dados criptografados hoje para descriptografá-los com um futuro computador quântico.</li>
  <li><strong>Cenário de Segurança Desigual:</strong> O hiato cria uma internet de duas camadas. As conexões com as principais plataformas de tecnologia (Google, Cloudflare, etc.) são cada vez mais resistentes a ataques quânticos, enquanto as conexões com empresas menores, serviços do setor público e aplicações corporativas internas muitas vezes não são.</li>
  <li><strong>Atraso na Transição de Certificados:</strong> O foco até agora tem sido na troca de chaves híbrida no TLS 1.3. O próximo grande passo, a emissão de certificados digitais PQC publicamente confiáveis (usando ML-DSA/SLH-DSA), ainda não começou. Espera-se que essa transição comece com programas piloto no final de 2026 e ganhe força em 2027.</li>
</ul>

<h3>Auto-avaliação</h3>
<ol>
    <li>Qual é o principal mecanismo de troca de chaves híbrida que está sendo adotado pelos principais navegadores em 2026?</li>
    <li>O que significa o termo "Harvest Now, Decrypt Later" (HNDL) e por que ele é relevante para o hiato de adoção da PQC?</li>
    <li>De acordo com as estimativas de 2026, qual a porcentagem do top 1 milhão de websites que habilitou o suporte do lado do servidor para a troca de chaves híbrida PQC?</li>
</ol>"""
references_md = "*   [TigerTrust - Post-Quantum Cryptography in 2026: Where Browsers, CAs, and Enterprises Actually Stand](https://www.tigertrust.io/blog/post-quantum-cryptography-2026-status)"

success = update_repo(day_str, date_str, topic_en, topic_pt, file_name_prefix, category_en, category_pt, content_en, content_pt, references_md)
print("UPDATE STATUS:", success)
