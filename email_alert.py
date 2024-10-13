import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from logger import Logger
from dotenv import load_dotenv

# Ladda miljövariabler från .env-filen
load_dotenv()

email_logger = Logger()

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")
SENDER_EMAIL = os.getenv("SENDER_EMAIL")

def send_email_alert(message):
    try:
        email = Mail(
            from_email=SENDER_EMAIL,
            to_emails=RECIPIENT_EMAIL,
            subject="Larm aktiverat i övervakningsapplikationen",
            plain_text_content=message,
        )
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(email)
        print(f"E-post skickat med statuskod {response.status_code}")
        email_logger.log(f"E-post skickat med statuskod {response.status_code}")
    except Exception as e:
        print(f"Misslyckades med att skicka e-post: {str(e)}")
        email_logger.log(f"Misslyckades med att skicka e-post: {str(e)}")
