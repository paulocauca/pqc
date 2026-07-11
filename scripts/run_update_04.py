import sys
sys.path.append('/home/rycz/pqc/scripts')
from daily_updater import update_repo

day_str = "04"
date_str = "2026-07-11"
topic_en = "Post-Quantum Cryptography in Virtual Private Networks (VPNs): The Transition to Hybrid WireGuard and PQPSK"
topic_pt = "Criptografia Pós-Quântica em Redes Privadas Virtuais (VPNs): A Transição para WireGuard Híbrido e PQPSK"
file_name_prefix = "wireguard_pqc_transition"
category_en = "Virtual Private Network (VPN) Security"
category_pt = "Segurança de Redes Privadas Virtuais (VPNs)"

content_en = """<p>In virtual private networks (VPNs), securing the confidentiality of encrypted tunnels is of paramount importance. VPNs are the primary targets for <strong>Harvest Now, Decrypt Later (HNDL)</strong> attacks, where adversaries record encrypted traffic today in hopes of decrypting it once Cryptographically Relevant Quantum Computers (CRQCs) emerge. As the industry moves towards post-quantum standards, two parallel paths have emerged for securing VPN tunnels: the immediate addition of <strong>Post-Quantum Preshared Keys (PQPSKs)</strong> and the integration of <strong>Hybrid Key Encapsulation Mechanisms (ML-KEM + Curve25519)</strong> inside modern VPN handshakes.</p>

<div class="highlight-box">
    <p><strong>The Core Security Architecture:</strong> VPN protocols like WireGuard rely on a highly streamlined public-key exchange. To achieve quantum resistance, architects can either inject a 256-bit post-quantum preshared key (PQPSK) into the key derivation process—effectively acting as a secure symmetric shield immune to Shor's algorithm—or implement a fully automated hybrid handshake combining <strong>ML-KEM-768</strong> with classical <strong>Curve25519</strong>.</p>
</div>

<h2>WireGuard's Noise Handshake & The Post-Quantum Preshared Key (PQPSK)</h2>
<p>WireGuard is built on a specific handshake pattern from the Noise Protocol Framework, known as <code>Noise_IKpsk2_25519_ChaChaPoly_BLAKE2s</code>. This pattern utilizes Curve25519 for key exchange, ChaCha20-Poly1305 for symmetric encryption, and BLAKE2s for hashing. To address the quantum threat without changing the lightweight codebase, WireGuard introduces an optional 256-bit symmetric pre-shared key (PSK) that is mixed into the handshake state machine:</p>

<ul>
    <li><strong>Symmetric Resistance:</strong> While classical public-key cryptography (Curve25519) is completely broken by Shor's algorithm, symmetric cryptography remains highly resilient. Under Grover's algorithm, a 256-bit symmetric key is reduced to 128 bits of security, which is still mathematically infeasible to brute-force.</li>
    <li><strong>Handshake Modification:</strong> The pre-shared key is mixed into the Noise session's key derivation chain during the second message (<code>psk2</code>). If the Curve25519 keys are broken retrospectively, an attacker still cannot decrypt the traffic unless they have also stolen the symmetric PSK.</li>
    <li><strong>Key Management Challenge:</strong> Although PQPSKs provide excellent quantum immunity today, they require out-of-band key distribution, making them difficult to scale across thousands of enterprise endpoints.</li>
</ul>

<h2>The Rise of Hybrid WireGuard Handshakes (2026 Status)</h2>
<p>To overcome the scale limitations of manual preshared keys, modern implementations and operating systems in 2026 have introduced native <strong>Post-Quantum Hybrid Handshakes (PQ-HS)</strong>. By integrating ML-KEM-768 directly into the handshake process, the protocol achieves automated quantum-safe session negotiation without manual key management:</p>

<ul>
    <li><strong>How it works:</strong> The handshake executes two simultaneous key exchanges: one using the classical Curve25519 and another using ML-KEM-768. The resulting secrets are combined using a secure key derivation function (KDF) to produce the final session keys.</li>
    <li><strong>Kernel-Native Speed:</strong> Benchmarks in 2026 show that the performance of hybrid handshakes (such as <code>ML-KEM-768 + Curve25519</code>) on modern server and mobile processors is exceptional, with less than an 8% increase in connection latency and negligible impact on battery life.</li>
    <li><strong>Interoperability & Fallbacks:</strong> Much like TLS 1.3, hybrid VPN handshakes are negotiated with fallback options, ensuring that older legacy clients can still establish classic tunnels while updated clients immediately benefit from quantum-resistant protection.</li>
</ul>

<h2>Protocol & Metric Comparison</h2>
<p>This table compares the security, key sizes, and operational overhead of classical VPN handshakes, symmetric PSK modes, and native hybrid post-quantum tunnels:</p>

<table class="comparison-table">
    <thead>
        <tr>
            <th>VPN Protocol Mode</th>
            <th>Cryptographic Primitives</th>
            <th>Symmetric Key Size</th>
            <th>Handshake Overhead</th>
            <th>Quantum Resistance Status</th>
            <th>Best Suited For</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Classical WireGuard</strong></td>
            <td>Curve25519 + ChaChaPoly</td>
            <td>N/A (No PSK)</td>
            <td>Extremely Low (~148 bytes)</td>
            <td><strong>Vulnerable</strong> (Broken by Shor's)</td>
            <td>Legacy networks and low-priority public traffic</td>
        </tr>
        <tr>
            <td><strong>WireGuard with PQPSK</strong></td>
            <td>Curve25519 + 256-bit PSK</td>
            <td>256 bits</td>
            <td>Minimal (+32 bytes)</td>
            <td><strong>Quantum-Safe</strong> (Symmetric Shield)</td>
            <td>Static site-to-site tunnels and high-security links</td>
        </tr>
        <tr>
            <td><strong>Hybrid WireGuard (2026)</strong></td>
            <td>ML-KEM-768 + Curve25519</td>
            <td>N/A (Auto-negotiated)</td>
            <td>Moderate (~2.3 KB)</td>
            <td><strong>Quantum-Safe</strong> (Algorithmic Hybrid)</td>
            <td>Enterprise remote access, dynamic mesh networks, and mobile clients</td>
        </tr>
    </tbody>
</table>

<div class="page-break"></div>

<h2>Daily Quiz: Test Your Understanding</h2>
<ol>
    <li><strong>How does a Post-Quantum Preshared Key (PQPSK) protect a WireGuard tunnel against a future quantum computer?</strong>
        <br><em>A) It utilizes a lattice-based mathematical signature to verify every packet on the wire.</em>
        <br><em>B) It injects a 256-bit symmetric key into the Noise handshake, forcing quantum attackers to use Grover's algorithm, which leaves an unbreakable 128 bits of security.</em>
        <br><em>C) It increases the encryption block size of ChaCha20 from 64 bits to 2048 bits to overwhelm quantum memory.</em>
        <br><strong>Correct Answer: B.</strong> Because symmetric cryptography is highly resistant to quantum algorithms, mixing a 256-bit PSK into the session key derivation protects the tunnel even if the Curve25519 key exchange is broken.
    </li>
    <br>
    <li><strong>What is the primary operational drawback of using the symmetric PQPSK mode in large-scale enterprise VPNs?</strong>
        <br><em>A) It drastically slows down the data transmission throughput by over 50%.</em>
        <br><em>B) It requires a constant, active connection to a central NIST-hosted licensing server.</em>
        <br><em>C) It presents a key management challenge, as symmetric keys must be securely distributed out-of-band to all peers beforehand.</em>
        <br><strong>Correct Answer: C.</strong> Distributing and rotating static preshared keys across thousands of remote employees or devices is logistically complex, which is why automated hybrid handshakes are preferred for dynamic networks.
    </li>
    <br>
    <li><strong>In a Hybrid WireGuard handshake (Curve25519 + ML-KEM-768), what happens if a mathematical vulnerability is discovered in the new ML-KEM algorithm?</strong>
        <br><em>A) The entire VPN connection is instantly compromised and can be decrypted by any adversary.</em>
        <br><em>B) The protocol automatically falls back to cleartext UDP to prevent a kernel crash.</em>
        <br><em>C) The tunnel remains fully secure under the classical Curve25519 layer, requiring an attacker to break both algorithms to decrypt the session.</em>
        <br><strong>Correct Answer: C.</strong> The hybrid handshake design ensures "defense in depth," meaning that the tunnel is secure as long as at least one of the underlying algorithms (classical or post-quantum) remains unbroken.
    </li>
</ol>"""

