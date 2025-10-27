learning/PLAN.md

This is my one-page learning plan for the month. I will complete and commit this file during the 15-minute selection clinic. It records the technology I chose to learn, why I chose it for my capstone, the three focused tasks I will complete, and the proof I will capture to show I did the work.

Student commitment

Name: Matthew Rich

Date created: 2025-10-27

I commit to treat this plan as my personal roadmap: I will keep dates realistic, finish each small task, capture evidence of success, and update this file if anything changes.

Chosen technology

Technology name: Syslog‑ng

Technology version (if applicable): 4.6 (or latest stable version)

Why I chose this technology

Syslog‑ng will allow me to aggregate logs from multiple sources — firewalls, web servers, and IDS systems — and forward them to Wazuh for centralized monitoring. This will enable me to verify log collection, parsing, and dashboard alerts in Wazuh for my capstone project.

First-day actions (complete in the 15-minute selection clinic)

Finalize the Chosen technology and Why I chose this technology fields above.

Draft three small integration tasks below with realistic start and target completion dates.

Commit this file to the repository at learning/PLAN.md before the end of the 15-minute clinic.

Record where I will start Task 1 (for example: local branch name or workspace folder) under Task 1.

If a task feels too large, I will make it smaller and update the dates here.

My three integration tasks (small, testable, dated)

Task 1 — Install and configure Syslog‑ng

Description: Install Syslog‑ng on the central log server and configure basic sources and destinations to forward logs to Wazuh.

Start date: 2025-10-27

Target completion date: 2025-10-29

Success criterion (explicit): Syslog‑ng successfully starts and forwards a sample log file to Wazuh.

Proof method (what I will capture to show success): Screenshot of Syslog‑ng status and sample log appearing in Wazuh dashboard.

Where I will start Task 1: Local branch feature/syslog-ng-install

Task 2 — Forward firewall and web server logs

Description: Configure Syslog‑ng to collect firewall logs (e.g., pfSense) and web server logs (Apache/Nginx) and forward them to Wazuh.

Start date: 2025-10-30

Target completion date: 2025-11-03

Success criterion (explicit): Logs from both firewall and web server appear in Wazuh and match expected formats.

Proof method (what I will capture to show success): Screenshots of Wazuh dashboard showing firewall and web server logs; sample log entries saved in learning/README.md.

Task 3 — Forward IDS logs and verify dashboards

Description: Configure Syslog‑ng to collect IDS logs (Snort/Suricata) and verify all log sources appear correctly in Wazuh dashboards.

Start date: 2025-11-04

Target completion date: 2025-11-08

Success criterion (explicit): IDS alerts appear in Wazuh and correlate with firewall/web logs as expected.

Proof method (what I will capture to show success): Screenshot of Wazuh dashboard showing IDS alerts and combined log sources; note any successful alerts or events in learning/README.md.

Risks, assumptions, and blockers (one-line each)

Requires access to firewall, web server, and IDS logs.

Needs Wazuh manager running and reachable from Syslog‑ng server.

May need custom decoders in Wazuh if logs have non-standard formats.

My weekly timeline (one-line plan)

Week 1: Commit this PLAN and start Task 1.

Week 2: Continue Task 1; produce a test log and capture in dashboard; start Task 2.

Week 3: Continue Task 2; ensure logs appear correctly in Wazuh; start Task 3.

Week 4: Complete Task 3; finalize proof screenshots and notes; draft learning/README.md and learning/REFLECTION.md.