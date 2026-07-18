├── README.md                  # Main project landing page, architecture, and scoring engine
├── LICENSE                    # Repository distribution license (e.g., MIT or Apache 2.0)
├── config/
│   ├── localstack/            # Docker compose and container setup files
│   │   └── docker-compose.yml
│   ├── caldera/               # MITRE Caldera adversary profiles and custom YAML abilities
│   │   ├── profiles/
│   │   └── abilities/
│   └── wazuh/                 # SIEM decoders, custom XML rules, and auditd configurations
│       ├── decoders/
│       ├── rules/
│       └── audit.rules
├── src/
│   ├── analytics/             # Python or R scripts implementing the SCES mathematical model
│   │   └── sces_calc.py
│   └── testbed/               # Network provisioning scripts and promiscuous mode helpers
│       └── set_promisc.sh
└── docs/                      # Thesis documentation, matrices, and supplementary data
    ├── test_matrix.csv
    └── architecture_schematic.png
