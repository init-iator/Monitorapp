from monitor import Monitor
from alarm import AlarmManager
from logger import Logger
import time, os, psutil

monitor = Monitor()
alarm_manager = AlarmManager()
logger = Logger()
logger.log("Applikationen startad")
os.system("cls" if os.name == "nt" else "clear")

def main_menu():
    while True:
        print("\n*** Övervakningsapplikation ***\n")
        print("1. Starta övervakning")
        print("2. Lista aktiv övervakning")
        print("3. Skapa larm")
        print("4. Visa larm")
        print("5. Starta övervakningsläge")
        print("6. Ta bort larm")
        print("7. Realtidsövervakning (Prestanda)")
        print("0. Avsluta programmet")

        choice = input("\nVälj ett alternativ: ")

        # Sanitering av inmatning
        if choice.isdigit():
            choice = int(choice)  # Konvertera till int om det är en giltig siffra
            if choice >= 0 and choice <= 7:  # Kontrollera om det ligger inom giltigt intervall
                logger.log(f"Användaren har gjort val {choice} från huvudmenun")

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
                    try:
                        while True:
                            start_realtimemonitor(
                                psutil.cpu_percent(),
                                psutil.virtual_memory().percent,
                                psutil.disk_usage("/").percent,
                                30
                            )
                            time.sleep(0.6)
                            os.system("cls" if os.name == "nt" else "clear")
                    except KeyboardInterrupt:
                        os.system("cls" if os.name == "nt" else "clear")
                        print("Realtidsövervakning avslutad.")
                        pass
                elif choice == 0:
                    os.system("cls" if os.name == "nt" else "clear")
                    print("\nHejdå...\n")
                    logger.log("Applikationen avslutad")
                    break
            else:
                os.system("cls" if os.name == "nt" else "clear")
                print("Felaktigt val, försök igen.")
                logger.log("Användaren har gjort felaktig val")
        else:
            os.system("cls" if os.name == "nt" else "clear")
            print("Ogiltig inmatning, vänligen ange ett nummer.")
            logger.log("Användaren har matat in ogiltig inmatning.")

def start_monitoring_mode():
    mon = monitor
    if not mon.active:
        os.system("cls" if os.name == "nt" else "clear")
        print("Ingen övervakning är aktiv. Aktivera alternativ \"1\" från huvudmenyn först!")
    else:
        os.system("cls" if os.name == "nt" else "clear")
        print("Övervakningen är aktiv. Tryck på \"Ctrl+C\" för att återgå till huvudmenyn.\n")
        logger.log("Övervakningsläge startat")
        try:
            while True:
                monitor.check_status(alarm_manager)
                time.sleep(1)
        except KeyboardInterrupt:
            os.system("cls" if os.name == "nt" else "clear")
            print("Övervakningsläge avslutad\n")
            logger.log("Övervakningsläge avslutad")
            pass

def start_realtimemonitor(cpu_usage, mem_usage, disk_usage, bars=50):
    cpu_percent = (cpu_usage / 100.0)
    cpu_bar = '█' * int(cpu_percent * bars) + '-' * (bars - int(cpu_percent * bars))
    mem_procent = (mem_usage / 100.0)
    mem_bar = '█' * int(mem_procent * bars) + '-' * (bars - int(mem_procent * bars))
    disk_percent = (disk_usage / 100.0)
    disk_bar = '█' * int(disk_percent * bars) + '-' * (bars - int(disk_percent * bars))
    print(f"\n\nCPU Usage:  |{cpu_bar}| {cpu_usage:.2f}%\n\nMEM Usage:  |{mem_bar}| {mem_usage:.2f}%\n\nDISK Usage: |{disk_bar}| {disk_usage:.2f}%")
    print("\nPress \"Ctrl+c\" to interrupt the performance monitor & go back to headmenu: ", end="\n")

if __name__ == "__main__":
    main_menu()
