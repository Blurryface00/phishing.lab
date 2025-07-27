from mailslurp_client import Configuration, ApiClient, SendEmailOptions
from mailslurp_client.api import InboxControllerApi, EmailControllerApi

API_KEY = "ee21579c10a9b34ce799b189d1a25225d3c9b2b01521c0cee8d79d562adf791"

configuration = Configuration()
configuration.api_key["x-api-key"] = API_KEY

with ApiClient(configuration) as api_client:
    inbox_api = InboxControllerApi(api_client)
import smtplib
from email.mime.text import MIMEText

# Email content
msg = MIMEText("Click here to reset your password: http://phishlab.fake/reset")
msg['Subject'] = "⚠️ Urgent: Password Expiry"
msg['From'] = "jamessimpnut@gmail.com"
msg['To'] = "jamessimpnutgmail.com@jamessimpnutgmail.onmicrosoft.com"

# SMTP config
smtp_server = "smtp.gmail.com"
smtp_port = 587
username = "jamessimpnut@gmail.com"
password = "mfaeepichdlavdky"

# Send the email
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(username, password)
    server.send_message(msg)

print("✅ Phishing email sent using Gmail SMTP.")
