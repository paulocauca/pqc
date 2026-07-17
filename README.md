# Post-Quantum Cryptography (PQC) - Daily Study & Monitoring

Welcome to the **Post-Quantum Cryptography (PQC)** repository. This repository is dedicated to the systematic study, daily monitoring, and mastery of PQC concepts, focusing on their mathematical foundations, security strengths, and practical cybersecurity applicability for the modern internet.

---

## 🎯 Repository Goals

The main objectives of this repository are:
1. **Master the Standards:** To deeply understand and analyze the official NIST Post-Quantum Cryptography Standards (FIPS 203, FIPS 204, and FIPS 205).
2. **Track the Frontier:** To monitor daily news, scientific papers, and industry shifts regarding quantum-resistant migration, security vulnerabilities, and network protocol integrations (e.g., TLS, SSH, VPNs).
3. **Dual-Language Education:** To build a high-quality, comprehensive study resource in both **English** and **Portuguese (pt-BR)** to bridge the knowledge gap for security professionals.
4. **Practical Application:** To analyze and document how these algorithms apply to securing communication, databases, and enterprise platforms in the real world.

---

## 📅 Latest Study Material

Here are the direct links to the latest study sheets and news digests:

- **English (EN):** [Day 09 - The 'Harvest Now, Decrypt Later' (HNDL) Threat Model (2026-07-17)](en/2026-07-17-hndl_threat_model.pdf)
- **Português (PT-BR):** [Dia 09 - O Modelo de Ameaça 'Harvest Now, Decrypt Later' (HNDL) (2026-07-17)](pt-BR/2026-07-17-hndl_threat_model.pdf)

*To see the full learning progression, view the [Study Timeline](./timeline).*

---

## 📚 Credits & Original Material

We acknowledge the original research, standards, and drafts provided by the **National Institute of Standards and Technology (NIST)** and the cryptography community:

### Official NIST FIPS Standards (Stored in `resources/`)
*   **FIPS 203 (ML-KEM):** [Module-Lattice-Based Key-Encapsulation Mechanism Standard](./resources/NIST.FIPS.203.pdf) — Derived from CRYSTALS-Kyber. Used for secure key exchange.
*   **FIPS 204 (ML-DSA):** [Module-Lattice-Based Digital Signature Standard](./resources/NIST.FIPS.204.pdf) — Derived from CRYSTALS-Dilithium. Used for general-purpose digital signatures.
*   **FIPS 205 (SLH-DSA):** [Stateless Hash-Based Digital Signature Standard](./resources/NIST.FIPS.205.pdf) — Derived from SPHINCS+. Used as a robust alternative signature scheme.

