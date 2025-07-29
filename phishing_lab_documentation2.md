# 🛡️ Microsoft Defender & Sentinel Phishing Simulation Lab Documentation
**Date:** July 27, 2025
---
## 🔧 Lab Overview
- **Project:** Simulate phishing attack, detect in Microsoft Defender, correlate in Sentinel, and respond automatically.
- **Environment:**
  - Azure VM (`Windowlogdemo`)
  - Windows Server 2019 (Standard B2s)
  - Parrot OS (VM on spare laptop)
  - Microsoft 365 Business Premium tenant (`kasoa.gees`)
---
## ✅ Completed Steps
### 1. Azure VM Setup
- Created VM: `Windowlogdemo`
- Resized to: `Standard B2s` for better performance
- Verified public IP and RDP working

### 2. Defender for Endpoint Onboarding
- Downloaded onboarding script from Microsoft 365 Defender portal
- RDP’d into VM
- Ran script via Admin Command Prompt from Desktop
- Successfully onboarded VM (verified in [security.microsoft.com/devices](https://security.microsoft.com/devices))

### 3. Attack Machine Configuration (Parrot OS)
- Set up virtual environment: `phishing_env`
- Installed MailSlurp Python SDK with `pip install mailslurp-client`
- Created phishing script using authenticated MailSlurp API
- Switched to Gmail SMTP for final email delivery
- Debugged issues like non-breaking spaces, syntax, and API key errors

### 4. Phishing Email Delivery
- Sent email from Gmail SMTP to `jason@kasoagees.onmicrosoft.com`
- Subject: `Urgent: Password Expiry`
- Body contained: `http://phishlab.fake/reset-password` and later `http://example.com/reset`
- Email received in Outlook Web → Junk folder
- Clicked link from the VM browser

### 5. Defender for Endpoint Plan 2 Upgrade
- Upgraded license to Microsoft Defender for Endpoint Plan 2
- Gained access to Device Timeline, Advanced Hunting, and Unified SIEM integration

### 6. Sentinel Integration and Detection
- Connected Microsoft Defender XDR to Microsoft Sentinel
- Enabled data connectors: `SecurityAlert`, `DeviceNetworkEvents`, `AlertEvidence`, etc.
- Created scheduled Analytics Rule with MITRE tactic `Initial Access`
- Detection rule triggered via simulated phishing click

### 7. Final Validation
- Confirmed `DeviceEvents`, `DeviceNetworkEvents`, and `SecurityAlert` logs in Sentinel
- Adjusted rule to detect real DNS-resolving domain clicks (e.g. `example.com`)
- Rule ran every 5 minutes, scanned 1 hour of logs

---
## 🛠 Files Created in Lab
- `phishing_email.py` – Python script using Gmail SMTP
- `phishing_requirements.txt` – pip requirements for phishing script
- `phishing_lab_backup.zip` – full environment backup
- `phishing_lab_documentation.md` – this documentation file

---
## 🧠 MITRE ATT&CK Mapping
| Tactic         | Technique                        |
|----------------|----------------------------------|
| Initial Access | [T1566.001] Spearphishing Link   |

---
## 🔁 Final Pause State
- ✅ Rule created and running in Sentinel
- ✅ Defender telemetry confirmed in `DeviceEvents`
- ✅ Email sent and clicked successfully
- ✅ Documentation and script uploaded to GitHub
- ❌ No automated playbook yet (next phase)
- ❌ No Logic App integration (optional)

---
## 🧭 Next Steps (Round 2 Ideas)
- Simulate malware drop or suspicious file write
- Run Defender quick/advanced scan from Sentinel
- Build Logic App to notify or isolate device
- Enable email header analysis and Safe Links inspection
---
📄 Documentation generated live with ChatGPT (Assistant) and user screenshots + terminal logs.