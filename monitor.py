from logger import Logger  # Importerar Logger-klassen för loggning av händelser
from textdecor import textdec
from alarm import AlarmManager
import psutil, os, time

logformon = Logger()  # Skapar en instans av Logger
txd = textdec()
alarm_manager = AlarmManager()

class Monitor:
    def __init__(self):
        self.active = False  # Initierar monitoreringens status (aktiv/inaktiv)

    def start_monitoring(self):
        self.active = True  # Sätter monitorering till aktiv
        os.system("cls" if os.name == "nt" else "clear")
        while True:
            user_input_start_mon = input(f"{txd.YELLOW}Övervakning startad! Tryck '{txd.BLUE}Enter{txd.END}{txd.YELLOW}' för att återgå till huvudmenu {txd.END}")
            if user_input_start_mon == "":
                os.system("cls" if os.name == "nt" else "clear")
                print(f"\n{txd.CYAN}Bekräftelse mottagen! Återgår till huvudmenu...{txd.END}")
                time.sleep(0.6)
                os.system("cls" if os.name == "nt" else "clear")
                break
            else:
                print(f"{txd.RED}Du måste trycka på endast '{txd.BLUE}Enter{txd.END}"
                      f"{txd.RED}' Försök igen.{txd.RED}")

        logformon.log("Övervakning startad.")

    def display_status(self):
        if not self.active:
            os.system("cls" if os.name == "nt" else "clear")
            print(f"{txd.YELLOW}Ingen övervakning är aktiv. Aktivera alternativ \"{txd.BLUE}"
                  f"1{txd.END}{txd.YELLOW}\" från huvudmenyn först!{txd.END}")
        else:
            cpu_usage = psutil.cpu_percent(interval=0)  # Hämtar CPU-användning
            memory_info = psutil.virtual_memory()
            disk_usage = psutil.disk_usage('/')
            
            os.system("cls" if os.name == "nt" else "clear")

            print(f"{txd.BOLD}{txd.BLUE}Snapshot av resurs användningen:{txd.END}")
            print(f"CPU Användning:\t\t{txd.BLUE}{cpu_usage}{txd.END} %")
            print(f"Minnesanvändning:\t{txd.BLUE}{memory_info.percent}{txd.END} % "
                  f"({memory_info.used / (1024 ** 3):.2f} GB of "
                  f"{memory_info.total / (1024 ** 3):.2f} GB used)"
                  )  # Visar minnesanvändning
            print(f"Diskanvändning:\t\t{txd.BLUE}{disk_usage.percent}{txd.END} % "
                  f"({disk_usage.used / (1024 ** 3):.2f} GB out of "
                  f"{disk_usage.total / (1024 ** 3):.2f} GB used)",
                  end="\n\n"
                  )  # Visar diskens användning
            logformon.log("Användaren har hämtat ögonblicksbild av resursanvändningen")
            logformon.log(f"Mätvärden:\t\tCPU:\t|{cpu_usage}%|\t\tMinne:\t|{memory_info.percent}%|\t\tDisk:\t|{disk_usage.percent}%|")

        while True:
            user_input = input(f"{txd.YELLOW}Tryck endast på '{txd.BLUE}Enter{txd.END}"
                               f"{txd.YELLOW}' för att fortsätta: {txd.END}")
            if user_input == "":
                os.system("cls" if os.name == "nt" else "clear")
                print(f"\n{txd.CYAN}Bekräftelse mottagen! Återgår till huvudmenu...{txd.END}")
                time.sleep(0.6)
                os.system("cls" if os.name == "nt" else "clear")
                break
            else:
                print(f"{txd.RED}Du måste trycka på endast '{txd.BLUE}Enter{txd.END}"
                      f"{txd.RED}' Försök igen.{txd.RED}")

    def start_monitoring_mode(self):
        if not self.active:  # Kontrollera om övervakning är aktiv
            os.system("cls" if os.name == "nt" else "clear")
            print(f"{txd.YELLOW}Ingen övervakning är aktiv. Aktivera alternativ \'{txd.BLUE}1{txd.END}"
                  f"{txd.YELLOW}\' från huvudmenyn först!{txd.END}")
        else:
            os.system("cls" if os.name == "nt" else "clear")
            print(f"{txd.RED}Övervakningen är aktiv. Tryck på \"Ctrl+C\" för att återgå till huvudmenyn.\n{txd.END}")
            logformon.log("Övervakningsläge startat")
            while True:
                try:
                    cpu_usage = psutil.cpu_percent(interval=0)  # Hämtar aktuell CPU-användning
                    memory_usage = psutil.virtual_memory().percent
                    disk_usage = psutil.disk_usage('/').percent

                    alarm_manager.check_alarm(cpu_usage, memory_usage, disk_usage)  # Kontrollerar larm med aktuella användningsvärden
                    time.sleep(2)
                except KeyboardInterrupt:
                    os.system("cls" if os.name == "nt" else "clear")
                    print(f"{txd.RED}Övervakningsläge avslutad\n{txd.END}")
                    logformon.log("Övervakningsläge avslutad")
                    break

    def start_realtimemonitor(self, bars=50):
        cpu_usage = psutil.cpu_percent()
        mem_usage = psutil.virtual_memory().percent

        # Skapa CPU-användningsstapel
        cpu_percent = (cpu_usage / 100.0)
        cpu_bar = '█' * int(cpu_percent * bars) + '-' * (bars - int(cpu_percent * bars))
        
        # Skapa minnesanvändningsstapel
        mem_percent = (mem_usage / 100.0)
        mem_bar = '█' * int(mem_percent * bars) + '-' * (bars - int(mem_percent * bars))
        
        # Skriv ut CPU och minnesanvändning
        print(
            f"\n\nCPU Usage:\t|{cpu_bar}| {cpu_usage:.2f}%\n\n"
            f"MEM Usage:\t|{mem_bar}| {mem_usage:.2f}%\n"
        )
        
        # Hämta alla monterade partitioner och visa diskutnyttjande för varje
        partitions = psutil.disk_partitions()
        for partition in partitions:
            try:
                usage = psutil.disk_usage(partition.mountpoint)
                disk_percent = (usage.percent / 100.0)
                disk_bar = '█' * int(disk_percent * bars) + '-' * (bars - int(disk_percent * bars))
                
                # Visa varje disks användningsstapel och detaljer
                print(
                    f"Disk {partition.device}\t"
                    f"|{disk_bar}| {usage.percent:.2f}%\n"
                )
            except PermissionError:
                # Om åtkomst nekas till partitionen
                print(f"Åtkomst nekad för {partition.device}")
        
        # Uppmaning för att avsluta realtidsövervakning
        print(
            f"\n{txd.YELLOW}Tryck \'{txd.BLUE}Ctrl+c{txd.END}{txd.YELLOW}\' för att avbryta prestandaövervakningen och gå tillbaka till huvudmenyn: {txd.END}", 
            end="\n"
        )