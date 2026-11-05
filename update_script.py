
import sys
sys.path.append('/home/rycz/pqc/scripts')
from daily_updater import update_repo

day_str = "50"
date_str = "2026-11-05"
topic_en = "Side-Channel Attacks on PQC Implementations"
topic_pt = "Ataques de Canal Lateral em Implementações PQC"
file_name_prefix = "pqc_side_channel_attacks"
category_en = "PQC Security and Implementation"
category_pt = "Segurança e Implementação de PQC"
content_en = """<h2>Understanding Side-Channel Attacks in the PQC Era</h2>
<p>As the world transitions to Post-Quantum Cryptography (PQC), the focus is not just on the mathematical robustness of algorithms like ML-KEM and ML-DSA, but also on their physical implementation. Side-channel attacks (SCAs) exploit information leaked from the physical hardware executing cryptographic operations, rather than from theoretical weaknesses in the algorithms themselves. These attacks are a critical threat to the real-world security of PQC.</p>

<h3>How do Side-Channel Attacks work?</h3>
<p>SCAs monitor physical characteristics of a device to infer secret data. Common side-channels include:</p>
<ul>
    <li><b>Power Consumption:</b> Different CPU instructions consume slightly different amounts of power. Power analysis attacks (SPA, DPA) can reveal patterns related to secret keys.</li>
    <li><b>Electromagnetic (EM) Emissions:</b> Electronic devices emit EM fields. These emissions can be captured and analyzed to reveal internal operations.</li>
    <li><b>Timing Information:</b> The time taken to perform a cryptographic operation can depend on the input data, including the secret key.</li>
    <li><b>Acoustic Cryptanalysis:</b> The sounds produced by a device's components (like capacitors) can sometimes leak information.</li>
</ul>

<div class="highlight-box">
    <h4>Why are PQC algorithms vulnerable?</h4>
    <p>Many PQC algorithms, especially lattice-based ones like CRYSTALS-Kyber (ML-KEM) and Dilithium (ML-DSA), rely on complex mathematical operations like polynomial multiplication and rejection sampling. These operations can have data-dependent execution paths or memory access patterns, creating measurable side-channel leakages if not implemented carefully.</p>
</div>

<h3>Real-World Applicability to Internet Protocols</h3>
<p>The security of protocols like TLS 1.3, SSH, and VPNs, which are starting to incorporate PQC, depends entirely on the secure implementation of the underlying algorithms. A side-channel vulnerability in a server's ML-KEM implementation could allow an attacker to recover the private key by monitoring its power consumption or EM emissions, completely bypassing the quantum-resistant mathematics. This would allow them to decrypt traffic and compromise the security of the entire communication channel.</p>

<h3>Countermeasures and Mitigation Strategies</h3>
<p>Protecting against SCAs requires a combination of software and hardware techniques:</p>
<table class="comparison-table">
    <thead>
        <tr>
            <th>Technique</th>
            <th>Description</th>
            <th>Applicability</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><b>Constant-Time Implementation</b></td>
            <td>Ensuring that cryptographic operations take the same amount of time, regardless of the input data. This mitigates timing attacks.</td>
            <td>Software</td>
        </tr>
        <tr>
            <td><b>Masking</b></td>
            <td>Splitting secret data into multiple random shares. Operations are performed on the shares, making it harder to correlate side-channel information with the original secret.</td>
            <td>Software/Hardware</td>
        </tr>
        <tr>
            <td><b>Hiding</b></td>
            <td>Introducing noise or shuffling operations to obscure the correlation between the side-channel leakage and the data being processed.</td>
            <td>Hardware</td>
        </tr>
        <tr>
            <td><b>Formal Verification</b></td>
            <td>Using mathematical methods to formally prove that an implementation is resistant to certain classes of side-channel attacks.</td>
            <td>Software</td>
        </tr>
    </tbody>
</table>

<h3>Daily Quiz</h3>
<ol>
    <li>What is the primary difference between a side-channel attack and a traditional cryptanalytic attack?</li>
    <li>Why are operations like rejection sampling in PQC algorithms a potential source of side-channel leakage?</li>
    <li>Explain how a constant-time implementation helps mitigate timing attacks.</li>
</ol>"""
content_pt = """<h2>Entendendo Ataques de Canal Lateral na Era PQC</h2>
<p>À medida que o mundo faz a transição para a Criptografia Pós-Quântica (PQC), o foco não está apenas na robustez matemática de algoritmos como ML-KEM e ML-DSA, mas também em sua implementação física. Ataques de canal lateral (SCAs) exploram informações vazadas do hardware físico que executa operações criptográficas, em vez de fraquezas teóricas nos próprios algoritmos. Esses ataques são uma ameaça crítica para a segurança real da PQC.</p>

<h3>Como funcionam os Ataques de Canal Lateral?</h3>
<p>SCAs monitoram características físicas de um dispositivo para inferir dados secretos. Canais laterais comuns incluem:</p>
<ul>
    <li><b>Consumo de Energia:</b> Diferentes instruções da CPU consomem quantidades de energia ligeiramente diferentes. Ataques de análise de potência (SPA, DPA) podem revelar padrões relacionados a chaves secretas.</li>
    <li><b>Emissões Eletromagnéticas (EM):</b> Dispositivos eletrônicos emitem campos EM. Essas emissões podem ser capturadas e analisadas para revelar operações internas.</li>
    <li><b>Informações de Tempo:</b> O tempo necessário para realizar uma operação criptográfica pode depender dos dados de entrada, incluindo a chave secreta.</li>
    <li><b>Criptoanálise Acústica:</b> Os sons produzidos pelos componentes de um dispositivo (como capacitores) às vezes podem vazar informações.</li>
</ul>

<div class="highlight-box">
    <h4>Por que os algoritmos PQC são vulneráveis?</h4>
    <p>Muitos algoritmos PQC, especialmente os baseados em reticulados como CRYSTALS-Kyber (ML-KEM) and Dilithium (ML-DSA), dependem de operações matemáticas complexas como multiplicação de polinômios e amostragem de rejeição. Essas operações podem ter caminhos de execução ou padrões de acesso à memória dependentes dos dados, criando vazamentos de canal lateral mensuráveis se não forem implementadas com cuidado.</p>
</div>

<h3>Aplicabilidade no Mundo Real para Protocolos da Internet</h3>
<p>A segurança de protocolos como TLS 1.3, SSH e VPNs, que estão começando a incorporar PQC, depende inteiramente da implementação segura dos algoritmos subjacentes. Uma vulnerabilidade de canal lateral na implementação de ML-KEM de um servidor poderia permitir que um invasor recuperasse a chave privada monitorando seu consumo de energia ou emissões EM, contornando completamente a matemática quântico-resistente. Isso lhes permitiria descriptografar o tráfego e comprometer a segurança de todo o canal de comunicação.</p>

<h3>Contramedidas e Estratégias de Mitigação</h3>
<p>A proteção contra SCAs requer uma combinação de técnicas de software e hardware:</p>
<table class="comparison-table">
    <thead>
        <tr>
            <th>Técnica</th>
            <th>Descrição</th>
            <th>Aplicabilidade</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><b>Implementação em Tempo Constante</b></td>
            <td>Garantir que as operações criptográficas levem a mesma quantidade de tempo, independentemente dos dados de entrada. Isso mitiga ataques de tempo.</td>
            <td>Software</td>
        </tr>
        <tr>
            <td><b>Mascaramento</b></td>
            <td>Dividir dados secretos em múltiplas partes aleatórias. As operações são realizadas nas partes, tornando mais difícil correlacionar informações de canal lateral com o segredo original.</td>
            <td>Software/Hardware</td>
        </tr>
        <tr>
            <td><b>Ocultação (Hiding)</b></td>
            <td>Introduzir ruído ou embaralhar operações para ofuscar a correlação entre o vazamento do canal lateral e os dados que estão sendo processados.</td>
            <td>Hardware</td>
        </tr>
        <tr>
            <td><b>Verificação Formal</b></td>
            <td>Usar métodos matemáticos para provar formalmente que uma implementação é resistente a certas classes de ataques de canal lateral.</td>
            <td>Software</td>
        </tr>
    </tbody>
</table>

<h3>Auto-avaliação</h3>
<ol>
    <li>Qual é a principal diferença entre um ataque de canal lateral e um ataque criptoanalítico tradicional?</li>
    <li>Por que operações como a amostragem de rejeição em algoritmos PQC são uma fonte potencial de vazamento de canal lateral?</li>
    <li>Explique como uma implementação em tempo constante ajuda a mitigar ataques de tempo.</li>
</ol>"""
references_md = """*   [IACR ePrint Archive](https://eprint.iacr.org/)
*   [NIST Computer Security Resource Center](https://csrc.nist.gov/projects/post-quantum-cryptography)"""

success = update_repo(day_str, date_str, topic_en, topic_pt, file_name_prefix, category_en, category_pt, content_en, content_pt, references_md)
print("UPDATE STATUS:", success)