### Daily Tracking News & Resources (2026-07-09)
* [TLS 1.3 Hybrid Key Exchange using X25519Kyber768 / ML-KEM](https://www.netmeister.org/blog/tls-hybrid-kex.html) (October 2024)
* [Post-Quantum Hybrid Key Exchange for TLS 1.3 - Inside.java](https://inside.java/2026/02/17/tls-post-quantum-hybrid-key-exchange) (February 2026)
* [Hybrid Key Exchange Today: Why X25519 + ML-KEM Is the Interim Default - NetGuardia](https://netguardia.com/privacy/encryption/hybrid-key-exchange-today-why-x25519-ml-kem-is-the-interim-default) (April 2026)
* [Hybrid KEM: Running X25519 and ML-KEM Together in TLS - AfterRSA](https://www.afterrsa.com/atlas/pqc/hybrid-kem) (April 2026)

### Daily Tracking News & Resources (2026-07-10)
* [OpenSSH Post-Quantum Cryptography](https://www.openssh.org/pq.html) (2025/2026)
* [Ubuntu 26.04 Post-Quantum SSH Hardening](https://computingforgeeks.com/ubuntu-2604-post-quantum-ssh-hardening/) (April 2026)
* [OpenSSH 9.9 released with mlkem768x25519-sha256 - 4sysops](https://4sysops.com/archives/openssh-99-new-features-enhanced-security-with-post-quantum-key-exchange-mlkem768x25519-sha256-and-dsa-removal) (November 2024)

### Daily Tracking News & Resources (2026-07-11)
* [WireGuard Protocol and Cryptography Documentation](https://www.wireguard.com/protocol/) (2025/2026)
* [Post-quantum WireGuard - Cryptology ePrint Archive](https://eprint.iacr.org/2020/379) (Hülsing et al., 2020)
* [VPN Protocols in 2026: Deep Dive into WireGuard, OpenVPN, IKEv2, and Next-Gen Standards](https://tunnelpicks.net/blog/vpn-protocols-2026-wireguard-openvpn-ikev2) (June 2026)
* [Post-Quantum Networking: WireGuard PQC and the Future of the VPN](https://www.fosslinux.com/156600/post-quantum-networking-wireguard-pqc-and-the-future-of-the-vpn.htm) (June 2026)

### Daily Tracking News & Resources (2026-07-12)
* [Post-Quantum Cryptography in 2026: Where Browsers, CAs, and Enterprises Actually Stand - TigerTrust](https://www.tigertrust.io/blog/post-quantum-cryptography-2026-status) (Marcus Webb, March 2026)
* [Quantum-Secure Internet: Post-Quantum Cryptography, National Rollouts, and the Future of Digital Trust - RI Study Post](https://www.ristudypost.com/2026/01/quantum-secure-internet-post-quantum.html) (January 2026)
* [Post-Quantum Cryptography in 2026 - PQC Standards, Lattice-Based Encryption, and Quantum-Safe Security - Internet Pros](https://internet-pros.com/blog/post-quantum-cryptography-pqc-2026/) (2026)

### Daily Tracking News & Resources (2026-07-13)
* [NIST FIPS 204: Module-Lattice-Based Digital Signature Standard](https://csrc.nist.gov/pubs/fips/204/final) (NIST, August 2024)
* [NIST FIPS 205: Stateless Hash-Based Digital Signature Standard](https://csrc.nist.gov/pubs/fips/205/final) (NIST, August 2024)
* [Post-Quantum Cryptography 2026: The Age of Deployment - CIR Report](https://www.cir-inc.com/product/post-quantum-cryptography-2026) (July 2026)
* [Encryption Consulting - The PQC Signature Selection Playbook & Firmware Signatures](https://www.encryptionconsulting.com/) (2025/2026)

### Daily Tracking News & Resources (2026-07-14)
* [RFC 9370: Multiple Key Exchanges in IKEv2](https://www.rfc-editor.org/rfc/rfc9370.html) (IETF, May 2023)
* [IETF Draft: Post-quantum Hybrid Key Exchange with ML-KEM in IKEv2](https://datatracker.ietf.org/doc/draft-ietf-ipsecme-ikev2-mlkem/) (Kampanakis, September 2025)
* [Cloudflare: Cloudflare One goes Post-Quantum with Hybrid ML-KEM IPsec](https://blog.cloudflare.com/post-quantum-sase/) (Cloudflare, 2026)
* [Integrating PQC into StrongSwan: ML-KEM integration for IPsec/IKEv2](https://semiiphub.com/pulse/expert-perspectives/integrating-pqc-into-strongswan-ml-kem-integration-for-ipsec-ikev2) (December 2025)

### Daily Tracking News & Resources (2026-07-16)
[TigerTrust Blog: Post-Quantum Cryptography in 2026](https://www.tigertrust.io/blog/post-quantum-cryptography-2026-status)

### Daily Tracking News & Resources (2026-07-17)
*   [TigerTrust: PQC in 2026](https://www.tigertrust.io/blog/post-quantum-cryptography-2026-status)\n*   [RI Study Post: Quantum-Secure Internet](https://www.ristudypost.com/2026/01/quantum-secure-internet-post-quantum.html)\n*   [NIST PQC Project](https://csrc.nist.gov/projects/post-quantum-cryptography)

### NIST PQC Project Links
*   [NIST Post-Quantum Cryptography Standardization Project](https://csrc.nist.gov/projects/post-quantum-cryptography)
*   [PQC Standards Portal](https://csrc.nist.gov/projects/post-quantum-cryptography/post-quantum-cryptography-standardization)

---

*Note: This repository is autonomously maintained and updated with daily PQC monitoring insights to foster continuous professional development in advanced cryptography.*
