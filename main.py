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
        print("\n*** Övervakningsapplikation ***")
        print("1. Starta övervakning")
        print("2. Lista aktiv övervakning")
        print("3. Skapa larm")
        print("4. Visa larm")
        print("5. Starta övervakningsläge")
        print("6. Ta bort larm")
        print("7. Realtidsövervakning (Prestanda)")
        print("0. Avsluta")

        choice = input("Välj ett alternativ: ")
        
        for i in choice:
            i = int(choice)
            if i >= 1 and i <= 7:
                logger.log(f"Användaren har gjort val {i} från huvudmenun")
        
        if choice == '1':
            monitor.start_monitoring()
        elif choice == '2':
            monitor.display_status()
        elif choice == '3':
            alarm_manager.configure_alarm()
        elif choice == '4':
            alarm_manager.display_alarms()
        elif choice == '5':
            start_monitoring_mode()
        elif choice == '6':
            alarm_manager.remove_alarm()
        elif choice == '7':
            try:
                while True:
                    start_realtimemonitor(psutil.cpu_percent(), psutil.virtual_memory().percent, psutil.disk_usage("/").percent, 30)
                    time.sleep(1)
                    os.system("cls" if os.name == "nt" else "clear")
            except KeyboardInterrupt:
                pass
        elif choice == '0':
            os.system("cls" if os.name == "nt" else "clear")
            print("\nHejdå...\n")
            logger.log("Applikationen avslutad")
            break
        else:
            print("Felaktigt val, försök igen.")
            logger.log("Användaren har gjort felaktig val")

def start_monitoring_mode():
    mon = monitor
    if not mon.active:
        print("Ingen övervakning är aktiv.")
    else:
        print("Övervakning är aktiv, tryck på \"Crtl+c\" för att återgå till menu\n")
        logger.log("Övervakningsläge startat")
        try:
            while True:
                monitor.check_status(alarm_manager)
                time.sleep(5)
        except KeyboardInterrupt:
            pass

def start_realtimemonitor(cpu_usage, mem_usage, disk_usage, bars=50):
    cpu_percent = (cpu_usage / 100.0)
    cpu_bar = '█' * int(cpu_percent * bars) + '-' * (bars - int(cpu_percent * bars))
    mem_procent = (mem_usage / 100.0)
    mem_bar = '█' * int(mem_procent * bars) + '-' * (bars - int(mem_procent * bars))
    disk_percent = (disk_usage / 100.0)
    disk_bar = '█' * int(disk_percent * bars) + '-' * (bars - int(disk_percent * bars))
    print(f"\n\nCPU Usage:  |{cpu_bar}| {cpu_usage:.2f}%\n\nMEM Usage:  |{mem_bar}| {mem_usage:.2f}%\n\nDISK Usage: |{disk_bar}| {disk_usage:.2f}%")
    print("Press \"Ctrl+c\" to interrupt the performance monitor & go back to headmenu: ", end="\n")

if __name__ == "__main__":
    main_menu()
