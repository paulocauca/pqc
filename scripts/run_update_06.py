import sys
sys.path.append('/home/rycz/pqc/scripts')
from daily_updater import update_repo

day_str = "06"
date_str = "2026-07-13"
topic_en = "Post-Quantum Code Signing and Software Updates: Securing the Software Supply Chain with ML-DSA and SLH-DSA"
topic_pt = "Assinatura de Código e Atualizações de Software Pós-Quânticas: Protegendo a Cadeia de Suprimentos de Software com ML-DSA e SLH-DSA"
file_name_prefix = "code_signing_pqc_transition"
category_en = "Software Supply Chain and Firmware Security"
category_pt = "Cadeia de Suprimentos de Software e Segurança de Firmware"

content_en = """<p>As the quantum computing era approaches, the software supply chain has emerged as one of the most critical targets for cyber adversaries. At the heart of software security lies the digital signature, which ensures that operating system updates, application installations, and hardware firmware originate from trusted sources and have not been altered. While securing active internet traffic with hybrid key exchanges (such as X25519 + ML-KEM) is already widespread in browsers and SSH, transitioning the <strong>software distribution and firmware signature</strong> ecosystem to Post-Quantum Cryptography (PQC) presents unique challenges, particularly regarding signature longevity, verification speeds, and hardware storage constraints.</p>

<div class="highlight-box">
    <p><strong>The Long-Term Integrity Problem:</strong> For typical web browsing, cryptographic keys are ephemeral and live for milliseconds. However, code signatures and firmware updates are designed to endure. If a medical device, an industrial PLC, or a vehicle's engine control unit is deployed in 2026 with a 15-year operational lifespan, its update verification keys must remain secure until 2041. A quantum computing breakthrough that compromises classical signing keys (RSA or ECDSA) retroactively invalidates the integrity of all past, present, and future updates, allowing attackers to inject malicious firmware without triggering bootloader warnings.</p>
</div>

<h2>The Two Pillars of Post-Quantum Signatures: ML-DSA vs. SLH-DSA</h2>
<p>To secure digital signatures against quantum threats, NIST has standardized two primary digital signature algorithms: <strong>ML-DSA</strong> (FIPS 204, based on module lattices) and <strong>SLH-DSA</strong> (FIPS 205, based on stateless hash structures). Each algorithm possesses distinct characteristics that dictate its applicability within the software supply chain:</p>

<ul>
    <li><strong>ML-DSA (FIPS 204):</strong> Based on the hardness of Module Learning With Errors (MLWE). It represents a general-purpose signature scheme. It features rapid signing, extremely fast verification speeds, and relatively compact public keys (~1.9 KB for ML-DSA-65) and signatures (~3.3 KB). It is the ideal candidate for high-frequency, large-scale general software distribution (e.g., operating system package managers like APT, secure code-signing certificates, and app store updates).</li>
    <li><strong>SLH-DSA (FIPS 205):</strong> Based strictly on stateless hash structures (SPHINCS+). It relies entirely on the collision resistance of underlying cryptographic hash functions (such as SHA-2 or SHAKE/SHA-3). Because SLH-DSA makes absolutely no structural algebraic assumptions, it is immune to future mathematical cryptanalysis that might theoretically compromise lattice-based schemes. However, it requires significantly longer signing times and produces large signatures (from ~7.8 KB to ~49 KB). Despite this overhead, its public key size is miniscule (~32 bytes), making it the gold standard for high-security applications, root certificate trust stores, and immutable hardware bootloaders.</li>
</ul>

<h2>Real-World Applicability in Secure Boot and OTA Updates</h2>
<p>In practice, integrating post-quantum signatures into internet protocols and devices requires navigating strict physical and networking constraints:</p>

<h3>1. Hardware Root of Trust and Secure Boot</h3>
<p>During the device boot process, the secure bootloader verifies the initial firmware using a public key permanently burned into the chip's Read-Only Memory (ROM) or One-Time Programmable (OTP) fuses. This environment is highly resource-constrained. Storing a 2 KB ML-DSA public key in hardware registers is often impossible. Conversely, <strong>SLH-DSA's 32-byte public key</strong> fits easily into standard hardware fuses. Even though verifying an SLH-DSA signature requires more CPU cycles, the boot process happens infrequently, making the tiny public key size the deciding factor for hardware manufacturers.</p>

<h3>2. Over-the-Air (OTA) Updates in IoT and Embedded Systems</h3>
<p>IoT and embedded systems deployed across remote industrial networks (e.g., smart grids, telemetry sensors) often rely on low-bandwidth protocols like cellular, satellite, or LPWAN. Transporting a 17 KB SLH-DSA signature for a minor 50 KB configuration update represents a massive overhead that drains device battery and consumes network bandwidth. In these scenarios, developers are turning to <strong>ML-DSA-44 or ML-DSA-65</strong>, which offer a balanced trade-off between signature size and computational overhead, or deploying <strong>hybrid signatures</strong> that combine classical ECDSA with ML-DSA to ensure backward compatibility and quantum resistance.</p>

<h3>3. Operating System Package Signing</h3>
<p>Linux distributions and enterprise software vendors must sign millions of individual packages. Signing speed is critical for continuous integration and delivery (CI/CD) pipelines. While SLH-DSA can take hundreds of milliseconds to generate a single signature, ML-DSA can sign in less than a millisecond, making ML-DSA the only viable option for high-volume, automated software release cycles.</p>

<h2>Comparing Signature Schemes for the Software Supply Chain</h2>
<p>This table compares classical signature algorithms with the new post-quantum standards under FIPS 204 and FIPS 205, highlighting their technical trade-offs:</p>

<table class="comparison-table">
    <thead>
        <tr>
            <th>Algorithm Name</th>
            <th>Type / Class</th>
            <th>Public Key Size</th>
            <th>Signature Size</th>
            <th>Signing Speed</th>
            <th>Verification Speed</th>
            <th>Best Suited For</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>ECDSA (P-256)</strong></td>
            <td>Classical (Elliptic Curve)</td>
            <td>~64 Bytes</td>
            <td>~64 Bytes</td>
            <td>Very Fast</td>
            <td>Fast</td>
            <td>No longer recommended (broken by Shor's Algorithm)</td>
        </tr>
        <tr>
            <td><strong>RSA-3072</strong></td>
            <td>Classical (Integer Factoring)</td>
            <td>~384 Bytes</td>
            <td>~384 Bytes</td>
            <td>Slow</td>
            <td>Very Fast</td>
            <td>No longer recommended (broken by Shor's Algorithm)</td>
        </tr>
        <tr>
            <td><strong>ML-DSA-65 (FIPS 204)</strong></td>
            <td>Post-Quantum (Module Lattice)</td>
            <td>1,952 Bytes</td>
            <td>3,293 Bytes</td>
            <td>Very Fast</td>
            <td>Very Fast</td>
            <td>General software signing, OS packages, app stores, CI/CD pipelines.</td>
        </tr>
        <tr>
            <td><strong>SLH-DSA-SHA2-128s (FIPS 205)</strong></td>
            <td>Post-Quantum (Stateless Hash)</td>
            <td>32 Bytes</td>
            <td>7,856 Bytes</td>
            <td>Very Slow</td>
            <td>Moderate</td>
            <td>High-security firmware updates, ROM secure boot keys, Root CAs.</td>
        </tr>
        <tr>
            <td><strong>SLH-DSA-SHA2-128f (FIPS 205)</strong></td>
            <td>Post-Quantum (Stateless Hash)</td>
            <td>32 Bytes</td>
            <td>17,088 Bytes</td>
            <td>Moderate</td>
            <td>Fast</td>
            <td>Applications requiring faster verification where signature size is secondary.</td>
        </tr>
    </tbody>
</table>

<div class="page-break"></div>

<h2>Daily Quiz: Test Your Understanding</h2>
<ol>
    <li><strong>Why is SLH-DSA (FIPS 205) considered structurally safer than ML-DSA (FIPS 204) for long-term code signing root anchors, despite having larger signatures and slower signing speeds?</strong>
        <br><em>A) Because SLH-DSA is stateful and requires tracking signature indexes, which prevents key replay attacks.</em>
        <br><em>B) Because SLH-DSA is a stateless hash-based scheme relying only on secure hash functions, with zero structured algebraic (lattice) assumptions that could be compromised by future mathematical breakthroughs.</em>
        <br><em>C) Because SLH-DSA is faster to sign on constrained microcontroller hardware.</em>
        <br><strong>Correct Answer: B.</strong> Since SLH-DSA depends solely on the collision resistance of standard hash functions (like SHA-2 or SHA-3), it does not rely on the complexity of lattice problems. It is mathematically simpler and less vulnerable to future algebraic cryptanalysis breakthroughs.
    </li>
    <br>
    <li><strong>Which characteristic of SLH-DSA makes it highly attractive for hardware secure boot ROM and OTP (One-Time Programmable) storage?</strong>
        <br><em>A) Its massive signature size, which fills up the storage to prevent buffer overflows.</em>
        <br><em>B) Its very fast signing speed, which accelerates factory programming lines.</em>
        <br><em>C) Its exceptionally tiny public key size of just 32 bytes, which easily fits in limited chip fuse registers.</em>
        <br><strong>Correct Answer: C.</strong> High-security chips have extremely limited ROM/OTP space to store the trust anchor (public key). SLH-DSA's public key is only 32 bytes (equal to or smaller than classical ECC/RSA keys), making it incredibly easy to store in physical hardware fuses.
    </li>
    <br>
    <li><strong>A software developer is setting up an automated CI/CD pipeline that signs thousands of compiled microservices and packages per hour. Which PQC signature should they select?</strong>
        <br><em>A) SLH-DSA-SHA2-128s, to minimize the public key size in their database.</em>
        <br><em>B) ML-DSA-65, because its sub-millisecond signing and verification speeds prevent pipeline bottlenecks while maintaining quantum resistance.</em>
        <br><em>C) Stateful XMSS (RFC 8391), because the continuous pipeline is perfect for tracking states across parallel server instances.</em>
        <br><strong>Correct Answer: B.</strong> Automated, high-frequency software build pipelines require fast signing speeds. ML-DSA provides rapid signing and verification with reasonable signature sizes, making it the practical choice for automated general-purpose software delivery.
    </li>
</ol>"""

