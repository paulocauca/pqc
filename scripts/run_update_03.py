import sys
sys.path.append('/home/rycz/pqc/scripts')
from daily_updater import update_repo

day_str = "03"
date_str = "2026-07-10"
topic_en = "Post-Quantum SSH Hardening in 2026: The Transition to mlkem768x25519-sha256 in OpenSSH"
topic_pt = "Endurecimento Pós-Quântico do SSH em 2026: A Transição para mlkem768x25519-sha256 no OpenSSH"
file_name_prefix = "openssh_pq_hardening_mlkem768"
category_en = "Network Protocol Hardening"
category_pt = "Endurecimento de Protocolo de Rede"

content_en = """<p>In the transition to post-quantum resistance, securing administrative channels is just as crucial as protecting web traffic. <strong>Secure Shell (SSH)</strong>, the backbone of modern cloud and server administration, has seen rapid PQC integration. While previous versions relied on experimental hybrid options (like <code>sntrup761x25519-sha512</code>), modern implementations like <strong>OpenSSH 9.9 (and newer)</strong> and platforms like <strong>Ubuntu 26.04 LTS</strong> have established <code>mlkem768x25519-sha256</code> as the preferred default key exchange (KEX) mechanism.</p>

<div class="highlight-box">
    <p><strong>Underlying Security Principle:</strong> The key exchange algorithm <code>mlkem768x25519-sha256</code> is a hybrid mechanism. It combines <strong>ML-KEM-768</strong> (the NIST FIPS 203 module-lattice-based key encapsulation mechanism) with the classical <strong>X25519</strong> elliptic curve Diffie-Hellman (ECDH), binding them using a SHA-256-based KDF. This "hybrid" design ensures that if ML-KEM is ever broken by future mathematical breakthroughs, the connection remains as secure as standard X25519.</p>
</div>

<h2>The Evolution of PQ-KEX in OpenSSH</h2>
<p>To understand the current state, we must look at how OpenSSH managed its post-quantum transition:</p>
<ul>
    <li><strong>OpenSSH 8.5 to 9.8:</strong> Introduced and defaulted to <code>sntrup761x25519</code> (combining Streamlined NTRU Prime 761 and X25519) because NTRU Prime was considered highly conservative and immune to certain patent concerns. However, it was not the final NIST standard.</li>
    <li><strong>OpenSSH 9.9:</strong> Following the official publication of FIPS 203 by NIST in late 2024, OpenSSH introduced <code>mlkem768x25519-sha256</code> and made it the highest-priority key exchange algorithm, while deprecating and removing obsolete algorithms like DSA.</li>
    <li><strong>Ubuntu 26.04 LTS (2026):</strong> Out of the box, Ubuntu 26.04's SSH client and server negotiate <code>mlkem768x25519-sha256</code> by default, ensuring that every administrative session is quantum-safe from day one.</li>
</ul>

<h2>Configuring and Hardening OpenSSH for PQC</h2>
<p>By default, OpenSSH negotiates the strongest mutually supported algorithm. However, to comply with strict post-quantum requirements and eliminate classical fallback risks, administrators can enforce a post-quantum-only key exchange policy.</p>

<h3>Auditing the Negotiated Algorithm</h3>
<p>To inspect what key exchange algorithm was negotiated for an active session, connect using double-verbose mode (<code>-vv</code>) and grep for the key exchange (<code>kex</code>) negotiations:</p>
<pre class="code">ssh -vv user@server exit 2&gt;&amp;1 | grep "kex:"</pre>
<p>If the client and server are updated, you will see:</p>
<pre class="code">debug1: kex: algorithm: mlkem768x25519-sha256</pre>

<h3>Enforcing Post-Quantum-Only KEX</h3>
<p>To restrict your server to only accept post-quantum and hybrid key exchanges, edit your SSH daemon configuration (e.g., in <code>/etc/ssh/sshd_config.d/99-pqc.conf</code>):</p>
<div class="highlight-box">
    <p><strong>Configuration Snippet:</strong></p>
    <pre class="code"># Force post-quantum hybrid key exchange only
KexAlgorithms mlkem768x25519-sha256,sntrup761x25519-sha512

# Enable verbose logging to audit client connection capabilities
LogLevel VERBOSE</pre>
</div>
<p>Before restarting the daemon, always validate the syntax to avoid locking yourself out: <code>sudo sshd -t</code>. Once verified, restart with <code>sudo systemctl restart ssh</code>.</p>

<h2>Algorithm & Performance Comparison in SSH</h2>
<p>The following table outlines the key exchange algorithms available in modern SSH daemons and their corresponding operational metrics:</p>

<table class="comparison-table">
    <thead>
        <tr>
            <th>Algorithm Name</th>
            <th>Type</th>
            <th>Key Exchange Overhead (Bytes)</th>
            <th>Cryptographic Foundation</th>
            <th>Quantum-Resistant?</th>
            <th>Production Status (2026)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>curve25519-sha256</strong></td>
            <td>Classical ECDH</td>
            <td>64</td>
            <td>Curve25519 (Discrete Logarithm)</td>
            <td>No</td>
            <td>Fallback Only</td>
        </tr>
        <tr>
            <td><strong>sntrup761x25519-sha512</strong></td>
            <td>Hybrid KEM</td>
            <td>~1,200</td>
            <td>NTRU Prime + X25519</td>
            <td>Yes (Hybrid)</td>
            <td>Supported (Legacy PQ)</td>
        </tr>
        <tr>
            <td><strong>mlkem768x25519-sha256</strong></td>
            <td>Hybrid KEM</td>
            <td>~2,300</td>
            <td>ML-KEM-768 (M-LWE) + X25519</td>
            <td>Yes (Hybrid)</td>
            <td><strong>Default Standard</strong></td>
        </tr>
    </tbody>
</table>

<div class="page-break"></div>

<h2>Daily Quiz: Test Your Understanding</h2>
<ol>
    <li><strong>Why is <code>mlkem768x25519-sha256</code> preferred over <code>sntrup761x25519-sha512</code> in OpenSSH 9.9 and modern operating systems like Ubuntu 26.04?</strong>
        <br><em>A) Because NTRU Prime was found to be completely broken by classical linear computers.</em>
        <br><em>B) Because ML-KEM-768 is the official NIST standard (FIPS 203), whereas NTRU Prime was not selected by NIST.</em>
        <br><em>C) Because ML-KEM-768 has significantly smaller public keys than curve25519.</em>
        <br><strong>Correct Answer: B.</strong> Although NTRU Prime is a secure and highly respected scheme (and was used as a stopgap measure), ML-KEM is the standardized post-quantum algorithm defined in NIST's FIPS 203, making it the globally accepted compliance baseline.
    </li>
    <br>
    <li><strong>What is the primary risk of not configuring a post-quantum key exchange on an SSH server today?</strong>
        <br><em>A) Attackers can instantly hack the SSH session using modern quantum computers available in 2026.</em>
        <br><em>B) Legacy SSH clients will not be able to connect to the server anymore.</em>
        <br><em>C) Sessions are vulnerable to "Harvest Now, Decrypt Later" (HNDL) attacks, where encrypted administrative sessions are recorded now and decrypted once a cryptographically relevant quantum computer is available.</em>
        <br><strong>Correct Answer: C.</strong> Symmetric session keys negotiated using classical Diffie-Hellman or ECDH are vulnerable to retroactive decryption once Shor's algorithm can be run on a quantum computer.
    </li>
    <br>
    <li><strong>What command is used to safely verify the SSH server configuration after hardening it with PQC-only algorithms?</strong>
        <br><em>A) <code>sudo systemctl restart ssh</code></em>
        <br><em>B) <code>sudo sshd -t</code></em>
        <br><em>C) <code>ssh-keygen -A</code></em>
        <br><strong>Correct Answer: B.</strong> <code>sudo sshd -t</code> tests the configuration files for syntax errors without restarting the SSH daemon. Running this command prevents locking yourself out of a remote server due to a typo.
    </li>
</ol>"""

