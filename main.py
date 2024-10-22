from monitor import Monitor
from alarm import AlarmManager
from logger import Logger
from textdecor import textdec
from email_alert import create_or_update_env_file
import time, os, psutil

# Initiera övervakning, larmhantering och loggning
monitor = Monitor()
alarm_manager = AlarmManager()
logger = Logger()
txdec = textdec()

# Logga att applikationen startas och rensa terminalfönstret
logger.log("Applikationen startad")
os.system("cls" if os.name == "nt" else "clear")

def main_menu():
    while True:
        # Visa menyalternativ
        print(f"\n{txdec.GREEN}*** Övervakningsapplikation ***{txdec.END}\n")
        print(f"{txdec.BLUE}1.{txdec.END} Starta övervakning")
        print(f"{txdec.BLUE}2.{txdec.END} Lista aktiv övervakning")
        print(f"{txdec.BLUE}3.{txdec.END} Skapa larm")
        print(f"{txdec.BLUE}4.{txdec.END} Visa larm")
        print(f"{txdec.BLUE}5.{txdec.END} Starta övervakningsläge")
        print(f"{txdec.BLUE}6.{txdec.END} Ta bort larm")
        print(f"{txdec.BLUE}7.{txdec.END} Realtidsövervakning (Prestanda)")
        print(f"{txdec.BLUE}8.{txdec.END} Kontrollera .env filen för email utskick")
        print(f"{txdec.RED}0.{txdec.END} Avsluta programmet")

        # Ta emot användarens val
        choice = input(f"\nVälj ett alternativ: {txdec.YELLOW}")
        print(txdec.END)

        if choice.isdigit():  # Kontrollera om valet är ett nummer
            choice = int(choice)
            if choice >= 0 and choice <= 8:  # Kontrollera om valet är inom giltigt intervall
                #Avaktivera kommentaret i nedanstående raden för att aktivera loggning av användarvalet
                #logger.log(f"Användaren har gjort val\t|{choice}| från huvudmenun")

                # Hantera olika val
                if choice == 1:
                    monitor.start_monitoring()
                elif choice == 2:
                    monitor.display_status()
                elif choice == 3:
                    os.system("cls" if os.name == "nt" else "clear")
                    alarm_manager.configure_alarm()
                elif choice == 4:
                    alarm_manager.display_alarms()
                elif choice == 5:
                    start_monitoring_mode()
                elif choice == 6:
                    alarm_manager.remove_alarm()
                elif choice == 7:
                    os.system("cls" if os.name == "nt" else "clear")
                    logger.log("Läge för realtidsövervakning startad")
                    try:
                        while True:
                            # Kör realtidsövervakning för CPU, minne och disk
                            monitor.start_realtimemonitor(
                                psutil.cpu_percent(),
                                psutil.virtual_memory().percent,
                                psutil.disk_usage("/").percent,
                                30 # Argument för bars parametern
                                )
                            time.sleep(0.6)
                            os.system("cls" if os.name == "nt" else "clear")
                    except KeyboardInterrupt:
                        os.system("cls" if os.name == "nt" else "clear")
                        print(f"{txdec.YELLOW}Realtidsövervakning avslutad.{txdec.END}")
                        logger.log("Läge för realtidsövervakning avslutad")
                        pass
                elif choice == 8:
                    os.system("cls" if os.name == "nt" else "clear")
                    create_or_update_env_file()
                    time.sleep(2)
                    logger.log("Användaren har inspekterat kongifuration för e-post utskick")
                    os.system("cls" if os.name == "nt" else "clear")
                elif choice == 0:
                    os.system("cls" if os.name == "nt" else "clear")
                    print(f"\n{txdec.BOLD}{txdec.CYAN}Hej-då................................{txdec.END}\n")
                    logger.log("Applikationen avslutad")
                    break
            else:
                os.system("cls" if os.name == "nt" else "clear")
                print(f"{txdec.RED}Felaktigt val, försök igen.{txdec.END}")
                logger.log("Användaren har gjort felaktig val")
        else:
            os.system("cls" if os.name == "nt" else "clear")
            print(f"{txdec.RED}Ogiltig inmatning, vänligen ange ett nummer.{txdec.END}")
            logger.log("Användaren har matat in ogiltig inmatning.")

def start_monitoring_mode():
    mon = monitor
    if not mon.active:  # Kontrollera om övervakning är aktiv
        os.system("cls" if os.name == "nt" else "clear")
        print(f"{txdec.YELLOW}Ingen övervakning är aktiv. Aktivera alternativ \'{txdec.BLUE}1{txdec.END}"
              f"{txdec.YELLOW}\' från huvudmenyn först!{txdec.END}")
    else:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"{txdec.RED}Övervakningen är aktiv. Tryck på \"Ctrl+C\" för att återgå till huvudmenyn.\n{txdec.END}")
        logger.log("Övervakningsläge startat")
        try:
            while True:
                monitor.check_status(alarm_manager)
                time.sleep(1)
        except KeyboardInterrupt:
            os.system("cls" if os.name == "nt" else "clear")
            print(f"{txdec.RED}Övervakningsläge avslutad\n{txdec.END}")
            logger.log("Övervakningsläge avslutad")
            pass

if __name__ == "__main__":
    main_menu()