content_pt = """<p>À medida que a era da computação quântica se aproxima, a cadeia de suprimentos de software (software supply chain) tornou-se um dos alvos mais críticos para adversários cibernéticos. No coração da segurança de software está a assinatura digital, que garante que as atualizações do sistema operacional, instalações de aplicativos e firmware de hardware venham de fontes confiáveis e não tenham sido alteradas. Embora a proteção do tráfego de internet ativo com trocas de chaves híbridas (como X25519 + ML-KEM) já esteja amplamente difundida em navegadores e SSH, a transição do ecossistema de <strong>distribuição de software e assinaturas de firmware</strong> para a Criptografia Pós-Quântica (PQC) apresenta desafios únicos, particularmente em relação à longevidade da assinatura, velocidades de verificação e restrições de armazenamento em hardware.</p>

<div class="highlight-box">
    <p><strong>O Problema da Integridade de Longo Prazo:</strong> Para a navegação web típica, as chaves criptográficas são efêmeras e vivem por milissegundos. No entanto, assinaturas de código e atualizações de firmware são feitas para durar. Se um dispositivo médico, um CLP industrial ou a unidade de controle do motor de um veículo for implantado em 2026 com uma vida útil operacional de 15 anos, suas chaves de verificação de atualização devem permanecer seguras até 2041. Um avanço na computação quântica que comprometa as chaves de assinatura clássicas (RSA ou ECDSA) invalida retroativamente a integridade de todas as atualizações passadas, presentes e futuras, permitindo que atacantes injetem firmware malicioso sem disparar alertas no bootloader.</p>
</div>

<h2>Os Dois Pilares das Assinaturas Pós-Quânticas: ML-DSA vs. SLH-DSA</h2>
<p>Para proteger as assinaturas digitais contra ameaças quânticas, o NIST padronizou dois algoritmos principais de assinatura digital: <strong>ML-DSA</strong> (FIPS 204, baseado em reticulados modulares) e <strong>SLH-DSA</strong> (FIPS 205, baseado em estruturas de hash sem estado - stateless). Cada algoritmo possui características distintas que ditam sua aplicabilidade na cadeia de suprimentos de software:</p>

<ul>
    <li><strong>ML-DSA (FIPS 204):</strong> Baseado na dificuldade do problema Module Learning With Errors (MLWE). É um esquema de assinatura de uso geral. Destaca-se por assinaturas rápidas, velocidades de verificação extremamente rápidas e chaves públicas (~1,9 KB para ML-DSA-65) e assinaturas (~3,3 KB) relativamente compactas. É o candidato ideal para distribuição de software geral em alta frequência e larga escala (por exemplo, gerenciadores de pacotes de sistemas operacionais como APT, certificados de assinatura de código seguros e atualizações de lojas de aplicativos).</li>
    <li><strong>SLH-DSA (FIPS 205):</strong> Baseado estritamente em estruturas de hash sem estado (SPHINCS+). Depende inteiramente da resistência à colisão das funções de hash criptográficas subjacentes (como SHA-2 ou SHAKE/SHA-3). Como o SLH-DSA não faz nenhuma suposição algébrica estrutural, ele é imune a futuras criptoanálises matemáticas que poderiam teoricamente comprometer esquemas baseados em reticulados. No entanto, exige tempos de assinatura significativamente mais longos e gera assinaturas grandes (de ~7,8 KB a ~49 KB). Apesar desse impacto, o tamanho de sua chave pública é minúsculo (~32 bytes), tornando-o o padrão-ouro para aplicações de alta segurança, repositórios de certificados raiz e bootloaders de hardware imutáveis.</li>
</ul>

<h2>Aplicabilidade no Mundo Real em Secure Boot e Atualizações OTA</h2>
<p>Na prática, a integração de assinaturas pós-quânticas em protocolos de internet e dispositivos requer navegar por restrições físicas e de rede severas:</p>

<h3>1. Raiz de Confiança em Hardware e Secure Boot</h3>
<p>Durante o processo de inicialização de um dispositivo, o bootloader seguro verifica o firmware inicial usando uma chave pública gravada permanentemente na memória somente leitura (ROM) do chip ou em fusíveis programáveis uma única vez (OTP). Este ambiente é altamente restrito em termos de recursos. Armazenar uma chave pública ML-DSA de 2 KB em registradores de hardware costuma ser impossível. Em contrapartida, a <strong>chave pública de 32 bytes do SLH-DSA</strong> cabe facilmente em fusíveis de hardware padrão. Mesmo que a verificação de uma assinatura SLH-DSA exija mais ciclos de CPU, o processo de inicialização ocorre com pouca frequência, tornando o tamanho minúsculo da chave pública o fator decisivo para os fabricantes de hardware.</p>

<h3>2. Atualizações Over-the-Air (OTA) em IoT e Sistemas Embarcados</h3>
<p>Dispositivos IoT e sistemas embarcados implantados em redes industriais remotas (como redes elétricas inteligentes, sensores de telemetria) geralmente dependem de produtos de baixa largura de banda, como redes celulares, satélite ou LPWAN. Transportar uma assinatura SLH-DSA de 17 KB para uma pequena atualização de configuração de 50 KB representa um consumo massivo que esgota a bateria do dispositivo e consome dados de rede. Nesses cenários, os desenvolvedores estão recorrendo ao <strong>ML-DSA-44 ou ML-DSA-65</strong>, que oferecem um equilíbrio ideal entre tamanho de assinatura e processamento computacional, ou implantando <strong>assinaturas híbridas</strong> que combinam ECDSA clássico com ML-DSA para garantir compatibilidade reversa e resistência quântica.</p>

<h3>3. Assinatura de Pacotes de Sistemas Operacionais</h3>
<p>Distribuições Linux e fornecedores de software empresarial devem assinar milhões de pacotes individuais. A velocidade de assinatura é crítica para pipelines de integração e entrega contínua (CI/CD). Enquanto o SLH-DSA pode levar centenas de milissegundos para gerar uma única assinatura, o ML-DSA pode assinar em menos de um milissegundo, tornando o ML-DSA a única opção viável para ciclos de lançamento de software automatizados e de alto volume.</p>

<h2>Comparando Esquemas de Assinatura para a Cadeia de Suprimentos de Software</h2>
<p>Esta tabela compara os algoritmos de assinatura clássicos com os novos padrões pós-quânticos sob o FIPS 204 e FIPS 205, destacando seus trade-offs técnicos:</p>

<table class="comparison-table">
    <thead>
        <tr>
            <th>Nome do Algoritmo</th>
            <th>Tipo / Classe</th>
            <th>Tamanho da Chave Pública</th>
            <th>Tamanho da Assinatura</th>
            <th>Velocidade de Assinatura</th>
            <th>Velocidade de Verificação</th>
            <th>Melhor Adequado Para</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>ECDSA (P-256)</strong></td>
            <td>Clássico (Curva Elíptica)</td>
            <td>~64 Bytes</td>
            <td>~64 Bytes</td>
            <td>Muito Rápida</td>
            <td>Rápida</td>
            <td>Não recomendado (quebrado pelo Algoritmo de Shor)</td>
        </tr>
        <tr>
            <td><strong>RSA-3072</strong></td>
            <td>Clássico (Fatoração de Inteiros)</td>
            <td>~384 Bytes</td>
            <td>~384 Bytes</td>
            <td>Lenta</td>
            <td>Muito Rápida</td>
            <td>Não recomendado (quebrado pelo Algoritmo de Shor)</td>
        </tr>
        <tr>
            <td><strong>ML-DSA-65 (FIPS 204)</strong></td>
            <td>Pós-Quântico (Reticulados Modulares)</td>
            <td>1.952 Bytes</td>
            <td>3.293 Bytes</td>
            <td>Muito Rápida</td>
            <td>Muito Rápida</td>
            <td>Assinatura de software geral, pacotes de S.O., lojas de apps, pipelines de CI/CD.</td>
        </tr>
        <tr>
            <td><strong>SLH-DSA-SHA2-128s (FIPS 205)</strong></td>
            <td>Pós-Quântico (Hash sem Estado)</td>
            <td>32 Bytes</td>
            <td>7.856 Bytes</td>
            <td>Muito Lenta</td>
            <td>Moderada</td>
            <td>Atualizações de firmware de alta segurança, chaves ROM de Secure Boot, ACs Raiz.</td>
        </tr>
        <tr>
            <td><strong>SLH-DSA-SHA2-128f (FIPS 205)</strong></td>
            <td>Pós-Quântico (Hash sem Estado)</td>
            <td>32 Bytes</td>
            <td>17.088 Bytes</td>
            <td>Moderada</td>
            <td>Rápida</td>
            <td>Aplicações que exigem verificação mais rápida, onde o tamanho da assinatura é secundário.</td>
        </tr>
    </tbody>
</table>

<div class="page-break"></div>

<h2>Quiz Diário: Teste seu Conhecimento</h2>
<ol>
    <li><strong>Por que o SLH-DSA (FIPS 205) é considerado estruturalmente mais seguro do que o ML-DSA (FIPS 204) para âncoras de confiança de assinatura de código de longo prazo, apesar de possuir assinaturas maiores e velocidades de assinatura mais lentas?</strong>
        <br><em>A) Porque o SLH-DSA exige controle de estado e rastreamento de índices de assinatura, o que impede ataques de repetição de chaves.</em>
        <br><em>B) Porque o SLH-DSA é um esquema baseado em hash sem estado (stateless) que depende apenas de funções de hash seguras, com zero suposições algébricas estruturadas (como reticulados) que poderiam ser comprometidas por futuros avanços matemáticos.</em>
        <br><em>C) Porque o SLH-DSA é mais rápido para assinar em hardware de microcontroladores restritos.</em>
        <br><strong>Resposta Correta: B.</strong> Como o SLH-DSA depende unicamente da resistência à colisão de funções de hash padrão (como SHA-2 ou SHA-3), ele não depende da complexidade de problemas de reticulados. Ele é matematicamente mais simples e menos vulnerável a futuras quebras criptográficas de natureza algébrica.
    </li>
    <br>
    <li><strong>Qual característica do SLH-DSA o torna altamente atraente para armazenamento em ROM de inicialização segura (Secure Boot) e fusíveis programáveis uma única vez (OTP) de hardware?</strong>
        <br><em>A) Seu tamanho massivo de assinatura, que preenche o armazenamento para evitar estouros de buffer (buffer overflows).</em>
        <br><em>B) Sua velocidade de assinatura muito rápida, que acelera as linhas de programação na fábrica.</em>
        <br><em>C) Seu tamanho excepcionalmente minúsculo de chave pública de apenas 32 bytes, que cabe facilmente em registradores de fusíveis de chip limitados.</em>
        <br><strong>Resposta Correta: C.</strong> Chips de alta segurança têm espaço de ROM/OTP extremamente limitado para armazenar a âncora de confiança (chave pública). A chave pública do SLH-DSA tem apenas 32 bytes (igual ou menor que as chaves clássicas de ECC/RSA), facilitando incrivelmente seu armazenamento em fusíveis físicos do hardware.
    </li>
    <br>
    <li><strong>Um desenvolvedor de software está configurando um pipeline de CI/CD automatizado que assina milhares de microsserviços e pacotes compilados por hora. Qual assinatura pós-quântica (PQC) ele deve selecionar?</strong>
        <br><em>A) SLH-DSA-SHA2-128s, para minimizar o tamanho da chave pública em seu banco de dados.</em>
        <br><em>B) ML-DSA-65, porque suas velocidades de assinatura e verificação na casa dos sub-milissegundos evitam gargalos no pipeline mantendo a resistência quântica.</em>
        <br><em>C) XMSS baseado em estado (RFC 8391), porque o pipeline contínuo é perfeito para rastrear estados em instâncias de servidores paralelos.</em>
        <br><strong>Resposta Correta: B.</strong> Pipelines automatizados de compilação de software de alta frequência exigem velocidades rápidas de assinatura. O ML-DSA fornece assinaturas e verificações rápidas com tamanhos de assinatura razoáveis, tornando-o a escolha prática para entrega automatizada de software de uso geral.
    </li>
</ol>"""

references_md = """* [NIST FIPS 204: Module-Lattice-Based Digital Signature Standard](https://csrc.nist.gov/pubs/fips/204/final) (NIST, August 2024)
* [NIST FIPS 205: Stateless Hash-Based Digital Signature Standard](https://csrc.nist.gov/pubs/fips/205/final) (NIST, August 2024)
* [Post-Quantum Cryptography 2026: The Age of Deployment - CIR Report](https://www.cir-inc.com/product/post-quantum-cryptography-2026) (July 2026)
* [Encryption Consulting - The PQC Signature Selection Playbook & Firmware Signatures](https://www.encryptionconsulting.com/) (2025/2026)"""

success = update_repo(day_str, date_str, topic_en, topic_pt, file_name_prefix, category_en, category_pt, content_en, content_pt, references_md)
print("UPDATE STATUS:", success)