content_pt = """<p>Na transição para a resistência pós-quântica, proteger os canais administrativos é tão crucial quanto proteger o tráfego web normal. O <strong>Secure Shell (SSH)</strong>, que é a espinha dorsal da administração moderna de servidores e nuvem, passou por uma rápida integração com a Criptografia Pós-Quântica (PQC). Enquanto as versões anteriores do OpenSSH dependiam de opções híbridas experimentais (como o <code>sntrup761x25519-sha512</code>), implementações modernas como o <strong>OpenSSH 9.9 (e mais recentes)</strong> e sistemas como o <strong>Ubuntu 26.04 LTS</strong> estabeleceram o algoritmo <code>mlkem768x25519-sha256</code> como o mecanismo padrão e preferencial de troca de chaves (KEX).</p>

<div class="highlight-box">
    <p><strong>Princípio de Segurança Subjacente:</strong> O algoritmo de troca de chaves <code>mlkem768x25519-sha256</code> é um mecanismo híbrido. Ele combina o <strong>ML-KEM-768</strong> (o mecanismo de encapsulamento de chave baseado em reticulados do padrão oficial NIST FIPS 203) com a curva elíptica clássica Diffie-Hellman <strong>X25519</strong>, vinculando-os através de uma KDF baseada em SHA-256. Este design "híbrido" garante que se o ML-KEM vier a ser quebrado por futuras descobertas matemáticas, a conexão permanecerá tão segura quanto uma sessão clássica com X25519.</p>
</div>

<h2>A Evolução da Troca de Chaves Pós-Quântica no OpenSSH</h2>
<p>Para entender o estado atual, devemos analisar como o OpenSSH gerenciou essa transição pós-quântica:</p>
<ul>
    <li><strong>OpenSSH 8.5 até 9.8:</strong> Introduziu e definiu como padrão o <code>sntrup761x25519</code> (combinando Streamlined NTRU Prime 761 e X25519) porque o NTRU Prime era considerado uma escolha conservadora e imune a questões de patentes. No entanto, não foi o algoritmo final escolhido pelo NIST.</li>
    <li><strong>OpenSSH 9.9:</strong> Após a publicação oficial do padrão FIPS 203 pelo NIST no final de 2024, o OpenSSH introduziu o <code>mlkem768x25519-sha256</code>, tornando-o o algoritmo de troca de chaves de maior prioridade, e removeu algoritmos obsoletos como o DSA.</li>
    <li><strong>Ubuntu 26.04 LTS (2026):</strong> De forma nativa, o cliente e o servidor SSH do Ubuntu 26.04 negociam o <code>mlkem768x25519-sha256</code> por padrão, garantindo sessões administrativas seguras contra ameaças quânticas desde o primeiro dia de instalação.</li>
</ul>

<h2>Configuração e Endurecimento (Hardening) do OpenSSH para PQC</h2>
<p>Por padrão, o OpenSSH negocia o algoritmo mais forte suportado por ambas as pontas. Contudo, para atender a requisitos rigorosos de segurança pós-quântica e eliminar riscos de queda para algoritmos clássicos, os administradores podem forçar uma política estrita que aceita apenas trocas de chaves pós-quânticas.</p>

<h3>Auditando o Algoritmo Negociado</h3>
<p>Para inspecionar qual algoritmo de troca de chaves foi negociado em uma sessão ativa, conecte-se usando o modo duplo-detalhado (<code>-vv</code>) e filtre as linhas de negociação (<code>kex</code>):</p>
<pre class="code">ssh -vv usuario@servidor exit 2&gt;&amp;1 | grep "kex:"</pre>
<p>Se o cliente e o servidor estiverem atualizados, você verá a confirmação na saída:</p>
<pre class="code">debug1: kex: algorithm: mlkem768x25519-sha256</pre>

<h3>Forçando KEX Apenas Pós-Quântico</h3>
<p>Para restringir seu servidor SSH a aceitar somente trocas de chaves pós-quânticas ou híbridas, edite o arquivo de configuração do daemon (por exemplo, em <code>/etc/ssh/sshd_config.d/99-pqc.conf</code>):</p>
<div class="highlight-box">
    <p><strong>Trecho de Configuração:</strong></p>
    <pre class="code"># Forçar apenas trocas de chave híbridas pós-quânticas
KexAlgorithms mlkem768x25519-sha256,sntrup761x25519-sha512

# Habilitar logs detalhados para auditar capacidades dos clientes
LogLevel VERBOSE</pre>
</div>
<p>Antes de reiniciar o serviço, sempre valide a sintaxe dos arquivos para evitar perder o acesso remoto ao servidor: <code>sudo sshd -t</code>. Uma vez validado, reinicie o daemon com <code>sudo systemctl restart ssh</code>.</p>

<h2>Comparação de Algoritmos e Desempenho no SSH</h2>
<p>A tabela a seguir apresenta os principais algoritmos de troca de chaves disponíveis nos daemons SSH modernos e seus respectivos parâmetros operacionais:</p>

<table class="comparison-table">
    <thead>
        <tr>
            <th>Nome do Algoritmo</th>
            <th>Tipo</th>
            <th>Sobrecarga da Troca de Chaves (Bytes)</th>
            <th>Fundamentação Criptográfica</th>
            <th>Resistente a Quântico?</th>
            <th>Status de Produção (2026)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>curve25519-sha256</strong></td>
            <td>ECDH Clássico</td>
            <td>64</td>
            <td>Curve25519 (Logaritmo Discreto)</td>
            <td>Não</td>
            <td>Apenas Fallback</td>
        </tr>
        <tr>
            <td><strong>sntrup761x25519-sha512</strong></td>
            <td>KEM Híbrido</td>
            <td>~1.200</td>
            <td>NTRU Prime + X25519</td>
            <td>Sim (Híbrido)</td>
            <td>Suportado (Legado PQ)</td>
        </tr>
        <tr>
            <td><strong>mlkem768x25519-sha256</strong></td>
            <td>KEM Híbrido</td>
            <td>~2.300</td>
            <td>ML-KEM-768 (M-LWE) + X25519</td>
            <td>Sim (Híbrido)</td>
            <td><strong>Padrão Atual</strong></td>
        </tr>
    </tbody>
</table>

<div class="page-break"></div>

<h2>Quiz Diário: Teste seu Conhecimento</h2>
<ol>
    <li><strong>Por que o <code>mlkem768x25519-sha256</code> é preferido em relação ao <code>sntrup761x25519-sha512</code> no OpenSSH 9.9 e em sistemas operacionais modernos como o Ubuntu 26.04?</strong>
        <br><em>A) Porque o NTRU Prime foi totalmente quebrado por computadores lineares clássicos.</em>
        <br><em>B) Porque o ML-KEM-768 é o padrão oficial do NIST (FIPS 203), enquanto o NTRU Prime não foi selecionado no portfólio final do NIST.</em>
        <br><em>C) Porque o ML-KEM-768 possui chaves públicas significativamente menores do que a curve25519.</em>
        <br><strong>Resposta Correta: B.</strong> Embora o NTRU Prime seja um esquema seguro e respeitável (e tenha sido muito útil como solução temporária), o ML-KEM é o algoritmo pós-quântico oficial definido na publicação FIPS 203 do NIST, tornando-se a linha de base de conformidade aceita globalmente.
    </li>
    <br>
    <li><strong>Qual é o principal risco de não configurar uma troca de chaves pós-quântica em um servidor SSH atualmente?</strong>
        <br><em>A) Invasores podem invadir instantaneamente a sessão SSH usando computadores quânticos comerciais já em 2026.</em>
        <br><em>B) Clientes SSH antigos não conseguirão mais se conectar ao servidor.</em>
        <br><em>C) Sessões ficam vulneráveis a ataques do tipo "Harvest Now, Decrypt Later" (Coletar Agora, Decifrar Depois), em que as sessões administrativas cifradas são gravadas hoje e decifradas no futuro quando um computador quântico viável surgir.</em>
        <br><strong>Resposta Correta: C.</strong> As chaves de sessão simétricas acordadas usando Diffie-Hellman ou ECDH clássicos são vulneráveis à decifragem retrospectiva via algoritmo de Shor quando um computador quântico potente o suficiente estiver disponível.
    </li>
    <br>
    <li><strong>Qual comando é usado para verificar com segurança a configuração do servidor SSH após endurecê-lo com algoritmos apenas pós-quânticos?</strong>
        <br><em>A) <code>sudo systemctl restart ssh</code></em>
        <br><em>B) <code>sudo sshd -t</code></em>
        <br><em>C) <code>ssh-keygen -A</code></em>
        <br><strong>Resposta Correta: B.</strong> O comando <code>sudo sshd -t</code> testa os arquivos de configuração em busca de erros de sintaxe sem reiniciar o daemon SSH. Executar este comando evita que você perca o acesso a um servidor remoto devido a um erro de digitação.
    </li>
</ol>"""

references_md = """* [OpenSSH Post-Quantum Cryptography](https://www.openssh.org/pq.html) (2025/2026)
* [Ubuntu 26.04 Post-Quantum SSH Hardening](https://computingforgeeks.com/ubuntu-2604-post-quantum-ssh-hardening/) (April 2026)
* [OpenSSH 9.9 released with mlkem768x25519-sha256 - 4sysops](https://4sysops.com/archives/openssh-99-new-features-enhanced-security-with-post-quantum-key-exchange-mlkem768x25519-sha256-and-dsa-removal) (November 2024)"""

success = update_repo(day_str, date_str, topic_en, topic_pt, file_name_prefix, category_en, category_pt, content_en, content_pt, references_md)
print("UPDATE STATUS:", success)
