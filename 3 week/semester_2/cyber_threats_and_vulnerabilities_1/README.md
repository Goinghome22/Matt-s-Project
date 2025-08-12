# Module: Cyber Threats and Vulnerabilities

Analyze service enumeration and vulnerability indicators.

## Key Artifact
- `juice_scan.txt`: Nmap scan of OWASP Juice Shop with default vuln scripts

## What to Look For
- Open ports and identified services/versions
- Reported CVEs or vulnerable configurations
- Enumerated endpoints that suggest admin panels or exposed apps

## Suggested Workflow
1. Skim header to confirm scan command and target
2. Identify top services (e.g., 80/tcp, 21/tcp) and versions
3. Note any CVEs flagged and read references
4. Propose next steps (e.g., targeted scans, auth brute-force prevention, patching)

## Optional CLI Aids
```bash
# Ports summary
awk '/^PORT/{p=1; next} p && NF==7{print $1, $2, $3, $4}' juice_scan.txt | head -n 20

# CVE mentions
grep -n "CVE-" juice_scan.txt | head -n 20
```

## Outcomes
- Translate scan output into actionable investigation and remediation items. 

## Direct Links
- [juice_scan.txt](./juice_scan.txt)
- [Vulnerability Scan Report.pdf](./%F0%9F%94%8D%20Vulnerability%20Scan%20Report.pdf)
- [Risk Management Report.pdf](./Risk%20Management%20Report.pdf)
- [Risk Register.xlsx](./Risk%20Register.xlsx)

## Assessment / Rubric
- ✅ High-risk services and CVEs correctly prioritized
- ✅ Proposed follow-up scans/tests make sense for findings
- ✅ Clear remediation recommendations

## Next Steps
- Run targeted scans (e.g., `nmap -sV -p <ports>`)
- Validate CVE applicability (version, config, exploitability)
- Draft patching/mitigation plan and verification steps 