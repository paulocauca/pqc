import sys
sys.path.append('/home/rycz/pqc/scripts')
from daily_updater import update_repo

day_str = "05"
date_str = "2026-07-12"
topic_en = "Post-Quantum Cryptography in Web Browsers and PKI: The 2026 Client-Side Adoption and CA Roadmap"
topic_pt = "Criptografia Pós-Quântica em Navegadores Web e PKI: A Adoção no Client-Side e o Cronograma das ACs em 2026"
file_name_prefix = "browser_pqc_pki_transition"
category_en = "Web Browser and PKI Security"
category_pt = "Segurança de Navegadores Web e PKI"

content_en = """<p>As of 2026, the transition of the web's transport layer to Post-Quantum Cryptography (PQC) presents a fascinating dichotomy. While major web browsers have achieved near-universal support for quantum-resistant key exchanges, the servers hosting the world's websites and the Public Key Infrastructure (PKI) that issues digital certificates are transitioning at a much slower pace. Understanding this gap is essential for security architects looking to secure web traffic against <strong>Harvest Now, Decrypt Later (HNDL)</strong> attacks without disrupting modern network performance.</p>

<div class="highlight-box">
    <p><strong>The 2026 Security Gap:</strong> While over 95% of active desktop and mobile web browsers now support hybrid post-quantum key exchange (typically combining classical Curve25519 with FIPS 203 ML-KEM-768), only about <strong>8.6% of the top 1 million websites</strong> have enabled server-side support. Furthermore, no publicly trusted Certificate Authorities (CAs) currently issue PQC certificates, meaning the web relies solely on hybrid <em>key exchange</em>, not hybrid <em>authentication</em>.</p>
</div>

<h2>Client-Side Readiness: Browsers Leading the Charge</h2>
<p>The client side of the web is fully prepared for the post-quantum era. Since mid-2024, all major browser engines have shipped hybrid key exchange protocols enabled by default. This deployment ensures that a significant portion of global internet traffic is already protected against future decryption by quantum computers:</p>

<ul>
    <li><strong>Universal Support:</strong> Chrome (124+), Firefox (128+), Safari (18+), and Edge (124+) natively support the hybrid mechanism <code>X25519Kyber768</code> (now updated to align with the FIPS 203 ML-KEM standard).</li>
    <li><strong>The Hybrid Philosophy:</strong> Browsers negotiate connections by combining a classical Elliptic Curve Diffie-Hellman exchange (X25519) with ML-KEM. If either algorithm is compromised, the connection remains secure. This mitigates the risk of early implementation flaws in the newer lattice-based schemes.</li>
    <li><strong>Symmetric Shielding:</strong> By securing the key exchange today, browsers ensure that recorded TLS session traffic cannot be decrypted retroactively, neutralizing the primary objective of state-sponsored HNDL campaigns.</li>
</ul>

<h2>The Server Lag: Why Web Infrastructure is Behind</h2>
<p>Despite browser readiness, server-side implementation remains deeply uneven. While tech giants and major Content Delivery Networks (CDNs) like Cloudflare, Google, and Meta have enabled hybrid key exchanges across their edges—covering roughly 40% of the top 100 websites—smaller organizations and internal enterprise servers are lagging significantly:</p>

<ul>
    <li><strong>Web Server Configuration:</strong> Activating hybrid key exchanges requires updating server software (e.g., NGINX, Apache, IIS) and cryptographic libraries (such as OpenSSL 3.x or BoringSSL). Many legacy servers run outdated versions that lack native support.</li>
    <li><strong>Middlebox and Firewall Interference:</strong> Some enterprise firewalls, intrusion detection systems, and deep packet inspection (DPI) appliances crash or drop connections when they encounter the larger client-hello and key-exchange payloads associated with PQC algorithms.</li>
    <li><strong>Hardware Offloading:</strong> Many high-performance web servers offload TLS decryption to dedicated Hardware Security Modules (HSMs) or application delivery controllers. Upgrading these devices to support FIPS 203 (ML-KEM) requires firmware updates or complete hardware replacements, slowing corporate adoption.</li>
</ul>

<h2>Public Key Infrastructure (PKI) & The CA Roadmap</h2>
<p>While hybrid key exchange secures the confidentiality of the session keys, it does not secure the authenticity of the website. Current web certificates still rely entirely on classical signatures (RSA or ECDSA). The transition of Public Key Infrastructure (PKI) to post-quantum signatures (such as FIPS 204 ML-DSA) introduces significant technical hurdles:</p>

<ul>
    <li><strong>Signature Size Overhead:</strong> Classical ECDSA signatures are around 64 bytes. In contrast, an ML-DSA-65 (FIPS 204) signature is roughly 2,400 bytes, while its public key is 1,300 bytes. This substantial increase in data size can cause TLS handshakes to exceed the standard TCP Maximum Transmission Unit (MTU) of 1,500 bytes, leading to packet fragmentation and increased connection latencies.</li>
    <li><strong>CA Adoption Timeline:</strong> As of mid-2026, no publicly trusted CA issues PQC certificates. The industry roadmap projects the first test/pilot PQC certificates to appear in late 2026, with initial publicly trusted hybrid certificates launching in 2027, and broader commercial availability not expected until 2028–2030.</li>
    <li><strong>Certificate Stacking:</strong> Until client support is universal, servers will need to support dual-certificate stacking (offering ECDSA certificates to older clients and ML-DSA/hybrid certificates to modern browsers), adding operational complexity to web servers.</li>
</ul>

<h2>Comparing the Transition States of Web Security</h2>
<p>This table summarizes the 2026 progress, cryptographic components, and technical challenges across the key layers of web security:</p>

<table class="comparison-table">
    <thead>
        <tr>
            <th>Security Layer</th>
            <th>Classical Baseline</th>
            <th>Current Hybrid State (2026)</th>
            <th>Full Post-Quantum Target</th>
            <th>Primary Bottleneck / Challenge</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Key Exchange (Confidentiality)</strong></td>
            <td>ECDH (X25519) / DH</td>
            <td><strong>X25519 + ML-KEM-768</strong><br>• Chrome/Firefox: ~95% default<br>• Servers: 8.6% of top 1M</td>
            <td>Pure ML-KEM (FIPS 203)</td>
            <td>Updating legacy enterprise web servers and proxy infrastructure.</td>
        </tr>
        <tr>
            <td><strong>Authentication (Certificates)</strong></td>
            <td>RSA (2048/4096) or ECDSA</td>
            <td><strong>Classical Only (ECDSA/RSA)</strong><br>• No public PQC certs exist yet<br>• Drafts for hybrid certificates</td>
            <td>ML-DSA (FIPS 204) or SLH-DSA (FIPS 205)</td>
            <td>Signature sizes leading to TCP fragmentation and handshake bloat.</td>
        </tr>
        <tr>
            <td><strong>Root Certificates (Trust Anchors)</strong></td>
            <td>Built-in CA Roots (SHA-256)</td>
            <td><strong>Classical Roots</strong><br>• Browsers trust standard PKI<br>• PQC CA roots in testing</td>
            <td>PQC-signed Root CA Store</td>
            <td>Strict compliance audits and long-term OS/browser trust store rollouts.</td>
        </tr>
    </tbody>
</table>

<div class="page-break"></div>

<h2>Daily Quiz: Test Your Understanding</h2>
<ol>
    <li><strong>Why have major web browsers prioritized hybrid key exchange (X25519 + ML-KEM) over waiting for full post-quantum certificates?</strong>
        <br><em>A) Because hybrid key exchange immediately protects traffic against "Harvest Now, Decrypt Later" retrospective decryption attacks.</em>
        <br><em>B) Because web browsers cannot process digital signatures without specialized quantum coprocessors.</em>
        <br><em>C) Because ML-KEM has smaller key sizes than ECDH, which speeds up initial connection times.</em>
        <br><strong>Correct Answer: A.</strong> Securing the key exchange today ensures that even if an attacker intercepts and records traffic now, they cannot decrypt it in the future with a quantum computer, which is the immediate threat.
    </li>
    <br>
    <li><strong>Which of the following represents the biggest operational hurdle when transitioning SSL/TLS certificates to post-quantum signatures like ML-DSA (FIPS 204)?</strong>
        <br><em>A) The high mathematical complexity makes client-side signature verification take several seconds.</em>
        <br><em>B) The large signature and public key sizes (~3.7 KB combined) exceed the standard 1.5 KB TCP MTU, causing packet fragmentation.</em>
        <br><em>C) ML-DSA is heavily patented and requires expensive runtime licensing fees for each website.</em>
        <br><strong>Correct Answer: B.</strong> The massive size of post-quantum keys and signatures compared to classical ECDSA leads to packet fragmentation across TCP connections, which can degrade handshake performance and trigger firewall drops.
    </li>
    <br>
    <li><strong>What is the estimated deployment rate of hybrid PQC key exchange on the top 1 million websites as of mid-2026?</strong>
        <br><em>A) Under 1%, because no browser has enabled support.</em>
        <br><em>B) Roughly 8.6%, indicating a major lag between universal client support and actual server-side enablement.</em>
        <br><em>C) Exactly 100%, because all cloud hosting providers forced the upgrade in 2025.</em>
        <br><strong>Correct Answer: B.</strong> While major browsers (Chrome, Firefox, Safari) support PQC by default, server adoption lags behind significantly at around 8.6% of the top 1 million websites, demonstrating a substantial upgrade gap for standard enterprise hosts.
    </li>
</ol>"""

