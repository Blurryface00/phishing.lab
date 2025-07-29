🧪 Phishing Simulation Lab (Microsoft Defender + Sentinel)

This project simulates a phishing attack scenario using Gmail SMTP and Microsoft Defender for Endpoint (Plan 2), integrated with Microsoft Sentinel for alert detection and incident response.

> 💡 Built and tested in a hybrid home lab with Parrot OS, Azure VM, and Microsoft 365 Business Premium.

---

## 🎯 Objectives

- Simulate a phishing email campaign
- Deliver a clickable phishing link via Gmail SMTP
- Detect the activity using Defender for Endpoint
- Forward telemetry and alerts to Microsoft Sentinel
- Trigger custom detection rules and automated incident response

---

## 🛠 Tools & Tech

| Tool                         | Role                                 |
|------------------------------|--------------------------------------|
| Parrot OS (VM)              | Attacker machine (email sender)      |
| Python 3                    | Phishing script via Gmail SMTP       |
| Azure VM (Windows Server)   | Victim endpoint onboarded to Defender|
| Microsoft Defender for Endpoint (P2) | Threat detection & telemetry    |
| Microsoft Sentinel          | SIEM for detection rules and response|
| GitHub                      | Backup and version control           |

---

## 💻 Lab Setup

1. *Created phishing script* (phishing_email.py) in Python using Gmail SMTP
2. *Sent phishing email* to jason@kasoagees.onmicrosoft.com with link to example.com
3. *Onboarded VM* to Microsoft Defender (Plan 2)
4. *Connected Defender to Sentinel*
5. *Created KQL rule* in Sentinel for DeviceNetworkEvents
6. *Built detection rule* to auto-trigger incidents

---

## 🔍 MITRE ATT&CK Mapping

| Tactic         | Technique                        |
|----------------|----------------------------------|
| Initial Access | [T1566.001] Spearphishing Link   |

---

## 📸 Screenshots

| Step                   | Screenshot |
|------------------------|------------|
| Email received         | 📎 IMG_... |
| Link clicked           | 📎 IMG_... |
| Sentinel rule created  | 📎 IMG_... |
| Defender alert fired   | 📎 IMG_... |

---

## 🚨 Sample Detection KQL

```kql
DeviceNetworkEvents
| where RemoteUrl contains "example.com"
| project TimeGenerated, DeviceName, RemoteUrl, InitiatingProcessAccountName
