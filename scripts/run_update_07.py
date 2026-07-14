import sys
sys.path.append('/home/rycz/pqc/scripts')
from daily_updater import update_repo

day_str = "07"
date_str = "2026-07-14"
topic_en = "Post-Quantum IPsec and IKEv2: Securing Enterprise VPNs with RFC 9370, RFC 9242, and ML-KEM"
topic_pt = "IPsec e IKEv2 Pós-Quânticos: Protegendo VPNs Corporativas com RFC 9370, RFC 9242 e ML-KEM"
file_name_prefix = "ipsec_ikev2_pqc_transition"
category_en = "Virtual Private Networks (VPN) & Enterprise Security"
category_pt = "Segurança de Redes Privadas Virtuais (VPNs) e Corporativa"

content_en = """<h2>Introduction: The Quantum Threat to Enterprise VPNs</h2>
<p>Enterprise virtual private networks (VPNs) rely heavily on <strong>IPsec (Internet Protocol Security)</strong> and its control plane protocol, <strong>IKEv2 (Internet Key Exchange Protocol Version 2)</strong>, to establish secure cryptographic tunnels across untrusted networks. Traditionally, peers use classical Diffie-Hellman (DH) or Elliptic Curve Diffie-Hellman (ECDH) during the <span class="code">IKE_SA_INIT</span> phase to agree upon session keys. However, classical public-key cryptography is highly vulnerable to future quantum computers running Shor’s algorithm, exposing enterprise traffic to "Harvest-Now, Decrypt-Later" (HNDL) attacks.</p>

<div class="highlight-box">
    <p><strong>Harvest-Now, Decrypt-Later (HNDL):</strong> Passive adversaries record today's encrypted VPN handshake and payload traffic. Once a cryptographically relevant quantum computer (CRQC) is built, they can decrypt the historical sessions, exposing sensitive corporate data, credentials, and proprietary intellectual property.</p>
</div>

<h2>RFC 9370: Enabling Multiple Key Exchanges in IKEv2</h2>
<p>In May 2023, the IETF published <strong>RFC 9370</strong>, which extends IKEv2 to allow multiple key exchanges to take place while establishing a Security Association (SA). Rather than forcing a hard cutover from classical to post-quantum algorithms—which introduces significant migration risk—RFC 9370 standardizes a hybrid approach. This ensures that the derived keys are cryptographically secure as long as <em>either</em> the classical or the post-quantum algorithm remains unbroken.</p>
<p>To implement this, RFC 9370 leverages the <strong>IKE_INTERMEDIATE</strong> exchange (defined in <strong>RFC 9242</strong>). Let's see how the handshake structure is adapted:</p>
<ul>
    <li><strong>IKE_SA_INIT:</strong> The initiator and responder perform a lightweight, classical key exchange (e.g., using X25519 or ECDH Curve P-256) to establish a baseline encrypted channel. This lightweight step prevents denial-of-service (DoS) attacks from wasting intensive post-quantum resources.</li>
    <li><strong>IKE_INTERMEDIATE:</strong> Within the newly encrypted—but quantum-vulnerable—channel, the peers conduct one or more intermediate exchanges to transmit the larger post-quantum Key Exchange Mechanism (KEM) payloads (e.g., ML-KEM-768).</li>
    <li><strong>IKE_AUTH:</strong> Finally, the peers authenticate each other, compile all exchange results, and derive the secure session keys (SKEYSEED) combining both classical and post-quantum shared secrets.</li>
</ul>

<h3>The Vital Role of IKE_INTERMEDIATE (RFC 9242)</h3>
<p>Post-Quantum algorithms, specifically lattice-based KEMs like ML-KEM, require substantially larger public keys and ciphertexts than their classical counterparts. For instance, an ML-KEM-768 public key is 1,184 bytes, compared to just 32 bytes for X25519. If these payloads were crammed into the initial <span class="code">IKE_SA_INIT</span> packet, the message would easily exceed the standard Ethernet Maximum Transmission Unit (MTU) of 1,500 bytes. This would lead to IP fragmentation at the network layer, which is frequently dropped by firewalls and middleboxes, resulting in connection timeouts.</p>
<p>By using <span class="code">IKE_INTERMEDIATE</span>, the post-quantum key exchange is performed after the initial encrypted channel is up, allowing the protocol to securely handle larger packets and leverage IKEv2's built-in cryptographic fragmentation capabilities if necessary.</p>

<h2>Real-World Cybersecurity Applicability and 2026 Status</h2>
<p>The transition of enterprise IPsec VPNs to post-quantum security is moving from theoretical drafts into active, widespread production deployment. In 2026, several industry leaders have integrated these capabilities:</p>
<ul>
    <li><strong>IETF Standard Drafts:</strong> The draft <span class="code">draft-ietf-ipsecme-ikev2-mlkem</span> specifies the direct mapping of ML-KEM (FIPS 203) as the additional key exchange under RFC 9370, removing previous interoperability issues caused by non-standardized ciphersuites.</li>
    <li><strong>Cloudflare One:</strong> Cloudflare has upgraded its SASE (Secure Access Service Edge) platform to support hybrid ML-KEM for IPsec tunnels, enabling enterprise clients to secure their offices, VPCs, and branches against HNDL attacks.</li>
    <li><strong>Fortinet (FortiOS 7.6.1):</strong> Fortinet’s NGFW now supports FIPS 203-compliant ML-KEM-512, ML-KEM-768, and ML-KEM-1024, enabling robust, multi-round hybrid key exchanges.</li>
    <li><strong>StrongSwan:</strong> The widely used open-source IPsec daemon has seen successful experimental integration of ML-KEM in tandem with hardware acceleration for high-throughput enterprise gateways.</li>
</ul>

<h2>Key Metrics Comparison: Classical vs. Hybrid vs. Pure PQC</h2>
<p>The table below summarizes the trade-offs in parameter sizes, round-trips, and cryptographic resilience across key exchange profiles in IKEv2.</p>

<table class="comparison-table">
    <thead>
        <tr>
            <th>Key Exchange Method</th>
            <th>Base Cryptography</th>
            <th>Public Key Size</th>
            <th>Ciphertext Size</th>
            <th>Quantum Resistance</th>
            <th>Fragmentation Risk</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>X25519 (Classical)</strong></td>
            <td>ECDH (Curve25519)</td>
            <td>32 bytes</td>
            <td>32 bytes</td>
            <td>None (Vulnerable to CRQC)</td>
            <td>Negligible</td>
        </tr>
        <tr>
            <td><strong>ML-KEM-768 (Pure PQC)</strong></td>
            <td>Module-Lattice (FIPS 203)</td>
            <td>1,184 bytes</td>
            <td>1,088 bytes</td>
            <td>Yes (NIST Level 3)</td>
            <td>Moderate (if in IKE_SA_INIT)</td>
        </tr>
        <tr>
            <td><strong>Hybrid X25519 + ML-KEM-768 (RFC 9370)</strong></td>
            <td>Hybrid (DH + Lattice)</td>
            <td>1,216 bytes</td>
            <td>1,120 bytes</td>
            <td>Yes (Failsafe Classical + PQ)</td>
            <td>Low (Mitigated via IKE_INTERMEDIATE)</td>
        </tr>
    </tbody>
</table>

<div class="page-break"></div>

<h2>Daily Quiz / Auto-Avaliação</h2>
<div class="highlight-box">
    <p><strong>1. Why doesn't RFC 9370 recommend sending ML-KEM public keys directly in the <span class="code">IKE_SA_INIT</span> payload?</strong><br>
    a) Because ML-KEM is not secure enough to be sent in plaintext.<br>
    b) Because ML-KEM's large keys and ciphertexts would trigger IP fragmentation, which is often dropped by firewalls and middleboxes.<br>
    c) Because it would violate the FIPS 203 specification.<br>
    <em>Answer: b) The large size of lattice-based keys exceeds typical MTU limits, and conducting the exchange within <span class="code">IKE_INTERMEDIATE</span> prevents fragmentation failures.</em></p>
    
    <p><strong>2. What is the main security advantage of a hybrid key exchange (e.g., X25519 + ML-KEM-768) over a pure PQC key exchange?</strong><br>
    a) It executes twice as fast as pure PQC.<br>
    b) It satisfies the legal requirements of classical standards while maintaining security if either the classical or post-quantum mathematical assumption holds true.<br>
    c) It uses smaller key sizes than standard ECDH.<br>
    <em>Answer: b) It provides dual security boundaries, acting as a cryptographic failsafe against potential mathematical or implementation flaws in newly standardized PQC algorithms.</em></p>
    
    <p><strong>3. How does RFC 9370 update the terminology established in RFC 7296 for IKEv2?</strong><br>
    a) Replace IPsec with PQ-IPsec.<br>
    b) It renames Transform Type 4 from "Diffie-Hellman Group (D-H)" to "Key Exchange Method (KE)" to generalize all types of key exchange mechanisms, including KEMs.<br>
    c) It deprecates ESP (Encapsulating Security Payload).<br>
    <em>Answer: b) It generalizes the transform type and fields to easily accommodate non-DH mechanisms like post-quantum key encapsulation.</em></p>
</div>"""