content_pt = """<p>Em 2026, a transição da camada de transporte da web para a Criptografia Pós-Quântica (PQC) apresenta uma dicotomia fascinante. Enquanto os principais navegadores web alcançaram suporte quase universal para trocas de chaves resistentes a computadores quânticos, os servidores que hospedam os sites e a Infraestrutura de Chaves Públicas (PKI) que emite certificados digitais estão se adaptando em um ritmo muito mais lento. Compreender essa lacuna é essencial para arquitetos de segurança que buscam proteger o tráfego web contra ataques de <strong>Harvest Now, Decrypt Later (HNDL)</strong> (Coletar Agora, Decifrar Depois) sem comprometer o desempenho da rede moderna.</p>

<div class="highlight-box">
    <p><strong>A Lacuna de Segurança em 2026:</strong> Embora mais de 95% dos navegadores ativos (desktop e mobile) já suportem a troca de chaves híbrida pós-quântica (combinando a Curve25519 clássica com o FIPS 203 ML-KEM-768), apenas cerca de <strong>8,6% dos 1 milhão de sites mais acessados</strong> habilitaram esse suporte em seus servidores. Além disso, nenhuma Autoridade Certificadora (AC) publicamente confiável emite certificados PQC ainda, o que significa que a web hoje depende exclusivamente de <em>troca de chaves</em> híbrida, e não de <em>autenticação</em> híbrida.</p>
</div>

<h2>Prontidão no Client-Side: Navegadores Liderando a Transição</h2>
<p>O lado do cliente está totalmente preparado para a era pós-quântica. Desde meados de 2024, todos os principais motores de navegadores vêm distribuindo protocolos de troca de chaves híbridos habilitados por padrão. Essa implantação em massa garante que uma parte significativa do tráfego global da internet já esteja protegida contra futura decodificação por computadores quânticos:</p>

<ul>
    <li><strong>Suporte Universal:</strong> Chrome (124+), Firefox (128+), Safari (18+) e Edge (124+) oferecem suporte nativo ao mecanismo híbrido <code>X25519Kyber768</code> (atualizado em conformidade com o padrão FIPS 203 ML-KEM).</li>
    <li><strong>A Filosofia Híbrida:</strong> Os navegadores negociam conexões combinando uma troca clássica Diffie-Hellman por Curvas Elípticas (X25519) com o ML-KEM. Se qualquer um dos algoritmos for comprometido, a conexão continua segura. Isso mitiga riscos associados a eventuais falhas de implementação iniciais nos novos esquemas baseados em reticulados.</li>
    <li><strong>Escudo contra Retroatividade:</strong> Ao proteger a troca de chaves hoje, os navegadores garantem que o tráfego TLS interceptado e gravado no presente não possa ser decifrado retrospectivamente, neutralizando o principal objetivo das campanhas estatais de HNDL.</li>
</ul>

<h2>O Atraso nos Servidores: Por que a Infraestrutura está Atrás?</h2>
<p>Apesar da prontidão dos navegadores, a implementação nos servidores é bastante desigual. Embora gigantes de tecnologia e grandes Redes de Distribuição de Conteúdo (CDNs) como Cloudflare, Google e Meta tenham habilitado trocas de chaves híbridas em suas bordas — cobrindo cerca de 40% dos 100 principais sites —, organizações de menor porte e servidores corporativos internos estão muito atrasados:</p>

<ul>
    <li><strong>Configuração de Servidores Web:</strong> Ativar trocas de chaves híbridas exige a atualização dos softwares de servidor (como NGINX, Apache, IIS) e de bibliotecas criptográficas (como OpenSSL 3.x ou BoringSSL). Muitos servidores legados rodam versões antigas que carecem de suporte nativo.</li>
    <li><strong>Interferência de Middleboxes e Firewalls:</strong> Alguns firewalls corporativos, sistemas de detecção de intrusão (IDS) e dispositivos de inspeção profunda de pacotes (DPI) travam ou rejeitam conexões ao encontrar os pacotes maiores de Client-Hello e troca de chaves exigidos pelos algoritmos PQC.</li>
    <li><strong>Aceleração por Hardware (Offloading):</strong> Muitos servidores web de alto desempenho delegam a descriptografia TLS a Módulos de Segurança de Hardware (HSMs) dedicados. Atualizar esses dispositivos para suportar o FIPS 203 (ML-KEM) requer atualizações de firmware complexas ou a substituição completa do hardware, desacelerando a adoção corporativa.</li>
</ul>

<h2>Infraestrutura de Chaves Públicas (PKI) e o Cronograma das ACs</h2>
<p>Embora a troca de chaves híbrida garanta a confidencialidade das chaves de sessão, ela não garante a autenticidade do site. Os certificados web atuais ainda dependem inteiramente de assinaturas clássicas (RSA ou ECDSA). A transição da PKI para assinaturas pós-quânticas (como o FIPS 204 ML-DSA) introduz desafios técnicos complexos:</p>

<ul>
    <li><strong>Impacto do Tamanho das Assinaturas:</strong> Assinaturas ECDSA clássicas ocupam cerca de 64 bytes. Em contrapartida, uma assinatura ML-DSA-65 (FIPS 204) exige cerca de 2.400 bytes, enquanto sua chave pública ocupa 1.300 bytes. Esse aumento expressivo faz com que os handshakes TLS excedam a Unidade Máxima de Transmissão (MTU) padrão do TCP de 1.500 bytes, provocando fragmentação de pacotes e aumentando a latência da conexão.</li>
    <li><strong>Cronograma de Adoção das ACs:</strong> Até o momento em 2026, nenhuma AC publicamente confiável emite certificados PQC comerciais. O cronograma da indústria prevê os primeiros certificados de teste/piloto para o final de 2026, com os primeiros certificados híbridos de confiança pública em 2027, e ampla disponibilidade comercial apenas entre 2028 e 2030.</li>
    <li><strong>Empilhamento de Certificados (Stacking):</strong> Até que o suporte do cliente seja universal, os servidores precisarão suportar o empilhamento de dois certificados (oferecendo certificados ECDSA para clientes antigos e ML-DSA/híbridos para navegadores modernos), adicionando complexidade operacional à gestão web.</li>
</ul>

<h2>Comparando o Estado de Transição da Segurança Web</h2>
<p>Esta tabela resume o progresso em 2026, os componentes criptográficos e os desafios técnicos em cada camada crítica da segurança web:</p>

<table class="comparison-table">
    <thead>
        <tr>
            <th>Camada de Segurança</th>
            <th>Linha de Base Clássica</th>
            <th>Estado Híbrido Atual (2026)</th>
            <th>Alvo Pós-Quântico Puro</th>
            <th>Principal Gargalo / Desafio</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Troca de Chaves (Confidencialidade)</strong></td>
            <td>ECDH (X25519) / DH</td>
            <td><strong>X25519 + ML-KEM-768</strong><br>• Navegadores: ~95% padrão<br>• Servidores: ~8,6% do top 1M</td>
            <td>ML-KEM Puro (FIPS 203)</td>
            <td>Atualização de servidores corporativos legados e proxies reversos.</td>
        </tr>
        <tr>
            <td><strong>Autenticação (Certificados)</strong></td>
            <td>RSA (2048/4096) ou ECDSA</td>
            <td><strong>Apenas Clássica (ECDSA/RSA)</strong><br>• Sem certificados PQC públicos<br>• Rascunhos para certificados híbridos</td>
            <td>ML-DSA (FIPS 204) ou SLH-DSA (FIPS 205)</td>
            <td>Tamanho das assinaturas gerando fragmentação de pacotes TCP e handshakes inflados.</td>
        </tr>
        <tr>
            <td><strong>Certificados Raiz (Âncoras de Confiança)</strong></td>
            <td>Raízes de AC embutidas (SHA-256)</td>
            <td><strong>Raízes Clássicas</strong><br>• Navegadores confiam na PKI padrão<br>• ACs testando raízes PQC</td>
            <td>Repositório de AC Raiz Assinado por PQC</td>
            <td>Auditorias rígidas de conformidade e rollouts lentos nos repositórios de S.O./navegadores.</td>
        </tr>
    </tbody>
</table>

<div class="page-break"></div>

<h2>Quiz Diário: Teste seu Conhecimento</h2>
<ol>
    <li><strong>Por que os principais navegadores web priorizaram a troca de chaves híbrida (X25519 + ML-KEM) antes mesmo de termos certificados pós-quânticos?</strong>
        <br><em>A) Porque a troca de chaves híbrida protege imediatamente o tráfego contra ataques de decifragem retrospectiva "Harvest Now, Decrypt Later".</em>
        <br><em>B) Porque os navegadores web são incapazes de processar assinaturas digitais sem coprocessadores quânticos dedicados.</em>
        <br><em>C) Porque o ML-KEM possui tamanhos de chave menores que o ECDH, agilizando a conexão inicial.</em>
        <br><strong>Resposta Correta: A.</strong> Proteger a troca de chaves hoje garante que mesmo que um invasor intercepte e grave o tráfego cifrado agora, ele não conseguirá decifrá-lo no futuro com um computador quântico, neutralizando a ameaça retrospectiva imediata.
    </li>
    <br>
    <li><strong>Qual é o maior obstáculo operacional ao migrar certificados SSL/TLS para assinaturas pós-quânticas como o ML-DSA (FIPS 204)?</strong>
        <br><em>A) A alta complexidade matemática faz com que a verificação de assinatura no navegador demore vários segundos.</em>
        <br><em>B) Os grandes tamanhos de assinatura e chaves públicas (~3.7 KB combinados) excedem a MTU TCP padrão de 1.5 KB, gerando fragmentação de pacotes.</em>
        <br><em>C) O ML-DSA é altamente patenteado e exige taxas caras de licenciamento para cada servidor web.</em>
        <br><strong>Resposta Correta: B.</strong> O tamanho expressivo das chaves e assinaturas pós-quânticas em comparação com as elípticas clássicas (ECDSA) causa fragmentação de pacotes TCP nas conexões, o que pode degradar o desempenho do handshake e fazer com que firewalls descartem pacotes.
    </li>
    <br>
    <li><strong>Qual é a taxa estimada de adoção da troca de chaves PQC híbrida nos 1 milhão de sites mais acessados em meados de 2026?</strong>
        <br><em>A) Menor que 1%, pois nenhum navegador ativou o suporte ainda.</em>
        <br><em>B) Aproximadamente 8,6%, indicando uma lacuna significativa entre o suporte universal do cliente e a ativação real no lado do servidor.</em>
        <br><em>C) Exatamente 100%, porque todos os provedores de nuvem forçaram a atualização em 2025.</em>
        <br><strong>Resposta Correta: B.</strong> Enquanto os navegadores dominantes (Chrome, Firefox, Safari) suportam PQC por padrão, a adoção em servidores comuns está muito atrás (cerca de 8,6%), demonstrando que hosts corporativos tradicionais ainda precisam habilitar a tecnologia.
    </li>
</ol>"""

references_md = """* [Post-Quantum Cryptography in 2026: Where Browsers, CAs, and Enterprises Actually Stand - TigerTrust](https://www.tigertrust.io/blog/post-quantum-cryptography-2026-status) (Marcus Webb, March 2026)
* [Quantum-Secure Internet: Post-Quantum Cryptography, National Rollouts, and the Future of Digital Trust - RI Study Post](https://www.ristudypost.com/2026/01/quantum-secure-internet-post-quantum.html) (January 2026)
* [Post-Quantum Cryptography in 2026 - PQC Standards, Lattice-Based Encryption, and Quantum-Safe Security - Internet Pros](https://internet-pros.com/blog/post-quantum-cryptography-pqc-2026/) (2026)"""

success = update_repo(day_str, date_str, topic_en, topic_pt, file_name_prefix, category_en, category_pt, content_en, content_pt, references_md)
print("UPDATE STATUS:", success)
