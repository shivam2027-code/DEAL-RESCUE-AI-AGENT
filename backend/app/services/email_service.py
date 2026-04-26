import smtplib
from email.mime.text import MIMEText
from app.core.config import getAppConfig

config = getAppConfig()

EMAIL = config.email
PASSWORD = config.password


def send_email(to_email: str, subject: str, body: str):
    try:
        msg = MIMEText(body)
        msg["subject"] = subject
        msg["from"] = EMAIL
        msg["To"] = to_email

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(EMAIL, PASSWORD)

        server.sendmail(EMAIL, to_email, msg.as_string())
        server.quit()

        print("Email sent successfully")
    except Exception as e:
        print("email sending failed", e)