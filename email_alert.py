import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

SENDGRID_API_KEY = "DIN_SENDGRID_API_NYCKEL"
RECIPIENT_EMAIL = "mottagare@example.com"
SENDER_EMAIL = "avsändare@example.com"

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
    except Exception as e:
        print(f"Misslyckades med att skicka e-post: {str(e)}")
