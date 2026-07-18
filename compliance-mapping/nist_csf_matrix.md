# NIST CSF 2.0 Control Mapping Matrix & SCES Framework

This directory outlines the governance and compliance mapping layer of the validation framework. It translates technical system telemetry into audit-ready evidence aligned with NIST CSF 2.0 core functions.

## 📊 Technical Control Mapping

| NIST CSF 2.0 Subcategory | Technical Control (SIEM) | Validation Method (Caldera) | Compliance Evidence Log |
| :--- | :--- | :--- | :--- |
| **PR.DS-01** (Data-at-rest is protected) | Wazuh File Integrity Monitoring (FIM) on system binaries | Unauthorized file modification simulation | Real-time syscheck alert log generation with cryptographic hash changes |
| **DE.AE-0002** (Anomalous activity is analyzed) | Custom Wazuh Ruleset (Rule ID 100001) | Multi-stage brute-force adversary profile | SSH/Auth log threshold breach alert triggering active response |
| **RS.MI-01** (Incidents are mitigated) | Python Active Response Script (IP blocking triggers) | Automated privilege escalation / connection attempt | Firewall drop action log with zero-second mitigation timestamp |

## 📐 Security Control Effectiveness Score (SCES) Model

The Security Control Effectiveness Score (SCES) is a quantitative metric engineered to measure compliance degradation and control drift across Cloud-IoT environments.

### Scoring Logic
The baseline effectiveness of each targeted NIST subcategory is calculated mathematically using three core operational parameters:
1. **Detection Triage Time ($T_d$):** Time elapsed between adversary emulation trigger and SIEM alert generation.
2. **Mitigation Execution ($M_e$):** Binary verification (1 or 0) indicating whether automated active response succeeded.
3. **Log Fidelity ($L_f$):** Verification that cryptographic audit trails maintained absolute chain of custody.

### Operational Utility
By tracking this score dynamically, security operations teams can move away from static, manual yearly check-lists and transition into a continuous compliance model where architectural drift or rule misconfigurations are flagged instantly.
