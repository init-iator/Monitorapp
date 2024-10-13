from monitor import Monitor
from alarm import AlarmManager
from logger import Logger
import time, os, psutil

# Initiera övervakning, larmhantering och loggning
monitor = Monitor()
alarm_manager = AlarmManager()
logger = Logger()

# Logga att applikationen startas och rensa terminalfönstret
logger.log("Applikationen startad")
os.system("cls" if os.name == "nt" else "clear")

# Huvudmenyn för applikationen
def main_menu():
    while True:
        # Visa menyalternativ
        print("\n*** Övervakningsapplikation ***\n")
        print("1. Starta övervakning")
        print("2. Lista aktiv övervakning")
        print("3. Skapa larm")
        print("4. Visa larm")
        print("5. Starta övervakningsläge")
        print("6. Ta bort larm")
        print("7. Realtidsövervakning (Prestanda)")
        print("0. Avsluta programmet")

        # Ta emot användarens val
        choice = input("\nVälj ett alternativ: ")

        if choice.isdigit():  # Kontrollera om valet är ett nummer
            choice = int(choice)
            if choice >= 0 and choice <= 7:  # Kontrollera om valet är inom giltigt intervall
                logger.log(f"Användaren har gjort val {choice} från huvudmenun")  # Logga valet

                # Hantera olika val
                if choice == 1:
                    monitor.start_monitoring()  # Starta övervakning
                elif choice == 2:
                    monitor.display_status()  # Visa status på aktiv övervakning
                elif choice == 3:
                    os.system("cls" if os.name == "nt" else "clear")  # Rensa terminalfönstret
                    alarm_manager.configure_alarm()  # Konfigurera ett nytt larm
                elif choice == 4:
                    alarm_manager.display_alarms()  # Visa befintliga larm
                elif choice == 5:
                    start_monitoring_mode()  # Starta övervakningsläge
                elif choice == 6:
                    alarm_manager.remove_alarm()  # Ta bort ett larm
                elif choice == 7:
                    os.system("cls" if os.name == "nt" else "clear")  # Rensa terminalfönstret
                    logger.log("Läge för realtidsövervakning startad")
                    try:
                        while True:
                            # Kör realtidsövervakning för CPU, minne och disk
                            start_realtimemonitor(
                                psutil.cpu_percent(),
                                psutil.virtual_memory().percent,
                                psutil.disk_usage("/").percent,
                                30
                            )
                            time.sleep(0.6)  # Vänta 0.6 sekunder mellan uppdateringar
                            os.system("cls" if os.name == "nt" else "clear")  # Rensa skärmen
                    except KeyboardInterrupt:
                        os.system("cls" if os.name == "nt" else "clear")  # Avsluta övervakningen vid Ctrl+C
                        print("Realtidsövervakning avslutad.")
                        logger.log("Läge för realtidsövervakning avslutad")
                        pass
                elif choice == 0:
                    os.system("cls" if os.name == "nt" else "clear")  # Rensa skärmen
                    print("\nHejdå...\n")
                    logger.log("Applikationen avslutad")  # Logga att applikationen avslutats                                       
                    break  # Avsluta programmet
            else:
                os.system("cls" if os.name == "nt" else "clear")  # Rensa skärmen vid felaktigt val
                print("Felaktigt val, försök igen.")
                logger.log("Användaren har gjort felaktig val")  # Logga felaktigt val
        else:
            os.system("cls" if os.name == "nt" else "clear")  # Rensa skärmen vid ogiltig inmatning
            print("Ogiltig inmatning, vänligen ange ett nummer.")
            logger.log("Användaren har matat in ogiltig inmatning.")  # Logga ogiltig inmatning

# Starta övervakningsläge om en övervakning är aktiv
def start_monitoring_mode():
    mon = monitor
    if not mon.active:  # Kontrollera om övervakning är aktiv
        os.system("cls" if os.name == "nt" else "clear")  # Rensa skärmen
        print("Ingen övervakning är aktiv. Aktivera alternativ \"1\" från huvudmenyn först!")
    else:
        os.system("cls" if os.name == "nt" else "clear")  # Rensa skärmen
        print("Övervakningen är aktiv. Tryck på \"Ctrl+C\" för att återgå till huvudmenyn.\n")
        logger.log("Övervakningsläge startat")  # Logga att övervakningsläget startat
        try:
            while True:
                monitor.check_status(alarm_manager)  # Kontrollera status på övervakningen
                time.sleep(1)  # Vänta 1 sekund mellan kontroller
        except KeyboardInterrupt:
            os.system("cls" if os.name == "nt" else "clear")  # Rensa skärmen vid avbrott
            print("Övervakningsläge avslutad\n")
            logger.log("Övervakningsläge avslutad")  # Logga att övervakningsläget avslutats
            pass

# Visa prestandadata (CPU, minne, disk) i realtid
def start_realtimemonitor(cpu_usage, mem_usage, disk_usage, bars=50):
    cpu_percent = (cpu_usage / 100.0)
    cpu_bar = '█' * int(cpu_percent * bars) + '-' * (bars - int(cpu_percent * bars))  # Skapa CPU-användningsstapel
    mem_procent = (mem_usage / 100.0)
    mem_bar = '█' * int(mem_procent * bars) + '-' * (bars - int(mem_procent * bars))  # Skapa minnesanvändningsstapel
    disk_percent = (disk_usage / 100.0)
    disk_bar = '█' * int(disk_percent * bars) + '-' * (bars - int(disk_percent * bars))  # Skapa diskanvändningsstapel
    # Visa användningsstaplarna
    print(
        f"\n\nCPU Usage:  |{cpu_bar}| {cpu_usage:.2f}%\n\n"
        f"MEM Usage:  |{mem_bar}| {mem_usage:.2f}%\n\n"
        f"DISK Usage: |{disk_bar}| {disk_usage:.2f}%"
    )
    print(
        "\nPress \"Ctrl+c\" to interrupt the performance monitor & go back to headmenu: ", 
        end="\n"
        )

# Kör programmet om det körs direkt
if __name__ == "__main__":
    main_menu()
