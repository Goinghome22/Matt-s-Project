Observability & Logging: Project Notes (Syslog-NG Edition)

This document tracks my implementation of observability and centralized logging using syslog-ng. It covers health checks, log generation, testing, and future monitoring integration.

1. Health Check Endpoint

Have you implemented a health-check endpoint?
(Replace [ ] with [x])

 Yes

 No

 Not applicable to my project

Your endpoint path:
Example: /health, /status, /api/v1/status

# Sample output (if applicable):
{
  "status": "ok",
  "uptime": "3600s",
  "version": "1.0.0"
}


Why is this useful?

The health-check endpoint lets me verify that my service is running properly before sending logs to syslog-ng. It ensures the system is responsive and that my log forwarding setup is only active when the service is healthy.

2. Health Check Test

Did you write a test for the health-check endpoint?

 Yes

 No

Paste your test code or describe your test method:

# Example in Python (FastAPI + pytest)
def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


This test helps confirm that my logging pipeline only processes data when the application is running correctly.

3. Log Event or Metric (via Syslog-NG)

Name of log event or metric:
Example: "failed_login", "firewall_alert", "system_health_heartbeat"

What triggers this?

Example: Every failed authentication attempt or every time the system heartbeat signal is sent to syslog-ng.

Sample syslog-ng formatted log:

<13>1 2025-11-04T19:12:05Z server1 appname 1234 ID47 [meta sequenceId="1"] event="unauthorized_attempt" ip="192.168.1.50" severity="warning"


Where is this implemented in your system?
Example: /etc/syslog-ng/conf.d/auth-logs.conf → handles logs from the authentication module.

How syslog-ng processes it:

The syslog-ng configuration filters these logs based on facility and severity, then routes them to /var/log/auth-events.log or a remote log collector (e.g., @192.168.1.200:514).

4. Optional Monitoring Tools

Did you use any monitoring or visualization tools (Grafana, Kibana, etc.)?

 Yes

 No

Tool name(s):
Example: Kibana connected to Elasticsearch receiving syslog-ng data.

Screenshot or description:

# Example description:
Dashboard displays real-time syslog-ng streams, error rates, and categorized security events.


syslog-ng integration details:

Syslog-ng forwards logs to my ELK (Elasticsearch, Logstash, Kibana) stack using a TCP destination. This setup allows visualization of system events and security alerts.

5. Reflection & Learning

What did you learn while implementing observability with syslog-ng?

I learned how syslog-ng can act as a powerful central hub for collecting and routing logs from multiple sources. It made it easier to analyze patterns and detect anomalies across systems.

Anything you would do differently or improve in the future?

I would set up log rotation and severity-based filtering to reduce noise, and configure syslog-ng to forward critical logs to an external alerting tool for real-time notifications.

✅ Next Steps / TODOs

 Add remote destination for syslog-ng logs.

 Enable TLS for secure log transmission.

 Integrate with visualization tool (e.g., Kibana or Loki).

 Create custom filters for specific security events.