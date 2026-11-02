
import sys
sys.path.append('/home/rycz/pqc/scripts')
from daily_updater import update_repo

day_str = "48"
date_str = "2026-11-02"
topic_en = "The Role of the IETF in Standardizing Post-Quantum Cryptography for the Internet"
topic_pt = "O Papel da IETF na Padronização da Criptografia Pós-Quântica para a Internet"
file_name_prefix = "ietf_pqc_standardization"
category_en = "PQC Adoption & Industry Status"
category_pt = "Adoção da PQC e Status da Indústria"
content_en = '''<h2>The Role of the IETF in Standardizing Post-Quantum Cryptography for the Internet</h2>

<p>The transition to Post-Quantum Cryptography (PQC) is not just about developing new algorithms, but also about integrating them into the protocols that power the internet. The Internet Engineering Task Force (IETF) plays a pivotal role in this process, ensuring that the next generation of cryptographic standards is robust, interoperable, and ready for global deployment.</p>

<h3>What is the IETF?</h3>

<p>The IETF is a large, open, international community of network designers, operators, vendors, and researchers concerned with the evolution of the internet architecture and the smooth operation of the internet. It is the primary body for developing and promoting internet standards, such as TCP/IP, HTTP, and TLS.</p>

<h3>Why is the IETF Crucial for PQC?</h3>

<p>For PQC to be effective, it must be seamlessly integrated into existing internet protocols. This is where the IETF comes in. The IETF's working groups are actively developing standards for using PQC in a variety of critical protocols, including:</p>

<ul>
  <li><strong>TLS (Transport Layer Security):</strong> The IETF is defining how to use PQC key exchange mechanisms, such as ML-KEM, in TLS 1.3. This will enable browsers and servers to establish quantum-resistant communication channels, protecting web traffic from future attacks.</li>
  <li><strong>SSH (Secure Shell):</strong> The IETF is working on new key exchange methods for SSH that incorporate PQC algorithms, ensuring that remote server administration remains secure in the quantum era.</li>
  <li><strong>IPsec (Internet Protocol Security):</strong> For securing network-level communication, such as in VPNs, the IETF is specifying how to use PQC to protect IKEv2 (Internet Key Exchange version 2) and the data transmitted over IPsec tunnels.</li>
  <li><strong>DNSSEC (Domain Name System Security Extensions):</strong> The IETF is exploring the use of PQC digital signature algorithms, like ML-DSA, to protect the integrity of DNS records, preventing DNS spoofing and other attacks.</li>
</ul>

<div class="highlight-box">
  The IETF's work is essential for ensuring that the transition to PQC is a coordinated and interoperable effort. Without these standards, different implementations of PQC could be incompatible, leading to a fragmented and less secure internet.
</div>

<h3>Key IETF Drafts and RFCs</h3>

<p>The IETF's work on PQC is documented in a series of Internet-Drafts and, eventually, RFCs (Request for Comments). Some of the key documents to watch include:</p>

<ul>
  <li><strong>draft-ietf-tls-pqc-kem:</strong> This draft specifies how to integrate PQC Key Encapsulation Mechanisms (KEMs) into TLS 1.3, including the use of hybrid key exchange.</li>
  <li><strong>draft-ietf-ipsecme-pqc-ikev2:</strong> This document outlines the use of PQC in IKEv2, enabling quantum-resistant VPNs.</li>
  <li><strong>draft-ietf-dnsop-pqc-dnssec:</strong> This draft explores the challenges and solutions for using PQC in DNSSEC, considering the impact on signature size and validation performance.</li>
</ul>

<h3>PQC Standardization Challenges</h3>

<p>The IETF faces several challenges in standardizing PQC for the internet:</p>

<table class="comparison-table">
  <tr>
    <th>Challenge</th>
    <th>Description</th>
    <th>IETF's Approach</th>
  </tr>
  <tr>
    <td><strong>Performance Overhead</strong></td>
    <td>PQC algorithms can have larger key sizes and signatures, and may require more computation, potentially impacting the performance of internet protocols.</td>
    <td>The IETF is carefully evaluating the performance of different PQC algorithms and is working on optimizations to minimize the impact on latency and bandwidth.</td>
  </tr>
  <tr>
    <td><strong>Packet Size Limitations</strong></td>
    <td>In some protocols, such as DNS, there are strict limits on packet size. The larger signatures of PQC algorithms can be a challenge.</td>
    <td>The IETF is exploring techniques such as signature aggregation and alternative signature schemes to address this issue.</td>
  </tr>
  <tr>
    <td><strong>Hybrid Key Exchange</strong></td>
    <td>To ensure a smooth and secure transition, the IETF is promoting a hybrid approach, where both classical and post-quantum key exchange are used together. This provides security against both classical and quantum computers.</td>
    <td>The IETF is standardizing how to implement hybrid key exchange in various protocols, ensuring that it is done in a secure and interoperable way.</td>
  </tr>
</table>

<h3>Daily Quiz</h3>

<ol>
  <li>What is the primary role of the IETF in the context of PQC?
    <br>a) Developing new PQC algorithms.
    <br>b) Standardizing the integration of PQC into internet protocols.
    <br>c) Manufacturing quantum computers.</li>
  <li>What is a "hybrid key exchange"?
    <br>a) A key exchange that uses both symmetric and asymmetric cryptography.
    <br>b) A key exchange that combines a classical and a post-quantum algorithm.
    <br>c) A key exchange that is only used in hybrid clouds.</li>
  <li>Which of the following is NOT a protocol where the IETF is actively working to integrate PQC?
    <br>a) TLS
    <br>b) FTP
    <br>c) SSH</li>
</ol>
'''
content_pt = '''<h2>O Papel da IETF na Padronização da Criptografia Pós-Quântica para a Internet</h2>

<p>A transição para a Criptografia Pós-Quântica (PQC) não se trata apenas de desenvolver novos algoritmos, mas também de integrá-los aos protocolos que sustentam a internet. A Força-Tarefa de Engenharia da Internet (IETF) desempenha um papel fundamental nesse processo, garantindo que a próxima geração de padrões criptográficos seja robusta, interoperável e pronta para implantação global.</p>

<h3>O que é a IETF?</h3>

<p>A IETF é uma comunidade internacional grande e aberta de projetistas de rede, operadores, fornecedores e pesquisadores preocupados com a evolução da arquitetura da internet e seu funcionamento contínuo. É o principal órgão para o desenvolvimento e promoção de padrões da internet, como TCP/IP, HTTP e TLS.</p>

<h3>Por que a IETF é Crucial para a PQC?</h3>

<p>Para que a PQC seja eficaz, ela deve ser integrada de forma transparente aos protocolos de internet existentes. É aqui que a IETF entra. Os grupos de trabalho da IETF estão desenvolvendo ativamente padrões para o uso da PQC em uma variedade de protocolos críticos, incluindo:</p>

<ul>
  <li><strong>TLS (Transport Layer Security):</strong> A IETF está definindo como usar mecanismos de troca de chaves PQC, como o ML-KEM, no TLS 1.3. Isso permitirá que navegadores e servidores estabeleçam canais de comunicação quântico-resistentes, protegendo o tráfego da web contra ataques futuros.</li>
  <li><strong>SSH (Secure Shell):</strong> A IETF está trabalhando em novos métodos de troca de chaves para o SSH que incorporam algoritmos PQC, garantindo que a administração remota de servidores permaneça segura na era quântica.</li>
  <li><strong>IPsec (Internet Protocol Security):</strong> Para proteger a comunicação no nível da rede, como em VPNs, a IETF está especificando como usar a PQC para proteger o IKEv2 (Internet Key Exchange version 2) e os dados transmitidos por túneis IPsec.</li>
  <li><strong>DNSSEC (Domain Name System Security Extensions):</strong> A IETF está explorando o uso de algoritmos de assinatura digital PQC, como o ML-DSA, para proteger a integridade dos registros DNS, prevenindo spoofing de DNS e outros ataques.</li>
</ul>

<div class="highlight-box">
  O trabalho da IETF é essencial para garantir que a transição para a PQC seja um esforço coordenado e interoperável. Sem esses padrões, diferentes implementações da PQC poderiam ser incompatíveis, levando a uma internet fragmentada e menos segura.
</div>

<h3>Principais Rascunhos e RFCs da IETF</h3>

<p>O trabalho da IETF sobre PQC está documentado em uma série de Rascunhos da Internet e, eventualmente, RFCs (Request for Comments). Alguns dos principais documentos a serem observados incluem:</p>

<ul>
  <li><strong>draft-ietf-tls-pqc-kem:</strong> Este rascunho especifica como integrar Mecanismos de Encapsulamento de Chaves (KEMs) PQC ao TLS 1.3, incluindo o uso de troca de chaves híbrida.</li>
  <li><strong>draft-ietf-ipsecme-pqc-ikev2:</strong> Este documento descreve o uso da PQC no IKEv2, permitindo VPNs quântico-resistentes.</li>
  <li><strong>draft-ietf-dnsop-pqc-dnssec:</strong> Este rascunho explora os desafios e soluções para o uso da PQC no DNSSEC, considerando o impacto no tamanho da assinatura e no desempenho da validação.</li>
</ul>

<h3>Desafios da Padronização da PQC</h3>

<p>A IETF enfrenta vários desafios na padronização da PQC para a internet:</p>

<table class="comparison-table">
  <tr>
    <th>Desafio</th>
    <th>Descrição</th>
    <th>Abordagem da IETF</th>
  </tr>
  <tr>
    <td><strong>Sobrecarga de Desempenho</strong></td>
    <td>Os algoritmos PQC podem ter chaves e assinaturas maiores e podem exigir mais computação, impactando potencialmente o desempenho dos protocolos de internet.</td>
    <td>A IETF está avaliando cuidadosamente o desempenho de diferentes algoritmos PQC e trabalhando em otimizações para minimizar o impacto na latência e na largura de banda.</td>
  </tr>
  <tr>
    <td><strong>Limitações de Tamanho de Pacote</strong></td>
    <td>Em alguns protocolos, como o DNS, existem limites rígidos para o tamanho do pacote. As assinaturas maiores dos algoritmos PQC podem ser um desafio.</td>
    <td>A IETF está explorando técnicas como agregação de assinaturas e esquemas de assinatura alternativos para resolver esse problema.</td>
  </tr>
  <tr>
    <td><strong>Troca de Chaves Híbrida</strong></td>
    <td>Para garantir uma transição suave e segura, a IETF está promovendo uma abordagem híbrida, onde a troca de chaves clássica e a pós-quântica são usadas em conjunto. Isso fornece segurança contra computadores clássicos e quânticos.</td>
    <td>A IETF está padronizando como implementar a troca de chaves híbrida em vários protocolos, garantindo que seja feita de forma segura e interoperável.</td>
  </tr>
</table>

<h3>Auto-avaliação</h3>

<ol>
  <li>Qual é o papel principal da IETF no contexto da PQC?
    <br>a) Desenvolver novos algoritmos PQC.
    <br>b) Padronizar a integração da PQC nos protocolos de internet.
    <br>c) Fabricar computadores quânticos.</li>
  <li>O que é uma "troca de chaves híbrida"?
    <br>a) Uma troca de chaves que usa tanto criptografia simétrica quanto assimétrica.
    <br>b) Uma troca de chaves que combina um algoritmo clássico e um pós-quântico.
    <br>c) Uma troca de chaves usada apenas em nuvens híbridas.</li>
  <li>Qual dos seguintes NÃO é um protocolo onde a IETF está trabalhando ativamente para integrar a PQC?
    <br>a) TLS
    <br>b) FTP
    <br>c) SSH</li>
</ol>
'''
references_md = "- [draft-ietf-tls-pqc-kem](https://datatracker.ietf.org/doc/draft-ietf-tls-pqc-kem/)\\n- [draft-ietf-ipsecme-pqc-ikev2](https://datatracker.ietf.org/doc/draft-ietf-ipsecme-pqc-ikev2/)\\n- [draft-ietf-dnsop-pqc-dnssec](https://datatracker.ietf.org/doc/draft-ietf-dnsop-pqc-dnssec/)"

success = update_repo(day_str, date_str, topic_en, topic_pt, file_name_prefix, category_en, category_pt, content_en, content_pt, references_md)
print("UPDATE STATUS:", success)
