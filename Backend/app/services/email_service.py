import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")


def send_email(to_email:str , subject:str , body:str):
    try:
        msg = MIMEText(body)
        msg["subject"] = subject
        msg["from"] = EMAIL
        msg["To"] = to_email

        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(EMAIL,PASSWORD)

        server.sendmail(EMAIL,to_email,msg.as_string())
        server.quit()

        print("Email sent successfully")
    except Exception as e:
        print("email sending failed",e)    