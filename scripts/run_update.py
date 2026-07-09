import sys
sys.path.append('/home/rycz/pqc/scripts')
from daily_updater import update_repo

day_str = "02"
date_str = "2026-07-09"
topic_en = "Hybrid Key Exchange in TLS 1.3: Combining X25519 and ML-KEM"
topic_pt = "Troca de Chaves Híbrida no TLS 1.3: Combinando X25519 e ML-KEM"
file_name_prefix = "hybrid_kem_tls13"
category_en = "Network Protocol Integration"
category_pt = "Integração de Protocolos de Rede"

content_en = """<p>As organizations prepare for the post-quantum transition, replacing classical elliptic curve cryptography (ECC) overnight carries significant risks. Lattice-based cryptography is relatively new in production environments compared to decades-old mathematical standards. To bridge this transition safely, the cryptography community has standardized <strong>Hybrid Key Encapsulation Mechanisms (Hybrid KEMs)</strong>. The primary production standard on the internet today is <code>X25519MLKEM768</code>, combining classical X25519 ECDH with the newly standardized ML-KEM-768 (FIPS 203).</p>

<div class="highlight-box">
    <p><strong>Underlying Security Principle:</strong> A hybrid KEM combines two independent key exchange mechanisms such that the resulting shared secret is secure as long as <em>at least one</em> of the constituent mechanisms remains unbroken. If a subtle flaw is discovered in ML-KEM, the classical X25519 component prevents decryption. If a quantum computer is built, the ML-KEM component blocks Shor's algorithm.</p>
</div>

<h2>How X25519MLKEM768 Works in TLS 1.3</h2>
<p>The integration of hybrid key exchange into the Transport Layer Security (TLS) 1.3 protocol operates within the standard handshake framework, introducing minimal changes to the state machine but modifying the data transmitted:</p>

<ul>
    <li><strong>Client Key Generation:</strong> The client generates a standard X25519 key pair and an ML-KEM-768 key pair. It concatenates the two public keys into a single hybrid public key.</li>
    <li><strong>Client Hello:</strong> In the <code>Supported Groups</code> extension of the <code>ClientHello</code>, the client lists <code>X25519MLKEM768</code> alongside legacy fallback groups like <code>X25519</code>. In the <code>KeyShare</code> extension, it sends the concatenated hybrid public key share, plus a standalone <code>X25519</code> public key share as a failover for legacy servers.</li>
    <li><strong>Server Encapsulation & Response:</strong> If the server supports the hybrid group, it executes classical ECDH on the X25519 share to produce a classical shared secret ($K_1$) and runs ML-KEM encapsulation on the ML-KEM-768 share to produce a ciphertext ($c_2$) and a post-quantum shared secret ($K_2$). It sends its classical public key and the post-quantum ciphertext in its <code>ServerHello</code> keyshare.</li>
    <li><strong>Key Combiner (HKDF):</strong> Both parties combine the classical and quantum secrets using a secure Key Derivation Function (KDF). To prevent active attacks where an adversary replaces a ciphertext or public key, the combiner binds the outputs together: 
    <br><span class="code">K = HKDF-Extract(Salt, K_1 || K_2 || c_1 || c_2 || pk_1 || pk_2)</span></li>
</ul>

<h2>Cybersecurity Applicability and Industry Status (2026)</h2>
<p>The primary driver for hybrid key exchange is <strong>Harvest Now, Decrypt Later (HNDL)</strong>. Adversaries are actively recording encrypted web traffic today, intending to decrypt it once a Cryptographically Relevant Quantum Computer (CRQC) becomes available. Protecting asymmetric key exchange today is critical because any data transmitted now is vulnerable to retrospective decryption.</p>

<p>By early 2026, the adoption of <code>X25519MLKEM768</code> has swept through the internet infrastructure:</p>
<ul>
    <li><strong>Web Browsers:</strong> Google Chrome (since version 131 in Nov 2024) and Mozilla Firefox (since version 132) enable this hybrid exchange by default for HTTPS.</li>
    <li><strong>Content Delivery Networks:</strong> Major CDNs like Cloudflare, Akamai, and Google Edge handle a large portion of their global TLS traffic using hybrid key exchanges, with Cloudflare reporting that over 38% of global HTTPS traffic used hybrid PQC as of early 2025.</li>
    <li><strong>Enterprise Software:</strong> In February 2026, Oracle integrated JEP 527 into JDK 27, enabling hybrid key exchange support (such as <code>X25519MLKEM768</code> and <code>SecP256r1MLKEM768</code>) by default in Java JSSE providers.</li>
</ul>

<h2>Algorithm & Performance Comparison</h2>
<table class="comparison-table">
    <thead>
        <tr>
            <th>Algorithm / Scheme</th>
            <th>Type</th>
            <th>Public Key Size (Bytes)</th>
            <th>Ciphertext / Share Size (Bytes)</th>
            <th>Security Foundation</th>
            <th>Network Overhead</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>X25519</strong></td>
            <td>Classical ECDH</td>
            <td>32</td>
            <td>32</td>
            <td>Elliptic Curve Discrete Logarithm</td>
            <td>Extremely Low (~64 bytes total)</td>
        </tr>
        <tr>
            <td><strong>ML-KEM-768</strong> (FIPS 203)</td>
            <td>Post-Quantum KEM</td>
            <td>1,184</td>
            <td>1,088</td>
            <td>Module Learning With Errors (M-LWE)</td>
            <td>Moderate (~2.2 KB total)</td>
        </tr>
        <tr>
            <td><strong>X25519MLKEM768</strong></td>
            <td>Hybrid KEM</td>
            <td>1,216</td>
            <td>1,120</td>
            <td>M-LWE + Elliptic Curves (ECDH)</td>
            <td>Moderate (~2.3 KB total; well within MTU)</td>
        </tr>
    </tbody>
</table>

<div class="page-break"></div>

<h2>Daily Quiz: Test Your Understanding</h2>
<ol>
    <li><strong>Why is a hybrid KEM like <code>X25519MLKEM768</code> preferred over a pure ML-KEM-768 deployment during the migration period?</strong>
        <br><em>A) Because ML-KEM-768 is too slow to run on modern mobile hardware without hardware acceleration.</em>
        <br><em>B) To protect against the risk of unproven or newly discovered mathematical flaws in lattice-based cryptography, while still defending against future quantum computers.</em>
        <br><em>C) Because ML-KEM-768 does not support key encapsulation and can only be used for digital signatures.</em>
        <br><strong>Correct Answer: B.</strong> The hybrid approach guarantees that security holds if <em>either</em> of the components remains secure, preventing failure if a cryptanalytic breakthrough occurs in lattice theory.
    </li>
    <br>
    <li><strong>How does the TLS 1.3 client prevent handshake failure when connecting to an older server that does not support hybrid key exchange?</strong>
        <br><em>A) By falling back to cleartext HTTP communication automatically.</em>
        <br><em>B) By sending a standalone classical X25519 public key share in the ClientHello KeyShare extension alongside the hybrid share.</em>
        <br><em>C) By using ML-KEM-768 as a signature algorithm to sign the handshake.</em>
        <br><strong>Correct Answer: B.</strong> Including a standard X25519 keyshare alongside the hybrid keyshare in the <code>KeyShare</code> extension allows legacy servers to ignore the hybrid share and perform a standard ECDH handshake.
    </li>
    <br>
    <li><strong>What is the purpose of including the public keys and ciphertexts in the KDF combiner of a hybrid KEM?</strong>
        <br><em>A) To increase the size of the shared secret so that it cannot be brute-forced.</em>
        <br><em>B) To ensure the KDF is fully compatible with SHA-256 block sizes.</em>
        <br><em>C) To bind the derived shared secret to the specific public keys and ciphertexts, preventing active attackers from substituting components of the hybrid exchange.</em>
        <br><strong>Correct Answer: C.</strong> If the KDF only combined the secrets (e.g. $H(K_1 || K_2)$), an attacker who broke one scheme could substitute their own ciphertext and force the final key without breaking the other scheme. Binding public keys and ciphertexts prevents this.
    </li>
</ol>"""

