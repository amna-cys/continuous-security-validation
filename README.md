# Continuous Security Control Validation Framework

This repository hosts the experimental implementation, configuration files, and quantitative scoring data for the master's thesis: **Continuous Security Control Validation: An Automated Adversary Emulation Framework for Evaluating NIST CSF 2.0 Compliance in Cloud-Integrated IoT Environments**.


## Abstract
Static compliance checklists fail to secure dynamically reconfigured cloud-integrated IoT gateways. This framework introduces an automated adversary emulation model directly aligned with the Govern, Protect, and Detect capabilities of the NIST CSF 2.0 standard. 

The physical environment uses two independent machines to eliminate hypervisor loopback resource bias. Physical PC 1 runs a centralized Wazuh SIEM virtual machine alongside a control validation VM hosting the MITRE Caldera engine and containerized LocalStack. Physical PC 2 runs an isolated target Ubuntu IoT gateway virtual machine. 

The framework converts raw kernel system calls and user-space events into uniform out-of-band telemetry logs across four distinct threat campaigns. These logs are processed through the Security Control Effectiveness Score (SCES) mathematical model. Phase 1 execution established a baseline score of 88.00% across a 67-atomic-action matrix, isolating 60 alerts and 7 user-space escapes. Controlled configuration drift via a firewall policy flush during Phase 2 degraded the network pivot domain efficiency to 86.67% over a 14-day observation window, demonstrating the model's ability to measure and track posture decay.

---

## Hardware and Virtualization Architecture

The framework requires two independent physical machines connected via an out-of-band Layer-2 managed hardware switch. This setup eliminates single-host processing and resource contention biases.

### Host Node 1: Control & Monitoring Plane
* **Hardware:** Intel Core i9-12900 CPU @ 2.40 GHz, 16 GB physical RAM
* **Base OS:** Ubuntu 22.04 LTS
* **Virtual Machines (Oracle VM VirtualBox):**
  * **Wazuh SIEM Manager VM:** 8,707 MB base memory allocation.
  * **Control Validation Hub VM:** 4,096 MB base memory, 3 vCPUs. Runs MITRE Caldera Server v5.0+ and LocalStack Pro inside a Docker container (intercepting API calls on Port 4566 with `ENFORCE_IAM=1`).

### Host Node 2: Target Platform
* **Hardware:** Intel Core i9-12900 CPU @ 2.40 GHz, 16 GB physical RAM
* **Base OS:** Ubuntu 22.04 LTS
* **Virtual Machine:**
  * **IoT Gateway Target VM:** 6,144 MB base memory, 3 vCPUs, capped at 60% execution limits. Runs a user-space Wazuh Agent masqueraded under the process name `splunkd` (PID: 9019). Kernel system calls are hooked using Linux `auditd` with a buffer queue set to `-b 8192`.

---

## Adversary Emulation & Threat Campaigns

The framework automates 12 specific tactical techniques across 4 distinct operational profiles ($n=4$) using the MITRE Caldera engine.

### OP_01: NIST_Identify_Discover (Discovery & Local Asset Harvesting)
* **Objective:** Validates NIST CSF 2.0 Category DE.CM-03.
* **Techniques:** Sensitive file path scanning (T1083), local SSH credential hunting (T1552.004), and shell history parsing (T1552.003).

### OP_02: NIST_Cloud_Pivot (Cross-Domain Cloud Integration Pivot)
* **Objective:** Validates NIST CSF 2.0 Category DE.AE-02.
* **Techniques:** AWS credential cache scanning (T1552.001), local cloud resource enumeration via Stratus Red Team (T1580), and storage bucket object discovery hitting LocalStack (T1619).

### OP_03: NIST_Network_Pivot (Local Subnet Internal Reconnaissance)
* **Objective:** Validates NIST CSF 2.0 Category DE.CM-01.
* **Techniques:** Internal network port scanning (T1046), network interface extraction (T1016), and neighbor host ARP sweeps (T1018).

### OP_04: NIST_Evasion_Tester (Anti-Forensics & Sensor Blinding)
* **Objective:** Validates NIST CSF 2.0 Category DE.CM-03 and PR.PT-01.
* **Techniques:** Binary padding via `dd` tool stream modifications (T1027.001), file permission manipulations via `chmod` (T1222.002), timestomping metadata alterations via `touch` (T1070.006), and user-space logging daemon termination via `systemctl stop wazuh-agent` (T1562.001).

---

## Quantitative Evaluation: SCES Framework

The technical security posture is calculated dynamically through the Security Control Effectiveness Score (SCES) mathematical engine. The model aggregates telemetry parameters across the evaluation categories.

### Formula
The composite posture score is defined as:

$$SCES = \sum_{i=1}^{n} w_{i} \cdot EV_{i}$$

Where:
* $n$: Total number of distinct evaluation domains assessed ($n = 4$).
* $i$: Active operational campaign evaluation index.
* $w_{i}$: Gravity weight coefficient assigned to prioritize domain $i$.
* $EV_{i}$: Operational Effectiveness Value of the active defenses within domain $i$.

### Constraints
To maintain mathematical integrity and prevent high-frequency alert masking, the gravity coefficients are bound to unity:

$$\sum_{i=1}^{n} w_{i} = 1.00$$

This validation engine enforces a uniform weight allocation model where each domain receives an equal coefficient:

$$w_{i} = 0.25$$

### Empirical Experimental Results

| Phase | Operational Status | Successful Alerts Generated | User-Space Process Escapes | Final SCES Score |
| :--- | :--- | :--- | :--- | :--- |
| **Phase 1** | Controlled Experimental Baseline | 60 | 7 | **88.00%** |
| **Phase 2** | 14-Day Configuration Drift (Firewall Flush) | 52 | 15 | **86.67%** |

---

## Setup Instructions

### 1. Configure Host Interfaces
Execute this script on both physical nodes to force network interfaces into promiscuous mode, preserving out-of-band Layer-2 frame routing:
```bash
sudo ip link set dev eth0 promiscuous on
