Mini-Tutorial: Using syslog-ng to Collect and Forward Logs

A student-authored tutorial documenting a key integration learned in Semester 5.

❓ What This Teaches

This tutorial explains how to use syslog-ng as a log collector to receive, process, and forward logs from devices such as pfSense firewalls, Linux servers, or applications.
Syslog-ng solves the problem of centralized logging—allowing security teams to gather logs in a single location instead of checking each device individually. Any cybersecurity or monitoring project benefits from this because it improves threat detection, auditing, and incident response.

🎯 Use Case

What real-world need or job scenario does this apply to?

 Backend development

 Cybersecurity

 Monitoring / Observability

 Performance / Testing

 Authentication / Authorization

 DevOps / Deployments

 Other: log forwarding

🚀 Quick Setup / Install

Minimal installation on Ubuntu/Debian:

sudo apt update
sudo apt install syslog-ng


Main config file:

/etc/syslog-ng/syslog-ng.conf

🛠️ Step-by-Step Guide
1. Create a Log Source (How syslog-ng receives logs)
sudo nano /etc/syslog-ng/syslog-ng.conf


Add:

source s_network {
    network(
        ip("0.0.0.0")
        port(514)
        transport("udp")
    );
};

2. Create a Destination (Where logs go)

Save locally:

destination d_logs {
    file("/var/log/remote_logs.log");
};


Or forward to Wazuh:

destination d_wazuh {
    network(
        "192.168.X.X"
        port(514)
        transport("udp")
    );
};

3. Connect Source → Destination
log {
    source(s_network);
    destination(d_logs);
    # or destination(d_wazuh);
};

4. Restart syslog-ng
sudo systemctl restart syslog-ng
sudo systemctl status syslog-ng

✅ What You Should See

Check for logs arriving:

tail -f /var/log/remote_logs.log


Example:

Nov 12 13:21:44 pfsense firewall: port 443 connection attempt blocked
Nov 12 13:21:45 ubuntu sshd[2022]: Failed password for root from 10.0.0.5


Screenshot example:

![Syslog-ng Proof Screenshot](../PROOF/syslog-ng-output.png)

💡 Pro Tips / Edge Cases

Port 514 must be open on firewalls

UDP = fast but not encrypted

Check /var/log permissions if file doesn’t generate

📚 Learn More

Syslog-ng Docs — https://www.syslog-ng.com/technical-documents/list/syslog-ng-open-source-edition/

Syslog RFC 5424 — https://datatracker.ietf.org/doc/html/rfc5424

pfSense Remote Syslog — https://docs.netgate.com/pfsense/en/latest/monitoring/logs/remote-syslog.html

👤 Authored by: Matthew Rich

🗓️ Date: 2025-11-13
🔁 Validated by: [Instructor Name]