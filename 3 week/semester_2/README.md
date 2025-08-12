# 3-Week • Semester 2 — Security, Python, and SOC

Hands-on security practice with scan artifacts, risk documentation, and Python scripting.

## Modules and Materials

- Cybersecurity Basics (`cybersecurity_basics_1`)
  - Artifacts: Risk reports, registers, and scan documents.
  - Outcome: Understand foundational security concepts and documentation.

- Cyber Threats and Vulnerabilities (`cyber_threats_and_vulnerabilities_1`)
  - Artifact: `juice_scan.txt` (Nmap scan of OWASP Juice Shop with default vuln scripts).
  - Outcome: Read port/service enumeration, correlate to common CVEs, identify next steps.

- Python (`python_1`)
  - Project: `FileIntegrityMonitor/` — monitors file changes by hashing contents over time.
  - Files:
    - `file_integrity_monitor.py`
    - `example_file.txt`
    - `file_integrity_report.txt` (created after runs)

- Security Operations Center (`security_operations_center_1`)
  - Artifacts: SOC reports and vulnerability/risk documentation.
  - Outcome: Exposure to SOC deliverables and triage thinking.

## Running the File Integrity Monitor

Requirements: Python 3

1. cd into the module folder:
   ```bash
   cd "python_1/FileIntegrityMonitor"
   ```
2. (Optional) Edit `file_integrity_monitor.py` to set `file_to_monitor` to a target file path.
3. Run the script:
   ```bash
   python3 file_integrity_monitor.py
   ```
4. Review output in the console and `file_integrity_report.txt`.

## Outcomes

- Ability to interpret basic scan outputs, connect findings to risk, and automate small checks with Python. 