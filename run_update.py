
import sys
sys.path.append('/home/rycz/pqc/scripts')
from daily_updater import update_repo

day_str = "14"
date_str = "2026-07-23"
topic_en = "PQC Adoption in the Wild: A Look at Real-World Data"
topic_pt = "Adoção da PQC no Mundo Real: Uma Análise de Dados Concretos"
file_name_prefix = "pqc_adoption_real_world_data"
category_en = "PQC Adoption & Industry Status"
category_pt = "Adoção da PQC & Status da Indústria"
content_en = """<h2>PQC Adoption in the Wild: A Look at Real-World Data</h2>
<p>While the standardization of post-quantum algorithms like ML-KEM and ML-DSA is a monumental step, the real measure of success is their adoption in live internet protocols. A recent study from researchers at the University of Illinois at Urbana-Champaign provides a rare, data-driven look into the actual deployment of PQC in critical services like SSH, offering a crucial reality check on the global migration progress.</p>

<h3>The PQC Network Instrument: Measuring the Transition</h3>
<p>To understand real-world adoption, researchers developed a "PQC network instrument" to passively monitor traffic at a major supercomputing center. This allows for large-scale measurement without disrupting services, providing a unique vantage point on which cryptographic algorithms are being negotiated in the wild. The primary focus was on SSH and TLS, two of the most fundamental protocols for secure communication on the internet.</p>

<div class="highlight-box">
  <p><strong>Key Finding:</strong> The study revealed a nascent but growing adoption of PQC in SSH. The hybrid algorithm <code>sntrup761x25519-sha512@openssh.com</code> (a combination of a PQC algorithm and a classic Elliptic Curve algorithm) was detected, showing that major providers are beginning to experiment with and deploy quantum-resistant key exchange mechanisms. However, the overall adoption rate remains low, highlighting the significant work ahead.</p>
</div>

<h3>Adoption Rates: A Snapshot of Progress</h3>
<p>The research provides concrete, albeit early, metrics on the state of the PQC transition. This data is critical for understanding the gap between standards availability and real-world implementation.</p>

<table class="comparison-table">
  <thead>
    <tr>
      <th>Protocol</th>
      <th>PQC Implementation Status</th>
      <th>Observed Adoption Rate (at NCSA)</th>
      <th>Key Takeaway</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>SSH (Secure Shell)</strong></td>
      <td>Hybrid KEX available (e.g., in OpenSSH)</td>
      <td>~0.029% of connections</td>
      <td>Adoption is measurable but still in its infancy. The use of hybrid modes is the clear migration path.</td>
    </tr>
    <tr>
      <td><strong>TLS (Transport Layer Security)</strong></td>
      <td>Implementations exist (e.g., in Chrome via hybrid KEMs)</td>
      <td>Not explicitly measured in this study, but noted as an area of active deployment by major browsers.</td>
      <td>Browser-side adoption is leading, but server-side readiness remains a major hurdle.</td>
    </tr>
    <tr>
      <td><strong>RDP (Remote Desktop Protocol)</strong></td>
      <td>No simple PQC solution available</td>
      <td>0%</td>
      <td>Highlights a critical gap, as legacy and proprietary protocols often lag in cryptographic agility.</td>
    </tr>
  </tbody>
</table>

<h3>Challenges and Migration Pathways</h3>
<p>The study underscores that the transition is not just about having standardized algorithms; it involves a complex ecosystem of software libraries, protocol implementations, and system administration practices. Key challenges include:</p>
<ul>
    <li><strong>Server-Side Lag:</strong> While client-side applications like browsers are adopting PQC, many servers are not yet configured to negotiate PQC-enabled connections.</li>
    <li><strong>Legacy Systems:</strong> The continued use of deprecated classical algorithms in some connections poses an immediate security risk and indicates a lack of crypto-agility that will also hinder PQC migration.</li>
    <li><strong>Protocol Complexity:</strong> Integrating new, larger keys and different cryptographic primitives into established protocols without breaking compatibility is a significant engineering effort.</li>
</ul>
<p>The clear pathway forward, as demonstrated by the observed SSH traffic, is the use of <strong>hybrid mechanisms</strong>. This approach combines a classical and a post-quantum algorithm, ensuring security against both current and future threats and providing a safety net in case of unforeseen weaknesses in the new PQC algorithms.</p>

<h3>Daily Quiz</h3>
<ol>
    <li>What is the primary advantage of using a "hybrid" key exchange mechanism for PQC adoption?</li>
    <li>According to the study, which internet protocol showed a measurable (though small) adoption of a PQC algorithm?</li>
    <li>What is meant by "server-side lag" in the context of the PQC transition?</li>
</ol>"""
content_pt = """<h2>Adoção da PQC no Mundo Real: Uma Análise de Dados Concretos</h2>
<p>Embora a padronização de algoritmos pós-quânticos como o ML-KEM e o ML-DSA seja um passo monumental, a verdadeira medida de sucesso é a sua adoção em protocolos de internet ativos. Um estudo recente de pesquisadores da Universidade de Illinois em Urbana-Champaign oferece uma visão rara, baseada em dados, da implementação real da PQC em serviços críticos como o SSH, fornecendo uma verificação de realidade crucial sobre o progresso da migração global.</p>

<h3>O Instrumento de Rede PQC: Medindo a Transição</h3>
<p>Para entender a adoção no mundo real, os pesquisadores desenvolveram um "instrumento de rede PQC" para monitorar passivamente o tráfego em um grande centro de supercomputação. Isso permite a medição em larga escala sem interromper os serviços, oferecendo um ponto de vista único sobre quais algoritmos criptográficos estão sendo negociados em campo. O foco principal foi o SSH e o TLS, dois dos protocolos mais fundamentais para a comunicação segura na internet.</p>

<div class="highlight-box">
  <p><strong>Principal Descoberta:</strong> O estudo revelou uma adoção nascente, mas crescente, da PQC no SSH. O algoritmo híbrido <code>sntrup761x25519-sha512@openssh.com</code> (a combinação de um algoritmo PQC e um algoritmo clássico de Curva Elíptica) foi detectado, mostrando que grandes provedores estão começando a experimentar e implantar mecanismos de troca de chaves resistentes à computação quântica. No entanto, a taxa de adoção geral permanece baixa, destacando o significativo trabalho que ainda está por vir.</p>
</div>

<h3>Taxas de Adoção: Um Retrato do Progresso</h3>
<p>A pesquisa fornece métricas concretas, embora iniciais, sobre o estado da transição para a PQC. Esses dados são críticos para entender a lacuna entre a disponibilidade dos padrões e a implementação no mundo real.</p>

<table class="comparison-table">
  <thead>
    <tr>
      <th>Protocolo</th>
      <th>Status da Implementação PQC</th>
      <th>Taxa de Adoção Observada (no NCSA)</th>
      <th>Principal Conclusão</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>SSH (Secure Shell)</strong></td>
      <td>KEX híbrido disponível (ex: no OpenSSH)</td>
      <td>~0.029% das conexões</td>
      <td>A adoção é mensurável, mas ainda está em sua infância. O uso de modos híbridos é o caminho claro para a migração.</td>
    </tr>
    <tr>
      <td><strong>TLS (Transport Layer Security)</strong></td>
      <td>Implementações existem (ex: no Chrome via KEMs híbridos)</td>
      <td>Não medido explicitamente neste estudo, mas notado como uma área de implantação ativa pelos principais navegadores.</td>
      <td>A adoção do lado do cliente (navegador) está liderando, mas a prontidão do lado do servidor continua sendo um grande obstáculo.</td>
    </tr>
    <tr>
      <td><strong>RDP (Remote Desktop Protocol)</strong></td>
      <td>Nenhuma solução PQC simples disponível</td>
      <td>0%</td>
      <td>Destaca uma lacuna crítica, pois protocolos legados e proprietários frequentemente ficam para trás em agilidade criptográfica.</td>
    </tr>
  </tbody>
</table>

<h3>Desafios e Caminhos para a Migração</h3>
<p>O estudo ressalta que a transição não se resume a ter algoritmos padronizados; envolve um ecossistema complexo de bibliotecas de software, implementações de protocolos e práticas de administração de sistemas. Os principais desafios incluem:</p>
<ul>
    <li><strong>Atraso do Lado do Servidor (Server-Side Lag):</strong> Enquanto aplicações do lado do cliente, como navegadores, estão adotando a PQC, muitos servidores ainda não estão configurados para negociar conexões habilitadas para PQC.</li>
    <li><strong>Sistemas Legados:</strong> O uso contínuo de algoritmos clássicos obsoletos em algumas conexões representa um risco de segurança imediato e indica uma falta de agilidade criptográfica que também dificultará a migração para a PQC.</li>
    <li><strong>Complexidade do Protocolo:</strong> Integrar chaves novas e maiores e primitivas criptográficas diferentes em protocolos estabelecidos sem quebrar a compatibilidade é um esforço de engenharia significativo.</li>
</ul>
<p>O caminho claro a seguir, conforme demonstrado pelo tráfego SSH observado, é o uso de <strong>mecanismos híbridos</strong>. Essa abordagem combina um algoritmo clássico e um pós-quântico, garantindo segurança contra ameaças atuais e futuras e fornecendo uma rede de segurança em caso de fraquezas imprevistas nos novos algoritmos PQC.</p>

<h3>Auto-avaliação</h3>
<ol>
    <li>Qual é a principal vantagem de usar um mecanismo de troca de chaves "híbrido" para a adoção da PQC?</li>
    <li>De acordo com o estudo, qual protocolo de internet mostrou uma adoção mensurável (embora pequena) de um algoritmo PQC?</li>
    <li>O que significa "atraso do lado do servidor" (server-side lag) no contexto da transição para a PQC?</li>
</ol>"""
references_md = "- [Post-Quantum Cryptography (PQC) Network Instrument: Measuring PQC Adoption Rates and Identifying Migration Pathways](https://arxiv.org/html/2408.00054v3)"

success = update_repo(day_str, date_str, topic_en, topic_pt, file_name_prefix, category_en, category_pt, content_en, content_pt, references_md)
print("UPDATE STATUS:", success)
