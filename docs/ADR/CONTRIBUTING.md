Thank you for your interest in contributing to the Small-Scale Security Operations Center (SOC) Simulation Project! This project replicates the workflow of a junior cybersecurity analyst by building a virtual SOC environment with a SIEM, endpoint agents, and simulated security incidents.

The goal is to create an open, educational lab environment for practicing detection, analysis, and incident response.



We welcome contributions in the following areas:

Documentation: Setup guides, troubleshooting steps, playbooks, or attack simulation walkthroughs.

Detection Rules: Writing and testing custom Wazuh/Security Onion rules for identifying suspicious activity.

Log Sources: Adding new endpoints or data sources (Windows/Linux logs, firewall, IDS/IPS).

Attack Simulations: Safe, reproducible simulations (Nmap scans, brute force attempts, EICAR test file).

Incident Response: Drafting and improving IR Playbooks and reporting templates.

Dashboards & Reports: Improving SIEM visualizations and metrics for better analysis.





Development Guidelines

Virtualization: UTM on macOS is the standard environment. Contributions should be compatible with this setup.

SIEM Platform: Use Wazuh or Security Onion (specify version when contributing).

Endpoints: Windows (10/11 Evaluation) and Ubuntu Linux are the supported endpoint types.

Safe Testing: Only use safe tools (Nmap, EICAR, custom scripts). No live malware or dangerous payloads.

Code & Rules: Use clear naming conventions, add inline comments, and document test cases.



Fork the Repository

Fork this repo to your own GitHub account.

Create a Branch

Use descriptive branch names:

feature/new-detection-rule

docs/update-playbook

bugfix/networking-config

Make Your Changes

Follow the guidelines above.

Include screenshots or test results where relevant (especially for SIEM rules or incident reports).

Submit a Pull Request (PR)

Explain what you changed and why.

Include test steps so others can reproduce your results.


All contributors are expected to:

Be respectful and professional.

Keep contributions safe, legal, and reproducible.

Share knowledge clearly (assume others may be new to cybersecurity).

Avoid uploading binaries, large VM files, or anything unsafe.



We are especially looking for help with:

Advanced attack simulation scenarios.

Expanding SIEM dashboards.

Incident correlation and alert tuning.

Integrating additional open-source tools into the SOC lab.


If you have questions about contributing:

Open a GitHub Issue with the label question.

Or contact the project maintainer directly.

We’re excited to build this SOC Simulation project together—thank you for contributing!






ADR-001: Choice of SIEM Platform

Date: 2025-09-08
Status: Accepted
Context:
The SOC Simulation project requires a SIEM (Security Information and Event Management) solution that can:

Run efficiently on a MacBook using UTM virtualization.

Support multiple endpoint agents (Windows/Linux).

Allow for custom rule creation, alerting, and log analysis.

Be free and open-source to ensure accessibility.

Two main options were considered:

Security Onion – A full-featured SOC-in-a-box platform (includes Suricata, Zeek, TheHive, Kibana).

Wazuh – A lightweight SIEM with strong endpoint monitoring, flexible agent deployment, and log analysis.

Decision:
We chose Wazuh as the SIEM platform.

Rationale:

Wazuh has a smaller resource footprint than Security Onion, making it more suitable for UTM and MacBook hardware limitations.

Easier to deploy and configure agents on both Windows and Linux endpoints.

Strong built-in detection capabilities with the ability to write custom rules.

Good web interface (Kibana/Opensearch dashboards) for analysis and visualization.

Consequences:

Some advanced features available in Security Onion (e.g., Zeek network analysis, built-in case management) will not be present.

Future scalability may require migrating to a heavier SIEM solution if more advanced correlation is needed.

Documentation and training will be focused around Wazuh rather than Security Onion.