content_pt = """<h2>Introdução: A Ameaça Quântica às VPNs Corporativas</h2>
<p>As redes privadas virtuais corporativas (VPNs) dependem fortemente do protocolo <strong>IPsec (Internet Protocol Security)</strong> e do seu plano de controle, o <strong>IKEv2 (Internet Key Exchange Protocol Version 2)</strong>, para estabelecer túneis criptográficos seguros em redes não confiáveis. Tradicionalmente, os pares usam o clássico Diffie-Hellman (DH) ou Elliptic Curve Diffie-Hellman (ECDH) durante a fase <span class="code">IKE_SA_INIT</span> para concordar com as chaves de sessão. No entanto, a criptografia de chave pública clássica é altamente vulnerável a futuros computadores quânticos que executem o algoritmo de Shor, expondo o tráfego corporativo a ataques do tipo "Harvest-Now, Decrypt-Later" (HNDL).</p>

<div class="highlight-box">
    <p><strong>Harvest-Now, Decrypt-Later (HNDL):</strong> Adversários passivos gravam hoje o tráfego criptografado de handshake e dados das VPNs. Assim que um computador quântico criptograficamente relevante (CRQC) estiver disponível, eles poderão decifrar as sessões históricas, expondo dados corporativos confidenciais, credenciais e propriedade intelectual proprietária.</p>
</div>

<h2>RFC 9370: Viabilizando Múltiplas Trocas de Chaves no IKEv2</h2>
<p>Em maio de 2023, o IETF publicou a <strong>RFC 9370</strong>, que estende o IKEv2 para permitir a realização de múltiplas trocas de chaves durante o estabelecimento de uma Associação de Segurança (SA). Em vez de forçar uma transição abrupta dos algoritmos clássicos para os pós-quânticos — o que introduziria riscos significativos de migração —, a RFC 9370 padroniza uma abordagem híbrida. Isso garante que as chaves derivadas permaneçam criptograficamente seguras desde que <em>pelo menos um</em> dos algoritmos (clássico ou pós-quântico) permaneça íntegro.</p>
<p>Para implementar isso, a RFC 9370 aproveita a troca <strong>IKE_INTERMEDIATE</strong> (definida na <strong>RFC 9242</strong>). Veja como a estrutura do handshake é adaptada:</p>
<ul>
    <li><strong>IKE_SA_INIT:</strong> O iniciador e o respondente realizam uma troca de chaves clássica e leve (por exemplo, usando X25519 ou ECDH Curve P-256) para estabelecer um canal criptografado inicial. Essa etapa leve evita que ataques de negação de serviço (DoS) esgotem recursos intensivos de computação pós-quântica.</li>
    <li><strong>IKE_INTERMEDIATE:</strong> Dentro do canal recém-criptografado — porém vulnerável quânticamente —, os pares realizam uma ou mais trocas intermediárias para transmitir as cargas úteis de Mecanismos de Encapsulamento de Chaves (KEM) pós-quânticos de maior tamanho (como o ML-KEM-768).</li>
    <li><strong>IKE_AUTH:</strong> Por fim, os pares autenticam-se mutuamente, compilam todos os resultados das trocas e derivam as chaves de sessão seguras (SKEYSEED), combinando os segredos compartilhados clássicos e pós-quânticos.</li>
</ul>

<h3>O Papel Vital da Troca IKE_INTERMEDIATE (RFC 9242)</h3>
<p>Os algoritmos pós-quânticos, especificamente os KEMs baseados em reticulados como o ML-KEM, exigem chaves públicas e textos cifrados substancialmente maiores do que seus equivalentes clássicos. Por exemplo, uma chave pública ML-KEM-768 possui 1.184 bytes, em comparação com apenas 32 bytes do X25519. Se essas cargas úteis fossem comprimidas no pacote inicial <span class="code">IKE_SA_INIT</span>, a mensagem facilmente excederia a Unidade Máxima de Transmissão (MTU) padrão da Ethernet de 1.500 bytes. Isso levaria à fragmentação de IP na camada de rede, que é frequentemente bloqueada por firewalls e roteadores intermediários, resultando em falhas de conexão.</p>
<p>Ao utilizar o <span class="code">IKE_INTERMEDIATE</span>, a troca de chaves pós-quântica é realizada após a ativação do canal criptografado inicial, permitindo que o protocolo gerencie pacotes maiores com segurança e utilize os recursos integrados de fragmentação criptográfica do IKEv2 se necessário.</p>

<h2>Aplicabilidade no Mundo Real da Cibersegurança e Status em 2026</h2>
<p>A transição das VPNs IPsec corporativas para a segurança pós-quântica está deixando de ser um rascunho teórico para se tornar uma implantação ativa e generalizada em produção. Em 2026, vários líderes do setor já integraram essas capacidades:</p>
<ul>
    <li><strong>Rascunhos de Padrões IETF:</strong> O rascunho <span class="code">draft-ietf-ipsecme-ikev2-mlkem</span> especifica o mapeamento direto do ML-KEM (FIPS 203) como a troca de chaves adicional sob a RFC 9370, eliminando problemas anteriores de interoperabilidade causados por suítes de cifra não padronizadas.</li>
    <li><strong>Cloudflare One:</strong> A Cloudflare atualizou sua plataforma SASE (Secure Access Service Edge) para suportar ML-KEM híbrido para túneis IPsec, permitindo que clientes corporativos protejam seus escritórios, VPCs e filiais contra ataques HNDL.</li>
    <li><strong>Fortinet (FortiOS 7.6.1):</strong> Os firewalls de próxima geração (NGFW) da Fortinet agora oferecem suporte a ML-KEM-512, ML-KEM-768 e ML-KEM-1024 em conformidade com o FIPS 203, permitindo trocas híbridas robustas e de múltiplas rodadas.</li>
    <li><strong>StrongSwan:</strong> O daemon IPsec de código aberto amplamente utilizado recebeu integrações experimentais de sucesso do ML-KEM em conjunto com aceleração de hardware para gateways corporativos de alto desempenho.</li>
</ul>

<h2>Comparação de Métricas Chave: Clássico vs. Híbrido vs. PQC Puro</h2>
<p>A tabela abaixo resume as compensações em tamanhos de parâmetros, rodadas de comunicação e resiliência criptográfica entre diferentes perfis de troca de chaves no IKEv2.</p>

<table class="comparison-table">
    <thead>
        <tr>
            <th>Método de Troca de Chaves</th>
            <th>Criptografia Base</th>
            <th>Tamanho da Chave Pública</th>
            <th>Tamanho do Texto Cifrado</th>
            <th>Resistência Quântica</th>
            <th>Risco de Fragmentação</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>X25519 (Clássico)</strong></td>
            <td>ECDH (Curve25519)</td>
            <td>32 bytes</td>
            <td>32 bytes</td>
            <td>Nenhuma (Vulnerável ao CRQC)</td>
            <td>Insignificante</td>
        </tr>
        <tr>
            <td><strong>ML-KEM-768 (PQC Puro)</strong></td>
            <td>Reticulados / Module-Lattice (FIPS 203)</td>
            <td>1.184 bytes</td>
            <td>1.088 bytes</td>
            <td>Sim (NIST Nível 3)</td>
            <td>Moderado (se no IKE_SA_INIT)</td>
        </tr>
        <tr>
            <td><strong>Híbrido X25519 + ML-KEM-768 (RFC 9370)</strong></td>
            <td>Híbrido (DH + Reticulados)</td>
            <td>1.216 bytes</td>
            <td>1.120 bytes</td>
            <td>Sim (Clássico + PQ Failsafe)</td>
            <td>Baixo (Mitigado via IKE_INTERMEDIATE)</td>
        </tr>
    </tbody>
</table>

<div class="page-break"></div>

<h2>Daily Quiz / Auto-Avaliação</h2>
<div class="highlight-box">
    <p><strong>1. Por que a RFC 9370 não recomenda o envio das chaves públicas do ML-KEM diretamente na carga útil do <span class="code">IKE_SA_INIT</span>?</strong><br>
    a) Porque o ML-KEM não é seguro o suficiente para ser enviado em texto limpo.<br>
    b) Porque o grande tamanho das chaves e textos cifrados do ML-KEM provocaria fragmentação de IP, que é frequentemente bloqueada por firewalls e intermediários de rede.<br>
    c) Porque violaria a especificação FIPS 203.<br>
    <em>Resposta: b) O grande tamanho das chaves baseadas em reticulados excede os limites de MTU típicos, e realizar a troca no <span class="code">IKE_INTERMEDIATE</span> evita falhas por fragmentação.</em></p>
    
    <p><strong>2. Qual é a principal vantagem de segurança de uma troca de chaves híbrida (ex: X25519 + ML-KEM-768) sobre uma troca de chaves puramente pós-quântica?</strong><br>
    a) Ela é executada duas vezes mais rápido que o PQC puro.<br>
    b) Ela atende aos requisitos legais de padrões clássicos e mantém a segurança caso a hipótese clássica OU a hipótese pós-quântica permaneça válida.<br>
    c) Ela usa chaves menores do que o ECDH padrão.<br>
    <em>Resposta: b) Oferece uma margem dupla de segurança, atuando como um plano de contingência (failsafe) criptográfico contra potenciais falhas matemáticas ou de implementação nos novos algoritmos PQC padronizados.</em></p>
    
    <p><strong>3. De que forma a RFC 9370 atualiza a terminologia estabelecida na RFC 7296 para o IKEv2?</strong><br>
    a) Substitui o IPsec por PQ-IPsec.<br>
    b) Renomeia o Tipo de Transformação 4 de "Grupo Diffie-Hellman (D-H)" para "Método de Troca de Chaves (KE)" para generalizar todos os tipos de mecanismos de troca de chaves, incluindo os KEMs pós-quânticos.<br>
    c) Deprecia o ESP (Encapsulating Security Payload).<br>
    <em>Resposta: b) Generaliza o tipo de transformação e os campos para acomodar facilmente mecanismos que não são do tipo DH clássico, como o encapsulamento de chaves pós-quânticas.</em></p>
</div>"""

references_md = """* [RFC 9370: Multiple Key Exchanges in IKEv2](https://www.rfc-editor.org/rfc/rfc9370.html) (IETF, May 2023)
* [IETF Draft: Post-quantum Hybrid Key Exchange with ML-KEM in IKEv2](https://datatracker.ietf.org/doc/draft-ietf-ipsecme-ikev2-mlkem/) (Kampanakis, September 2025)
* [Cloudflare: Cloudflare One goes Post-Quantum with Hybrid ML-KEM IPsec](https://blog.cloudflare.com/post-quantum-sase/) (Cloudflare, 2026)
* [Integrating PQC into StrongSwan: ML-KEM integration for IPsec/IKEv2](https://semiiphub.com/pulse/expert-perspectives/integrating-pqc-into-strongswan-ml-kem-integration-for-ipsec-ikev2) (December 2025)"""

success = update_repo(day_str, date_str, topic_en, topic_pt, file_name_prefix, category_en, category_pt, content_en, content_pt, references_md)
print("UPDATE STATUS:", success)