content_pt = """<p>À medida que as organizações se preparam para a transição pós-quântica, substituir a criptografia de curva elíptica clássica (ECC) repentinamente traz riscos significativos. A criptografia baseada em reticulados (lattices) é relativamente nova em ambientes de produção comparada a padrões matemáticos de décadas atrás. Para fazer essa transição com segurança, a comunidade de criptografia padronizou os <strong>Mecanismos de Encapsulamento de Chave Híbridos (Hybrid KEMs)</strong>. O principal padrão de produção na internet hoje é o <code>X25519MLKEM768</code>, que combina o ECDH clássico em curva X25519 com o recém-padronizado ML-KEM-768 (FIPS 203).</p>

<div class="highlight-box">
    <p><strong>Princípio de Segurança Subjacente:</strong> Um KEM híbrido combina dois mecanismos de troca de chaves independentes de modo que o segredo compartilhado resultante seja seguro desde que <em>pelo menos um</em> dos mecanismos constituintes permaneça seguro. Se uma falha sutil for descoberta no ML-KEM, o componente clássico X25519 impede a decifragem. Se um computador quântico viável for construído, o componente ML-KEM bloqueia o algoritmo de Shor.</p>
</div>

<h2>Como o X25519MLKEM768 Funciona no TLS 1.3</h2>
<p>A integração da troca de chaves híbrida no protocolo Transport Layer Security (TLS) 1.3 opera dentro da estrutura padrão de handshake, introduzindo mudanças mínimas na máquina de estados, mas alterando os dados transmitidos:</p>

<ul>
    <li><strong>Geração de Chaves no Cliente:</strong> O cliente gera um par de chaves X25519 padrão e um par de chaves ML-KEM-768. Ele concatena as duas chaves públicas em uma única chave pública híbrida.</li>
    <li><strong>Client Hello:</strong> Na extensão <code>Supported Groups</code> do <code>ClientHello</code>, o cliente lista o <code>X25519MLKEM768</code> junto com os grupos herdados (como <code>X25519</code>). Na extensão <code>KeyShare</code>, envia a fração de chave pública híbrida concatenada, além de uma fração de chave pública <code>X25519</code> autônoma como alternativa (fallback) para servidores antigos.</li>
    <li><strong>Encapsulamento e Resposta do Servidor:</strong> Se o servidor suportar o grupo híbrido, ele executa o ECDH clássico na fração X25519 para gerar um segredo compartilhado clássico ($K_1$) e executa o encapsulamento ML-KEM na fração ML-KEM-768 para gerar um texto cifrado ($c_2$) e um segredo compartilhado pós-quântico ($K_2$). Ele envia sua chave pública clássica e o texto cifrado pós-quântico no keyshare do <code>ServerHello</code>.</li>
    <li><strong>Combinador de Chaves (KDF):</strong> Ambas as partes combinam os segredos clássico e quântico usando uma Função de Derivação de Chave (KDF) segura. Para evitar ataques ativos onde um adversário substitui um texto cifrado ou chave pública, o combinador vincula os dados:
    <br><span class="code">K = HKDF-Extract(Salt, K_1 || K_2 || c_1 || c_2 || pk_1 || pk_2)</span></li>
</ul>

<h2>Aplicabilidade na Cibersegurança e Status na Indústria (2026)</h2>
<p>O principal motivador para a troca de chaves híbrida é a ameaça <strong>Harvest Now, Decrypt Later (HNDL)</strong> (Coletar Agora, Decifrar Depois). Adversários estão capturando ativamente tráfego cifrado da web hoje com a intenção de decifrá-lo no futuro assim que um Computador Quântico Relevante para Criptografia (CRQC) estiver disponível. Proteger a troca de chaves assimétrica hoje é crucial, pois qualquer dado transmitido agora é vulnerável a decifragem retrospectiva.</p>

<p>No início de 2026, a adoção do <code>X25519MLKEM768</code> já domina a infraestrutura da internet:</p>
<ul>
    <li><strong>Navegadores Web:</strong> Google Chrome (desde a versão 131 em Nov de 2024) e Mozilla Firefox (desde a versão 132) habilitam essa troca híbrida por padrão para conexões HTTPS.</li>
    <li><strong>Redes de Distribuição de Conteúdo (CDNs):</strong> Grandes CDNs como Cloudflare, Akamai e Google Edge processam uma enorme fatia do seu tráfego global TLS usando trocas de chaves híbridas, com a Cloudflare relatando que mais de 38% do tráfego HTTPS global usava PQC híbrido já no início de 2025.</li>
    <li><strong>Software Corporativo:</strong> Em fevereiro de 2026, a Oracle integrou o JEP 527 no JDK 27, ativando suporte a trocas de chaves híbridas (como <code>X25519MLKEM768</code> e <code>SecP256r1MLKEM768</code>) por padrão nos provedores JSSE do Java.</li>
</ul>

<h2>Comparação de Algoritmos e Desempenho</h2>
<table class="comparison-table">
    <thead>
        <tr>
            <th>Algoritmo / Esquema</th>
            <th>Tipo</th>
            <th>Tamanho da Chave Pública (Bytes)</th>
            <th>Tamanho do Texto Cifrado / Share (Bytes)</th>
            <th>Base de Segurança Matemática</th>
            <th>Sobrecarga de Rede (Overhead)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>X25519</strong></td>
            <td>ECDH Clássico</td>
            <td>32</td>
            <td>32</td>
            <td>Logaritmo Discreto em Curva Elíptica</td>
            <td>Extremamente Baixa (~64 bytes total)</td>
        </tr>
        <tr>
            <td><strong>ML-KEM-768</strong> (FIPS 203)</td>
            <td>KEM Pós-Quântico</td>
            <td>1.184</td>
            <td>1.088</td>
            <td>Module Learning With Errors (M-LWE)</td>
            <td>Moderada (~2,2 KB total)</td>
        </tr>
        <tr>
            <td><strong>X25519MLKEM768</strong></td>
            <td>KEM Híbrido</td>
            <td>1.216</td>
            <td>1.120</td>
            <td>M-LWE + Curvas Elípticas (ECDH)</td>
            <td>Moderada (~2,3 KB total; bem dentro do MTU)</td>
        </tr>
    </tbody>
</table>

<div class="page-break"></div>

<h2>Quiz Diário: Teste seu Conhecimento</h2>
<ol>
    <li><strong>Por que um KEM híbrido como o <code>X25519MLKEM768</code> é preferido em vez de uma implementação pura de ML-KEM-768 durante o período de migração?</strong>
        <br><em>A) Porque o ML-KEM-768 é muito lento para rodar em dispositivos móveis modernos sem aceleração por hardware.</em>
        <br><em>B) Para mitigar o risco de falhas matemáticas desconhecidas ou recém-descobertas na criptografia baseada em reticulados, enquanto ainda se defende contra futuros computadores quânticos.</em>
        <br><em>C) Porque o ML-KEM-768 não suporta encapsulamento de chave, podendo ser usado apenas para assinaturas digitais.</em>
        <br><strong>Resposta Correta: B.</strong> A abordagem híbrida garante que a segurança seja mantida se <em>qualquer um</em> dos dois componentes permanecer seguro, evitando uma falha de segurança catastrófica se ocorrer uma descoberta criptanalítica na teoria de reticulados.
    </li>
    <br>
    <li><strong>Como o cliente TLS 1.3 evita falhas de conexão ao se conectar a um servidor antigo que não suporta troca de chaves híbrida?</strong>
        <br><em>A) Ele rebaixa a conexão para HTTP em texto claro automaticamente.</em>
        <br><em>B) Enviando uma fração de chave pública X25519 clássica autônoma na extensão KeyShare do ClientHello, junto com a fração híbrida.</em>
        <br><em>C) Usando o ML-KEM-768 como um algoritmo de assinatura para assinar o handshake.</em>
        <br><strong>Resposta Correta: B.</strong> Ao incluir um keyshare X25519 clássico além do híbrido na extensão <code>KeyShare</code>, servidores legados podem simplesmente ignorar a fração híbrida e realizar um handshake ECDH padrão.
    </li>
    <br>
    <li><strong>Qual é a finalidade de incluir as chaves públicas e textos cifrados no combinador KDF de um KEM híbrido?</strong>
        <br><em>A) Aumentar o tamanho do segredo compartilhado para evitar força bruta.</em>
        <br><em>B) Garantir que a KDF seja totalmente compatível com blocos de tamanho SHA-256.</em>
        <br><em>C) Vincular o segredo derivado às chaves públicas e textos cifrados específicos, impedindo que atacantes ativos substituam componentes da troca híbrida.</em>
        <br><strong>Resposta Correta: C.</strong> Se a KDF combinasse apenas os segredos (ex: $H(K_1 || K_2)$), um atacante que quebrasse um dos esquemas poderia substituir o texto cifrado e forçar a chave final sem quebrar o outro esquema. Vincular chaves e textos cifrados na KDF previne esse ataque de substituição.
    </li>
</ol>"""

references_md = """* [TLS 1.3 Hybrid Key Exchange using X25519Kyber768 / ML-KEM](https://www.netmeister.org/blog/tls-hybrid-kex.html) (October 2024)
* [Post-Quantum Hybrid Key Exchange for TLS 1.3 - Inside.java](https://inside.java/2026/02/17/tls-post-quantum-hybrid-key-exchange) (February 2026)
* [Hybrid Key Exchange Today: Why X25519 + ML-KEM Is the Interim Default - NetGuardia](https://netguardia.com/privacy/encryption/hybrid-key-exchange-today-why-x25519-ml-kem-is-the-interim-default) (April 2026)
* [Hybrid KEM: Running X25519 and ML-KEM Together in TLS - AfterRSA](https://www.afterrsa.com/atlas/pqc/hybrid-kem) (April 2026)"""

success = update_repo(day_str, date_str, topic_en, topic_pt, file_name_prefix, category_en, category_pt, content_en, content_pt, references_md)
print("UPDATE STATUS:", success)
