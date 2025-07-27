import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from_address = "security@outlook.com"
to_address = "Yonny@jamessimpnutgmail.onmicrosoft.com"
subject = "Account Verification Required"
body = """\
We detected unusual login activity. Please verify your account here:
https://6a7183595663.ngrok-free.app
"""
# Compose email
msg = MIMEMultipart()
msg["From"] = from_address
msg["To"] = to_address
msg["Subject"] = subject

msg.attach(MIMEText(body, "plain"))

# Gmail SMTP
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = "jamessimpnut@gmail.com"
smtp_password = "mfaeepichdlavdky"
# Send
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(smtp_username, smtp_password)
server.sendmail(from_address, to_address, msg.as_string())
server.quit()

print("Email sent!")
