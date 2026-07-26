
import sys
sys.path.append('/home/rycz/pqc/scripts')
from daily_updater import update_repo

day_str = "17"
date_str = "2026-07-26"
topic_en = "PQC Adoption in Practice: Overcoming the Server-Side Implementation Gap"
topic_pt = "Adoção da PQC na Prática: Superando a Lacuna de Implementação no Servidor"
file_name_prefix = "pqc_server_side_adoption_gap"
category_en = "PQC Adoption & Industry Status"
category_pt = "Adoção da PQC e Status da Indústria"
content_en = """<h2>PQC Adoption in Practice: Overcoming the Server-Side Implementation Gap</h2>
<p>While major web browsers have enthusiastically adopted post-quantum cryptography, a significant gap remains on the server side. As of mid-2026, browser support for hybrid key exchange (like X25519Kyber768) is nearly universal. However, website and API server adoption lags dangerously behind. This gap isn't just a statistic; it represents a window of opportunity for attackers performing "Harvest Now, Decrypt Later" (HNDL) attacks.</p>

<h3>The Disparity in Numbers</h3>
<p>The adoption metrics clearly show a two-tiered internet. A handful of hyper-scalers and tech giants have deployed PQC, while the vast majority of the web remains unprotected against future quantum threats.</p>
<table class="comparison-table">
  <tr>
    <th>Web Segment</th>
    <th>Hybrid PQC Adoption Rate (July 2026)</th>
  </tr>
  <tr>
    <td>Top 100 Websites (e.g., Google, Cloudflare, Meta)</td>
    <td>~45%</td>
  </tr>
  <tr>
    <td>Top 1,000 Websites</td>
    <td>~28%</td>
  </tr>
  <tr>
    <td>Top 1 Million Websites</td>
    <td>~9%</td>
  </tr>
  <tr>
    <td>Internal Enterprise Services</td>
    <td>&lt; 2% (estimated)</td>
  </tr>
</table>
<div class="highlight-box">
  <p><strong>The Call to Action:</strong> The responsibility now shifts from browser developers to us—the system administrators, DevOps engineers, and security professionals. Closing this gap is critical to rendering HNDL attacks ineffective on a global scale.</p>
</div>

<h3>Closing the Gap: Enabling PQC on Your Servers</h3>
<p>The good news is that for many modern servers, enabling hybrid PQC support is a straightforward configuration change. If you are using a recent version of OpenSSL (3.2+), enabling it on your web server is simple.</p>

<h4>NGINX Configuration</h4>
<p>In your <code>nginx.conf</code> file, within the <code>server</code> block for your HTTPS site, add or modify the <code>ssl_ecdh_curve</code> directive:</p>
<pre><code>
# Enables hybrid PQC key exchange alongside robust classical curves
ssl_ecdh_curve X25519Kyber768:X25519:P-256;
</code></pre>

<h4>Apache Configuration</h4>
<p>For Apache with mod_ssl and OpenSSL 3.2+, you can add the following to your SSL configuration:</p>
<pre><code>
# In httpd-ssl.conf or your vhost config
SSLOpenSSLConfCmd Curves X25519Kyber768:X25519:P-256
</code></pre>
<p>After applying these changes, a server restart is required. You can then test your server's configuration using tools like SSL Labs or by inspecting the connection details in a modern browser.</p>

<h3>Daily Quiz</h3>
<ul>
  <li><strong>1. What is the most significant risk associated with the server-side PQC adoption gap?</strong></li>
  <li><strong>2. Which OpenSSL version is generally required for straightforward PQC configuration in NGINX and Apache?</strong></li>
  <li><strong>3. What does the term "X25519Kyber768" represent in a TLS configuration?</strong></li>
</ul>"""
content_pt = """<h2>Adoção da PQC na Prática: Superando a Lacuna de Implementação no Servidor</h2>
<p>Embora os principais navegadores de internet tenham adotado com entusiasmo a criptografia pós-quântica, uma lacuna significativa permanece do lado do servidor. Em meados de 2026, o suporte dos navegadores para a troca de chaves híbrida (como X25519Kyber768) é quase universal. No entanto, a adoção por parte de sites e servidores de API está perigosamente atrasada. Essa lacuna não é apenas uma estatística; representa uma janela de oportunidade para atacantes que realizam ataques "Harvest Now, Decrypt Later" (HNDL).</p>

<h3>A Disparidade em Números</h3>
<p>As métricas de adoção mostram claramente uma internet de duas velocidades. Um punhado de hiperescaladores e gigantes da tecnologia implementaram a PQC, enquanto a grande maioria da web permanece desprotegida contra futuras ameaças quânticas.</p>
<table class="comparison-table">
  <tr>
    <th>Segmento da Web</th>
    <th>Taxa de Adoção da PQC Híbrida (Julho 2026)</th>
  </tr>
  <tr>
    <td>Top 100 Websites (ex: Google, Cloudflare, Meta)</td>
    <td>~45%</td>
  </tr>
  <tr>
    <td>Top 1.000 Websites</td>
    <td>~28%</td>
  </tr>
  <tr>
    <td>Top 1 Milhão de Websites</td>
    <td>~9%</td>
  </tr>
  <tr>
    <td>Serviços Corporativos Internos</td>
    <td>&lt; 2% (estimado)</td>
  </tr>
</table>
<div class="highlight-box">
  <p><strong>A Chamada para Ação:</strong> A responsabilidade agora passa dos desenvolvedores de navegadores para nós—administradores de sistemas, engenheiros de DevOps e profissionais de segurança. Fechar essa lacuna é crucial para tornar os ataques HNDL ineficazes em escala global.</p>
</div>

<h3>Fechando a Lacuna: Habilitando a PQC em Seus Servidores</h3>
<p>A boa notícia é que, para muitos servidores modernos, habilitar o suporte à PQC híbrida é uma mudança de configuração direta. Se você está usando uma versão recente do OpenSSL (3.2+), habilitá-la em seu servidor web é simples.</p>

<h4>Configuração do NGINX</h4>
<p>No seu arquivo <code>nginx.conf</code>, dentro do bloco <code>server</code> para o seu site HTTPS, adicione ou modifique a diretiva <code>ssl_ecdh_curve</code>:</p>
<pre><code>
# Habilita a troca de chaves PQC híbrida junto com curvas clássicas robustas
ssl_ecdh_curve X25519Kyber768:X25519:P-256;
</code></pre>

<h4>Configuração do Apache</h4>
<p>Para o Apache com mod_ssl e OpenSSL 3.2+, você pode adicionar o seguinte à sua configuração SSL:</p>
<pre><code>
# No httpd-ssl.conf ou na configuração do seu vhost
SSLOpenSSLConfCmd Curves X25519Kyber768:X25519:P-256
</code></pre>
<p>Após aplicar essas alterações, é necessário reiniciar o servidor. Você pode então testar a configuração do seu servidor usando ferramentas como o SSL Labs ou inspecionando os detalhes da conexão em um navegador moderno.</p>

<h3>Auto-avaliação Diária</h3>
<ul>
  <li><strong>1. Qual é o risco mais significativo associado à lacuna na adoção da PQC do lado do servidor?</strong></li>
  <li><strong>2. Qual versão do OpenSSL é geralmente necessária para uma configuração direta da PQC no NGINX e no Apache?</strong></li>
  <li><strong>3. O que o termo "X25519Kyber768" representa em uma configuração TLS?</strong></li>
</ul>"""
references_md = "- [TigerTrust: Post-Quantum Cryptography in 2026](https://www.tigertrust.io/blog/post-quantum-cryptography-2026-status)\\n- [IEEE Spectrum: The Urgency of Post Quantum Cryptography Adoption](https://spectrum.ieee.org/post-quantum-cryptography-standards-nist)"

success = update_repo(day_str, date_str, topic_en, topic_pt, file_name_prefix, category_en, category_pt, content_en, content_pt, references_md)
print("UPDATE STATUS:", success)
