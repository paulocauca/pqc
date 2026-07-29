
import sys
sys.path.append('/home/rycz/pqc/scripts')
from daily_updater import update_repo

day_str = "20"
date_str = "2026-07-29"
topic_en = "PQC in Practice: A 2026 Status Report on Real-World Adoption"
topic_pt = "Criptografia Pós-Quântica (PQC) na Prática: Um Relatório de Status da Adoção no Mundo Real em 2026"
file_name_prefix = "pqc_adoption_status_report_2026"
category_en = "PQC Adoption & Industry Status"
category_pt = "Adoção da PQC & Status da Indústria"
content_en = """
<h2>Day 20: PQC in Practice: A 2026 Status Report on Real-World Adoption</h2>

<p>The year 2026 marks a pivotal moment for Post-Quantum Cryptography (PQC), transitioning from a theoretical discipline to a practical and urgent reality. An industry event, the "PQC Update 2026," hosted by the Fraunhofer Institute for Secure Information Technology (AISEC), revealed that the post-quantum era is no longer a distant future but a present-day challenge for governments, standards bodies, and critical industries. The consensus is clear: the time for action is now.</p>

<p>This study explores the key findings from the 2026 PQC landscape, focusing on the shift from theoretical research to concrete implementation and the organizational hurdles that lie ahead.</p>

<h3>Key Takeaways from the 2026 PQC Landscape:</h3>
<ul>
  <li><strong>International Strategies are Solidifying:</strong> Nations are establishing clear roadmaps for PQC migration. The Netherlands, for instance, treats the transition as a collaborative national project. While approaches differ—Europe often favors long-term hybrid schemes as a safety net, whereas the U.S. and UK view them as a temporary bridge—the overall direction is one of coordinated, government-backed action.</li>
  <li><strong>Standards are Maturing and In Use:</strong> The Internet Engineering Task Force (IETF) is actively integrating PQC into core internet protocols like TLS and IPsec. More importantly, these standards are not just drafts; they are being implemented in real-world applications, such as German ID cards, which already incorporate PQC.</li>
  <li><strong>The Technology is Ready:</strong> Practical, working implementations of PQC are now available. This includes PQC-enabled ID cards, open-source security chips, Hardware Security Modules (HSMs), and even passwordless authentication systems built on new quantum-resistant algorithms.</li>
  <li><strong>The Challenge is Now Organizational, Not Technical:</strong> The primary obstacle is no longer the mathematical complexity of PQC but the logistical challenge of migration. This involves creating a comprehensive inventory of existing cryptographic systems, clarifying responsibilities within organizations, building new ecosystems, and executing a multi-year migration plan.</li>
</ul>

<div class="highlight-box">
  <h3>From Theory to Practice: The Era of PQC Migration</h3>
  <p>The central message from the PQC Update 2026 is that the debate is no longer about <em>if</em> the transition will happen, but <em>how well</em> organizations are prepared for it. The tools needed to identify and replace legacy cryptography are available. The question is no longer "Is it time?" but rather "Have you started?"</p>
</div>

<h3>Applicability to Internet Protocols and Cybersecurity</h3>
<p>The progress in PQC directly impacts the security of the entire internet. Here’s how:</p>
<ul>
  <li><strong>TLS (HTTPS):</strong> As the IETF finalizes standards, web browsers and servers are beginning to deploy hybrid key exchange mechanisms (e.g., X25519+ML-KEM) to protect web traffic from "Harvest Now, Decrypt Later" (HNDL) attacks.</li>
  <li><strong>IPsec (VPNs):</strong> Enterprise VPNs are being updated to support PQC, securing network connections against future quantum threats.</li>
  <li><strong>Digital Identity:</strong> The use of PQC in national ID cards demonstrates its readiness for critical public key infrastructure (PKI), securing digital identities and signatures for decades to come.</li>
</ul>

<h3>PQC Migration: A Comparison of National Approaches</h3>
<table class="comparison-table">
  <thead>
    <tr>
      <th>Feature</th>
      <th>European Union (EU) Approach</th>
      <th>U.S. / UK Approach</th>
      <th>Key Implication</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Role of Hybrid Schemes</strong></td>
      <td>Viewed as a long-term safety net, combining classical and PQC algorithms for many years.</td>
      <td>Considered a necessary but temporary transitional solution.</td>
      <td>The EU's strategy prioritizes stability and backward compatibility, while the U.S./UK approach aims for a faster, full transition.</td>
    </tr>
    <tr>
      <td><strong>Signature Schemes</strong></td>
      <td>Hash-based signatures (like SLH-DSA) are widely trusted and can be used standalone.</td>
      <td>Similar trust in hash-based signatures.</td>
      <td>Demonstrates strong international consensus on the security of stateless hash-based signatures.</td>
    </tr>
    <tr>
      <td><strong>Migration Driver</strong></td>
      <td>Collaborative, multi-stakeholder projects (e.g., the Dutch model).</td>
      <td>Driven by government mandates and directives (e.g., NIST standards, federal agency deadlines).</td>
      <td>Both approaches are effective, but the U.S. model may force a more rapid pace of adoption in the public sector.</td>
    </tr>
  </tbody>
</table>

<hr>

<h3>Daily Quiz</h3>
<ol>
  <li>What was the main conclusion of the "PQC Update 2026" event regarding the status of Post-Quantum Cryptography?
    <br>a) PQC is still a decade away from practical use.
    <br>b) The post-quantum era has already begun, and the main challenge is now organizational.
    <br>c) The mathematical foundations of PQC are still unproven.</li>
  <li>According to the IETF, which core internet protocols are being updated to include PQC?
    <br>a) FTP and Telnet
    <br>b) DNS and BGP
    <br>c) TLS and IPsec</li>
  <li>How do the EU and U.S./UK approaches to hybrid cryptographic schemes generally differ?
    <br>a) The EU rejects hybrid schemes, while the U.S. mandates them.
    <br>b) The EU sees them as a long-term safety net, while the U.S./UK see them as a temporary bridge.
    <br>c) Both see them as a permanent solution.</li>
</ol>
"""
content_pt = """
<h2>Dia 20: Criptografia Pós-Quântica (PQC) na Prática: Um Relatório de Status da Adoção no Mundo Real em 2026</h2>

<p>O ano de 2026 marca um momento crucial para a Criptografia Pós-Quântica (PQC), que transita de uma disciplina teórica para uma realidade prática e urgente. Um evento do setor, o "PQC Update 2026", organizado pelo Instituto Fraunhofer de Segurança da Informação (AISEC), revelou que a era pós-quântica não é mais um futuro distante, mas um desafio presente para governos, órgãos de padronização e indústrias críticas. O consenso é claro: a hora de agir é agora.</p>

<p>Este estudo explora as principais conclusões do cenário PQC de 2026, focando na mudança da pesquisa teórica para a implementação concreta e nos obstáculos organizacionais que se apresentam.</p>

<h3>Principais Conclusões do Cenário PQC em 2026:</h3>
<ul>
  <li><strong>Estratégias Internacionais Estão se Solidificando:</strong> As nações estão estabelecendo roteiros claros para a migração PQC. A Holanda, por exemplo, trata a transição como um projeto nacional colaborativo. Embora as abordagens divirjam — a Europa frequentemente favorece esquemas híbridos de longo prazo como uma rede de segurança, enquanto os EUA e o Reino Unido os veem como uma ponte temporária — a direção geral é de uma ação coordenada e apoiada pelo governo.</li>
  <li><strong>Padrões Estão Amadurecendo e em Uso:</strong> A Força-Tarefa de Engenharia da Internet (IETF) está integrando ativamente a PQC em protocolos centrais da internet, como TLS e IPsec. Mais importante, esses padrões não são apenas rascunhos; eles estão sendo implementados em aplicações do mundo real, como as carteiras de identidade alemãs, que já incorporam PQC.</li>
  <li><strong>A Tecnologia Está Pronta:</strong> Implementações práticas e funcionais de PQC já estão disponíveis. Isso inclui carteiras de identidade com PQC, chips de segurança de código aberto, Módulos de Segurança de Hardware (HSMs) e até sistemas de autenticação sem senha baseados em novos algoritmos resistentes à computação quântica.</li>
  <li><strong>O Desafio Agora é Organizacional, Não Técnico:</strong> O principal obstáculo não é mais a complexidade matemática da PQC, mas o desafio logístico da migração. Isso envolve a criação de um inventário abrangente dos sistemas criptográficos existentes, o esclarecimento de responsabilidades dentro das organizações, a construção de novos ecossistemas e a execução de um plano de migração plurianual.</li>
</ul>

<div class="highlight-box">
  <h3>Da Teoria à Prática: A Era da Migração PQC</h3>
  <p>A mensagem central do "PQC Update 2026" é que o debate não é mais sobre <em>se</em> a transição acontecerá, mas sobre <em>quão bem</em> as organizações estão preparadas para ela. As ferramentas necessárias para identificar e substituir a criptografia legada estão disponíveis. A pergunta não é mais "Já é hora?", mas sim "Você já começou?".</p>
</div>

<h3>Aplicabilidade a Protocolos de Internet e Cibersegurança</h3>
<p>O progresso na PQC impacta diretamente a segurança de toda a internet. Veja como:</p>
<ul>
  <li><strong>TLS (HTTPS):</strong> À medida que a IETF finaliza os padrões, navegadores web e servidores estão começando a implantar mecanismos de troca de chaves híbridos (ex: X25519+ML-KEM) para proteger o tráfego web contra ataques "Harvest Now, Decrypt Later" (HNDL).</li>
  <li><strong>IPsec (VPNs):</strong> As VPNs corporativas estão sendo atualizadas para suportar PQC, protegendo as conexões de rede contra futuras ameaças quânticas.</li>
  <li><strong>Identidade Digital:</strong> O uso de PQC em carteiras de identidade nacionais demonstra sua prontidão para infraestruturas de chave pública (PKI) críticas, garantindo a segurança de identidades e assinaturas digitais por décadas.</li>
</ul>

<h3>Migração PQC: Uma Comparação de Abordagens Nacionais</h3>
<table class="comparison-table">
  <thead>
    <tr>
      <th>Característica</th>
      <th>Abordagem da União Europeia (UE)</th>
      <th>Abordagem dos EUA / Reino Unido</th>
      <th>Implicação Principal</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Papel dos Esquemas Híbridos</strong></td>
      <td>Vistos como uma rede de segurança de longo prazo, combinando algoritmos clássicos e PQC por muitos anos.</td>
      <td>Considerados uma solução de transição necessária, mas temporária.</td>
      <td>A estratégia da UE prioriza a estabilidade e a retrocompatibilidade, enquanto a abordagem dos EUA/Reino Unido visa uma transição completa e mais rápida.</td>
    </tr>
    <tr>
      <td><strong>Esquemas de Assinatura</strong></td>
      <td>Assinaturas baseadas em hash (como SLH-DSA) são amplamente confiáveis e podem ser usadas de forma autônoma.</td>
      <td>Confiança semelhante em assinaturas baseadas em hash.</td>
      <td>Demonstra um forte consenso internacional sobre a segurança das assinaturas baseadas em hash sem estado.</td>
    </tr>
    <tr>
      <td><strong>Motor da Migração</strong></td>
      <td>Projetos colaborativos com múltiplos stakeholders (ex: o modelo holandês).</td>
      <td>Impulsionada por mandatos e diretrizes governamentais (ex: padrões do NIST, prazos para agências federais).</td>
      <td>Ambas as abordagens são eficazes, mas o modelo dos EUA pode forçar um ritmo de adoção mais rápido no setor público.</td>
    </tr>
  </tbody>
</table>

<hr>

<h3>Auto-avaliação</h3>
<ol>
  <li>Qual foi a principal conclusão do evento "PQC Update 2026" sobre o status da Criptografia Pós-Quântica?
    <br>a) A PQC ainda está a uma década de uso prático.
    <br>b) A era pós-quântica já começou, e o principal desafio agora é organizacional.
    <br>c) Os fundamentos matemáticos da PQC ainda não foram provados.</li>
  <li>De acordo com a IETF, quais protocolos centrais da internet estão sendo atualizados para incluir a PQC?
    <br>a) FTP e Telnet
    <br>b) DNS e BGP
    <br>c) TLS e IPsec</li>
  <li>Como as abordagens da UE e dos EUA/Reino Unido para esquemas criptográficos híbridos geralmente diferem?
    <br>a) A UE rejeita esquemas híbridos, enquanto os EUA os tornam obrigatórios.
    <br>b) A UE os vê como uma rede de segurança de longo prazo, enquanto os EUA/Reino Unido os veem como uma ponte temporária.
    <br>c) Ambos os veem como uma solução permanente.</li>
</ol>
"""
references_md = "[From Early Warning Signs to the Workbench: the PQC Update 2026 Shows that the Post-Quantum Era Has Begun](https://www.cybersecurity.blog.aisec.fraunhofer.de/en/from-early-warning-signs-to-the-workbench-the-pqc-update-2026-shows-that-the-post-quantum-era-has-begun)"

success = update_repo(day_str, date_str, topic_en, topic_pt, file_name_prefix, category_en, category_pt, content_en, content_pt, references_md)
print("UPDATE STATUS:", success)
