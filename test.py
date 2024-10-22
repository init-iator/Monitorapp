import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from logger import Logger
from dotenv import load_dotenv, find_dotenv, set_key
from textdecor import textdec

txd = textdec()

class EmailManager:
    def __init__(self):
        """
        Tom konstruktionsmetod för EmailManager-klassen.
        """
        pass

    def send_email_alert(self, message):
        """
        Skickar ett e-postmeddelande med ett givet meddelande.
        """
        try:
            # Ladda miljövariabler
            load_dotenv(".env", override=True)
            SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
            RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")
            SENDER_EMAIL = os.getenv("SENDER_EMAIL")

            email_logger = Logger()

            # Skapar ett e-postmeddelande med avsändare, mottagare, ämne och innehåll
            email = Mail(
                from_email=SENDER_EMAIL,
                to_emails=RECIPIENT_EMAIL,
                subject="Larm aktiverat i övervakningsapplikationen",
                plain_text_content=message,
            )
            # Skapar en klient för att skicka e-post via SendGrid
            sg = SendGridAPIClient(SENDGRID_API_KEY)
            # Skickar e-postmeddelandet och loggar statuskoden
            response = sg.send(email)
            print(f"E-post skickat med statuskod {response.status_code}")
            email_logger.log(f"E-post skickat med statuskod\t|{response.status_code}|")
        except Exception as e:
            # Fångar och loggar eventuella fel som uppstår under e-postsändningen
            print(f"Misslyckades med att skicka e-post: {str(e)}")
            email_logger.log(f"Misslyckades med att skicka e-post:\t|{str(e)}|")

    def create_or_update_env_file(self):
        """
        Skapar eller uppdaterar en .env-fil med användarens inmatade värden.
        """
        dotenv_path = find_dotenv()

        if dotenv_path:
            load_dotenv(dotenv_path)
            print(f"{txd.GREEN}Hittade en befintlig .env-fil med följande innehåll:{txd.END}")
            print(f"{txd.BLUE}SENDGRID_API_KEY{txd.END}={os.getenv('SENDGRID_API_KEY')}")
            print(f"{txd.BLUE}RECIPIENT_EMAIL{txd.END}={os.getenv('RECIPIENT_EMAIL')}")
            print(f"{txd.BLUE}SENDER_EMAIL{txd.END}={os.getenv('SENDER_EMAIL')}")

            confirm = input(f"Stämmer ovanstående information? ({txd.GREEN}ja{txd.END}/{txd.RED}nej{txd.END}): ")
            if confirm.lower() == "ja":
                print(f"{txd.BOLD}{txd.YELLOW}.env-filen har lästs in.{txd.END}{txd.END}")
            elif confirm.lower() == "nej":
                sendgrid_api_key = input("Ange SendGrid API-nyckel: ")
                recipient_email = input("Ange mottagarens e-postadress: ")
                sender_email = input("Ange avsändarens e-postadress: ")

                set_key(dotenv_path, "SENDGRID_API_KEY", sendgrid_api_key)
                set_key(dotenv_path, "RECIPIENT_EMAIL", recipient_email)
                set_key(dotenv_path, "SENDER_EMAIL", sender_email)
                print(f"{txd.BOLD}{txd.YELLOW}.env-filen har uppdaterats. {txd.RED}STARTA OM PROGRAMMET!{txd.END}{txd.END}{txd.END}")
            else:
                os.system("cls" if os.name == "nt" else "clear")
                print(f"{txd.YELLOW}Felaktigt val, skriv {txd.GREEN}ja{txd.END}{txd.YELLOW} eller {txd.RED}nej{txd.END}{txd.YELLOW}.{txd.END}")
                self.create_or_update_env_file()
        else:
            print(f"{txd.BOLD}{txd.YELLOW}.env-fil hittades inte, skapa en ny{txd.END}{txd.END}")
            sendgrid_api_key = input("Ange SendGrid API-nyckel: ")
            recipient_email = input("Ange mottagarens e-postadress: ")
            sender_email = input("Ange avsändarens e-postadress: ")
            print(f"{txd.BOLD}{txd.YELLOW}.env-filen har uppdaterats. {txd.RED}STARTA OM PROGRAMMET!{txd.END}{txd.END}{txd.END}")

            with open('.env', 'w') as f:
                f.write(f"SENDGRID_API_KEY={sendgrid_api_key}\n")
                f.write(f"RECIPIENT_EMAIL={recipient_email}\n")
                f.write(f"SENDER_EMAIL={sender_email}\n")