content_pt = """<p>Nas redes privadas virtuais (VPNs), a proteção da confidencialidade dos túneis cifrados é de importância crítica. As VPNs são alvos prioritários de ataques do tipo <strong>Harvest Now, Decrypt Later (HNDL)</strong> (Coletar Agora, Decifrar Depois), nos quais os adversários capturam e armazenam o tráfego criptografado hoje para decifrá-lo no futuro assim que Computadores Quânticos Relevantes para Criptografia (CRQCs) estiverem disponíveis. Na transição para a era pós-quântica, dois caminhos paralelos consolidaram-se para proteger os túneis VPN: a adoção imediata de <strong>Chaves Pré-Compartilhadas Pós-Quânticas (PQPSKs)</strong> e a integração de <strong>Mecanismos de Encapsulamento de Chave Híbridos (ML-KEM + Curve25519)</strong> no handshake das VPNs modernas.</p>

<div class="highlight-box">
    <p><strong>A Arquitetura de Segurança Central:</strong> Protocolos de VPN modernos como o WireGuard dependem de uma troca de chaves públicas altamente simplificada. Para alcançar a resistência quântica, os arquitetos de rede podem injetar uma chave simétrica pré-compartilhada de 256 bits (PQPSK) no processo de derivação de chaves — agindo como um escudo simétrico imune ao algoritmo de Shor — ou implementar um handshake híbrido totalmente automatizado que combina o <strong>ML-KEM-768</strong> com a curva clássica <strong>Curve25519</strong>.</p>
</div>

<h2>O Handshake Noise do WireGuard e a Chave Pré-Compartilhada Pós-Quântica (PQPSK)</h2>
<p>O WireGuard é construído sobre um padrão específico de handshake do Noise Protocol Framework, chamado <code>Noise_IKpsk2_25519_ChaChaPoly_BLAKE2s</code>. Esse padrão usa a Curve25519 para troca de chaves, ChaCha20-Poly1305 para criptografia simétrica e BLAKE2s para hashing. Para mitigar a ameaça quântica sem alterar a base de código minimalista do protocolo, o WireGuard suporta uma chave simétrica opcional de 256 bits (PSK) que é mesclada na máquina de estados do handshake:</p>

<ul>
    <li><strong>Resistência Simétrica:</strong> Embora a criptografia clássica de chave pública (Curve25519) seja completamente quebrada pelo algoritmo de Shor, a criptografia simétrica permanece altamente segura. Sob o algoritmo de Grover, uma chave simétrica de 256 bits mantém 128 bits de segurança efetiva, o que é matematicamente impossível de quebrar por força bruta.</li>
    <li><strong>Modificação do Handshake:</strong> A chave pré-compartilhada é integrada na cadeia de derivação de chaves da sessão Noise durante a segunda mensagem (<code>psk2</code>). Mesmo que as chaves Curve25519 sejam quebradas retrospectivamente, o invasor não poderá decifrar o tráfego sem possuir também a chave PSK simétrica.</li>
    <li><strong>Desafio de Gerenciamento:</strong> Embora as PQPSKs forneçam excelente imunidade quântica hoje, elas exigem distribuição de chaves fora de banda (out-of-band), dificultando a escalabilidade do gerenciamento de chaves em milhares de endpoints corporativos.</li>
</ul>

<h2>O Surgimento do Handshake Híbrido no WireGuard (Status em 2026)</h2>
<p>Para superar as limitações de escala do gerenciamento manual de chaves pré-compartilhadas, implementações modernas e sistemas operacionais em 2026 introduziram os handshakes nativos de <strong>Troca de Chaves Híbrida Pós-Quântica (PQ-HS)</strong>. Ao integrar o ML-KEM-768 diretamente ao processo de handshake, o protocolo estabelece sessões seguras pós-quânticas de forma automatizada:</p>

<ul>
    <li><strong>Como funciona:</strong> O handshake realiza duas trocas de chaves simultâneas: uma usando a Curve25519 clássica e outra usando o ML-KEM-768. Os segredos resultantes são combinados por meio de uma função de derivação de chave (KDF) segura para produzir as chaves finais da sessão.</li>
    <li><strong>Velocidade Nativa no Kernel:</strong> Testes de benchmark em 2026 demonstram que o desempenho dos handshakes híbridos (como <code>ML-KEM-768 + Curve25519</code>) em processadores de servidores e dispositivos móveis é excelente, com um acréscimo inferior a 8% na latência de conexão e impacto insignificante no consumo de bateria.</li>
    <li><strong>Interoperabilidade e Fallbacks:</strong> Assim como no TLS 1.3, os handshakes de VPN híbridos são negociados com opções de fallback, garantindo que clientes legados continuem estabelecendo túneis clássicos de forma transparente, enquanto clientes atualizados usufruem imediatamente da proteção pós-quântica.</li>
</ul>

<h2>Comparação de Protocolos e Métricas</h2>
<p>Esta tabela compara a segurança, tamanhos de chaves e sobrecarga operacional dos modos de handshake clássicos, do uso de PSK simétrica e dos novos túneis híbridos pós-quânticos nativos:</p>

<table class="comparison-table">
    <thead>
        <tr>
            <th>Modo do Protocolo VPN</th>
            <th>Primitivas Criptográficas</th>
            <th>Tamanho da Chave Simétrica</th>
            <th>Sobrecarga no Handshake</th>
            <th>Status de Resistência Quântica</th>
            <th>Melhor Indicado Para</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>WireGuard Clássico</strong></td>
            <td>Curve25519 + ChaChaPoly</td>
            <td>Não aplicável (Sem PSK)</td>
            <td>Extremamente Baixa (~148 bytes)</td>
            <td><strong>Vulnerável</strong> (Quebrado pelo algoritmo de Shor)</td>
            <td>Redes legadas e tráfego público de baixa prioridade</td>
        </tr>
        <tr>
            <td><strong>WireGuard com PQPSK</strong></td>
            <td>Curve25519 + PSK de 256 bits</td>
            <td>256 bits</td>
            <td>Mínima (+32 bytes)</td>
            <td><strong>Seguro Pós-Quântico</strong> (Escudo Simétrico)</td>
            <td>Túneis estáticos ponto a ponto (site-to-site) e conexões de alta segurança</td>
        </tr>
        <tr>
            <td><strong>WireGuard Híbrido (2026)</strong></td>
            <td>ML-KEM-768 + Curve25519</td>
            <td>Não aplicável (Auto-negociado)</td>
            <td>Moderada (~2,3 KB)</td>
            <td><strong>Seguro Pós-Quântico</strong> (Híbrido Algorítmico)</td>
            <td>Acesso remoto corporativo, redes em malha dinâmica (mesh) e clientes móveis</td>
        </tr>
    </tbody>
</table>

<div class="page-break"></div>

<h2>Quiz Diário: Teste seu Conhecimento</h2>
<ol>
    <li><strong>Como uma Chave Pré-Compartilhada Pós-Quântica (PQPSK) protege um túnel WireGuard contra futuros computadores quânticos?</strong>
        <br><em>A) Ela utiliza uma assinatura matemática baseada em reticulados para verificar cada pacote transmitido.</em>
        <br><em>B) Ela injeta uma chave simétrica de 256 bits no handshake Noise, forçando atacantes quânticos a usar o algoritmo de Grover, o que preserva uma segurança inquebrável de 128 bits.</em>
        <br><em>C) Ela aumenta o tamanho do bloco de criptografia do ChaCha20 de 64 bits para 2048 bits para sobrecarregar a memória quântica.</em>
        <br><strong>Resposta Correta: B.</strong> Como a criptografia simétrica é altamente resistente a ataques quânticos, a inclusão de uma chave PSK de 256 bits na derivação de chaves da sessão protege o túnel mesmo que a troca de chaves Curve25519 seja quebrada retrospectivamente.
    </li>
    <br>
    <li><strong>Qual é o principal desafio operacional ao adotar o modo simétrico PQPSK em VPNs corporativas de grande escala?</strong>
        <br><em>A) Ele reduz drasticamente a taxa de transferência de dados em mais de 50%.</em>
        <br><em>B) Ele exige uma conexão ativa e constante com um servidor de licenciamento central hospedado pelo NIST.</em>
        <br><em>C) Ele apresenta um grande desafio de gerenciamento de chaves, pois as chaves simétricas precisam ser distribuídas de forma segura fora de banda para todos os pares previamente.</em>
        <br><strong>Resposta Correta: C.</strong> Distribuir e rotacionar chaves pré-compartilhadas estáticas entre milhares de funcionários ou dispositivos remotos é logisticamente complexo, motivo pelo qual os handshakes híbridos automatizados são preferidos para redes corporativas dinâmicas.
    </li>
    <br>
    <li><strong>Em um handshake WireGuard Híbrido (Curve25519 + ML-KEM-768), o que acontece se uma falha matemática for descoberta no novo algoritmo ML-KEM?</strong>
        <br><em>A) Todo o túnel VPN é instantaneamente comprometido e pode ser decifrado por qualquer adversário.</em>
        <br><em>B) O protocolo rebaixa automaticamente a conexão para UDP em texto claro para evitar uma falha catastrófica no kernel.</em>
        <br><em>C) O túnel permanece totalmente protegido pela camada clássica Curve25519, exigindo que o invasor quebre ambos os algoritmos para decifrar a sessão.</em>
        <br><strong>Resposta Correta: C.</strong> O design do handshake híbrido garante "defesa em profundidade", o que significa que o túnel é considerado seguro desde que pelo menos um dos algoritmos subjacentes (o clássico ou o pós-quântico) permaneça íntegro.
    </li>
</ol>"""

references_md = """* [WireGuard Protocol and Cryptography Documentation](https://www.wireguard.com/protocol/) (2025/2026)
* [Post-quantum WireGuard - Cryptology ePrint Archive](https://eprint.iacr.org/2020/379) (Hülsing et al., 2020)
* [VPN Protocols in 2026: Deep Dive into WireGuard, OpenVPN, IKEv2, and Next-Gen Standards](https://tunnelpicks.net/blog/vpn-protocols-2026-wireguard-openvpn-ikev2) (June 2026)
* [Post-Quantum Networking: WireGuard PQC and the Future of the VPN](https://www.fosslinux.com/156600/post-quantum-networking-wireguard-pqc-and-the-future-of-the-vpn.htm) (June 2026)"""

success = update_repo(day_str, date_str, topic_en, topic_pt, file_name_prefix, category_en, category_pt, content_en, content_pt, references_md)
print("UPDATE STATUS:", success)
