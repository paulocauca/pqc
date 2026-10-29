
import sys
sys.path.append('/home/rycz/pqc/scripts')
from daily_updater import update_repo

day_str = "44"
date_str = "2026-10-29"
topic_en = "The Future of PQC: Beyond the First NIST Standards"
topic_pt = "O Futuro da PQC: Além dos Primeiros Padrões do NIST"
file_name_prefix = "pqc_future_beyond_nist"
category_en = "PQC Foundational Concepts"
category_pt = "Conceitos Fundamentais de PQC"
content_en = """<h2>The Future of PQC: Beyond the First NIST Standards</h2>
<p>As the world begins the transition to the first generation of NIST-standardized PQC algorithms (ML-KEM, ML-DSA, SLH-DSA), the cryptographic community is already looking ahead. The standardization process is not an endpoint but a milestone in a continuous journey to secure our digital infrastructure against future threats. Today, we explore what lies beyond these initial standards and how the landscape of post-quantum cryptography will continue to evolve.</p>

<h3>The Need for Continuous Evolution</h3>
<p>The current PQC standards are the result of years of intense scrutiny, but no algorithm is perfect, and the quantum threat itself is still theoretical. Several factors drive the need for ongoing research and development:</p>
<ul>
    <li><strong>New Quantum Algorithms:</strong> Shor's and Grover's algorithms are the best-known quantum threats, but new quantum algorithms could emerge, aiting the mathematical foundations of our current PQC standards.</li>
    <li><strong>Implementation Vulnerabilities:</strong> Even with secure algorithm designs, vulnerabilities can be introduced during implementation (e.g., side-channel attacks). Research into "implementation-aware" cryptography and hardening techniques is crucial.</li>
    <li><strong>Performance and Efficiency:</strong> The first PQC standards represent a trade-off between security and performance. Future algorithms may offer better efficiency, smaller key/signature sizes, or faster computation, making them more suitable for a wider range of applications, especially in resource-constrained environments like IoT.</li>
    <li><strong>Diversification of Cryptographic Assumptions:</strong> The majority of the current lattice-based candidates (like Kyber and Dilithium) rely on similar mathematical problems. To avoid a cryptographic monoculture, NIST is already planning a future standardization round to encourage the development of algorithms based on different mathematical foundations.</li>
</ul>

<h3>What's Next on the PQC Roadmap?</h3>
<p>NIST has outlined a path forward that includes a new call for proposals for public-key encryption and digital signature schemes, with a focus on algorithms that are not based on structured lattices. This is intended to diversify the portfolio of available PQC standards.</p>
<p>Key areas of active research include:</p>
<ul>
    <li><strong>Isogeny-Based Cryptography:</strong> Algorithms like SIKE (Supersingular Isogeny Key Encapsulation) were once promising candidates but were broken in 2022. However, research in this area continues, as it offers very small key sizes.</li>
    <li><strong>Hash-Based Signatures:</strong> While SLH-DSA (SPHINCS+) is already standardized, it is a stateless hash-based signature scheme. Research into stateful schemes and other variations continues to offer different performance trade-offs.</li>
    <li><strong>Code-Based Cryptography:</strong> Schemes like Classic McEliece offer high security but have large key sizes. Research is focused on reducing these overheads.</li>
    <li><strong>Symmetric-Key Cryptography:</strong> The impact of quantum computers on symmetric-key algorithms like AES is less dramatic but still significant. Grover's algorithm effectively halves the key strength, which is why the transition to AES-256 is recommended.</li>
</ul>

<h3>Applicability to Internet Protocols</h3>
<p>The evolution of PQC will directly impact internet protocols. Crypto-agility—the ability to easily swap out cryptographic algorithms—is more critical than ever. Future versions of TLS, SSH, and VPN protocols will need to be designed to accommodate new PQC standards with minimal disruption. Hybrid schemes, combining a classical and a post-quantum algorithm, will likely remain a key transition strategy, providing a safety net as new PQC algorithms are deployed and battle-tested in real-world environments.</p>

<h3>Comparison of PQC Algorithm Families</h3>
<table class="comparison-table">
    <thead>
        <tr>
            <th>Algorithm Family</th>
            <th>Main Advantage</th>
            <th>Main Disadvantage</th>
            <th>Current NIST Standard</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Lattice-Based</strong></td>
            <td>Strong security, good performance, relatively small key/signature sizes.</td>
            <td>Relies on a single family of mathematical problems.</td>
            <td>ML-KEM, ML-DSA</td>
        </tr>
        <tr>
            <td><strong>Hash-Based</strong></td>
            <td>Security is well-understood (based on the security of hash functions).</td>
            <td>Signatures can be large, and some schemes are stateful.</td>
            <td>SLH-DSA</td>
        </tr>
        <tr>
            <td><strong>Code-Based</strong></td>
            <td>Long history of security against both classical and quantum attacks.</td>
            <td>Very large public key sizes.</td>
            <td>N/A (was a finalist)</td>
        </tr>
        <tr>
            <td><strong>Isogeny-Based</strong></td>
            <td>Very small key sizes.</td>
            <td>Currently broken, active area of research to fix.</td>
            <td>N/A (was a finalist)</td>
        </tr>
        <tr>
            <td><strong>Multivariate</strong></td>
            <td>Small signatures.</td>
            <td>Some schemes have been broken; complex security analysis.</td>
            <td>N/A</td>
        </tr>
    </tbody>
</table>

<div class="highlight-box">
    <p><strong>Key Takeaway:</strong> The PQC transition is a marathon, not a sprint. The first NIST standards are a critical first step, but the journey requires continuous research, development, and adaptation to stay ahead of emerging threats.</p>
</div>

<h3>Daily Quiz</h3>
<ol>
    <li>Why is cryptographic monoculture a concern in the context of PQC?</li>
    <li>What does "crypto-agility" mean, and why is it important for internet protocols?</li>
    <li>Which PQC algorithm family is known for its very large public key sizes but has a long history of security?</li>
</ol>
"""
content_pt = """<h2>O Futuro da PQC: Além dos Primeiros Padrões do NIST</h2>
<p>Enquanto o mundo inicia a transição para a primeira geração de algoritmos PQC padronizados pelo NIST (ML-KEM, ML-DSA, SLH-DSA), a comunidade criptográfica já está olhando para o futuro. O processo de padronização não é um ponto final, mas um marco em uma jornada contínua para proteger nossa infraestrutura digital contra ameaças futuras. Hoje, exploramos o que está além desses padrões iniciais e como o cenário da criptografia pós-quântica continuará a evoluir.</p>

<h3>A Necessidade de Evolução Contínua</h3>
<p>Os padrões PQC atuais são o resultado de anos de escrutínio intenso, mas nenhum algoritmo é perfeito, e a própria ameaça quântica ainda é teórica. Vários fatores impulsionam a necessidade de pesquisa e desenvolvimento contínuos:</p>
<ul>
    <li><strong>Novos Algoritmos Quânticos:</strong> Os algoritmos de Shor e Grover são as ameaças quânticas mais conhecidas, mas novos algoritmos quânticos podem surgir, potencialmente visando os fundamentos matemáticos de nossos padrões PQC atuais.</li>
    <li><strong>Vulnerabilidades de Implementação:</strong> Mesmo com designs de algoritmos seguros, vulnerabilidades podem ser introduzidas durante a implementação (por exemplo, ataques de canal lateral). A pesquisa em criptografia "consciente da implementação" e técnicas de endurecimento é crucial.</li>
    <li><strong>Performance e Eficiência:</strong> Os primeiros padrões PQC representam um equilíbrio entre segurança e performance. Algoritmos futuros podem oferecer maior eficiência, tamanhos de chave/assinatura menores ou computação mais rápida, tornando-os mais adequados para uma gama mais ampla de aplicações, especialmente em ambientes com recursos restritos como a IoT.</li>
    <li><strong>Diversificação das Suposições Criptográficas:</strong> A maioria dos candidatos atuais baseados em reticulados (como Kyber e Dilithium) depende de problemas matemáticos semelhantes. Para evitar uma monocultura criptográfica, o NIST já está planejando uma futura rodada de padronização para incentivar o desenvolvimento de algoritmos baseados em diferentes fundamentos matemáticos.</li>
</ul>

<h3>O Que Vem a Seguir no Roadmap da PQC?</h3>
<p>O NIST delineou um caminho a seguir que inclui uma nova chamada para propostas de esquemas de criptografia de chave pública e assinatura digital, com foco em algoritmos que não são baseados em reticulados estruturados. Isso tem como objetivo diversificar o portfólio de padrões PQC disponíveis.</p>
<p>As principais áreas de pesquisa ativa incluem:</p>
<ul>
    <li><strong>Criptografia Baseada em Isogenias:</strong> Algoritmos como o SIKE (Supersingular Isogeny Key Encapsulation) foram candidatos promissores, mas foram quebrados em 2022. No entanto, a pesquisa nesta área continua, pois oferece tamanhos de chave muito pequenos.</li>
    <li><strong>Assinaturas Baseadas em Hash:</strong> Embora o SLH-DSA (SPHINCS+) já esteja padronizado, ele é um esquema de assinatura baseado em hash sem estado (<em>stateless</em>). A pesquisa em esquemas com estado (<em>stateful</em>) e outras variações continua a oferecer diferentes equilíbrios de performance.</li>
    <li><strong>Criptografia Baseada em Código:</strong> Esquemas como o Classic McEliece offer high security but have large key sizes. Research is focused on reducing these overheads.</li>
    <li><strong>Criptografia de Chave Simétrica:</strong> O impacto dos computadores quânticos em algoritmos de chave simétrica como o AES é menos dramático, mas ainda significativo. O algoritmo de Grover efetivamente reduz pela metade a força da chave, razão pela qual a transição para o AES-256 é recomendada.</li>
</ul>

<h3>Aplicabilidade aos Protocolos da Internet</h3>
<p>A evolução da PQC impactará diretamente os protocolos da internet. A criptoagilidade — a capacidade de trocar facilmente os algoritmos criptográficos — é mais crítica do que nunca. Versões futuras do TLS, SSH e protocolos VPN precisarão ser projetadas para acomodar novos padrões PQC com o mínimo de interrupção. Esquemas híbridos, combinando um algoritmo clássico e um pós-quântico, provavelmente continuarão sendo uma estratégia de transição chave, fornecendo uma rede de segurança à medida que novos algoritmos PQC são implantados e testados em ambientes do mundo real.</p>

<h3>Comparação das Famílias de Algoritmos PQC</h3>
<table class="comparison-table">
    <thead>
        <tr>
            <th>Família de Algoritmos</th>
            <th>Principal Vantagem</th>
            <th>Principal Desvantagem</th>
            <th>Padrão NIST Atual</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Baseado em Reticulado</strong></td>
            <td>Segurança forte, boa performance, tamanhos de chave/assinatura relativamente pequenos.</td>
            <td>Depende de uma única família de problemas matemáticos.</td>
            <td>ML-KEM, ML-DSA</td>
        </tr>
        <tr>
            <td><strong>Baseado em Hash</strong></td>
            <td>A segurança é bem compreendida (baseada na segurança das funções de hash).</td>
            <td>Assinaturas podem ser grandes, e alguns esquemas mantêm estado.</td>
            <td>SLH-DSA</td>
        </tr>
        <tr>
            <td><strong>Baseado em Código</strong></td>
            <td>Longo histórico de segurança contra ataques clássicos e quânticos.</td>
            <td>Tamanhos de chave pública muito grandes.</td>
            <td>N/A (foi finalista)</td>
        </tr>
        <tr>
            <td><strong>Baseado em Isogenia</strong></td>
            <td>Tamanhos de chave muito pequenos.</td>
            <td>Atualmente quebrado, área de pesquisa ativa para correção.</td>
            <td>N/A (foi finalista)</td>
        </tr>
        <tr>
            <td><strong>Multivariado</strong></td>
            <td>Assinaturas pequenas.</td>
            <td>Alguns esquemas foram quebrados; análise de segurança complexa.</td>
            <td>N/A</td>
        </tr>
    </tbody>
</table>

<div class="highlight-box">
    <p><strong>Ponto Chave:</strong> A transição PQC é uma maratona, não uma corrida de curta distância. Os primeiros padrões do NIST são um primeiro passo crítico, mas a jornada exige pesquisa, desenvolvimento e adaptação contínuos para se manter à frente das ameaças emergentes.</p>
</div>

<h3>Auto-avaliação Diária</h3>
<ol>
    <li>Por que a monocultura criptográfica é uma preocupação no contexto da PQC?</li>
    <li>O que significa "criptoagilidade" e por que ela é importante para os protocolos da internet?</li>
    <li>Qual família de algoritmos PQC é conhecida por seus tamanhos de chave pública muito grandes, mas possui um longo histórico de segurança?</li>
</ol>
"""
references_md = ""

success = update_repo(day_str, date_str, topic_en, topic_pt, file_name_prefix, category_en, category_pt, content_en, content_pt, references_md)
print("UPDATE STATUS:", success)
