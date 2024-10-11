from logger import Logger  # Importerar Logger-klassen för loggning av händelser
import psutil, os, time  # Importerar nödvändiga bibliotek för systemövervakning och hantering

logformon = Logger()  # Skapar en instans av Logger

class Monitor:
    def __init__(self):
        self.active = False  # Initierar monitoreringens status (aktiv/inaktiv)

    def start_monitoring(self):
        self.active = True  # Sätter monitorering till aktiv
        os.system("cls" if os.name == "nt" else "clear")  # Rensar skärmen
        while True:
            user_input_start_mon = input("Övervakning startad! Tryck 'Enter' för att återgå till huvudmenu ")
            if user_input_start_mon == "":
                os.system("cls" if os.name == "nt" else "clear")  # Rensar skärmen
                print("\nBekräftelse mottagen! Återgår till huvudmenu...")  # Bekräftar återgång
                time.sleep(0.6)  # Väntar en kort stund
                os.system("cls" if os.name == "nt" else "clear")  # Rensar skärmen igen
                break  # Avslutar loopen
            else:
                print("Du måste trycka på endast 'Enter'. Försök igen.")  # Använder felaktig inmatning

        logformon.log("Övervakning startad.")  # Loggar att övervakningen har startat

    def display_status(self):
        if not self.active:
            os.system("cls" if os.name == "nt" else "clear")  # Rensar skärmen
            print("Ingen övervakning är aktiv. Aktivera alternativ \"1\" från huvudmenyn först!")  # Meddelande om inaktiv monitorering
        else:
            cpu_usage = psutil.cpu_percent(interval=0)  # Hämtar CPU-användning
            memory_info = psutil.virtual_memory()  # Hämtar minnesinformation
            disk_usage = psutil.disk_usage('/')  # Hämtar diskinformation
            
            os.system("cls" if os.name == "nt" else "clear")  # Rensar skärmen

            print("Snapshot av resurs användningen:")  # Rubrik för resursanvändning
            print(f"CPU Användning:\t\t{cpu_usage}%")  # Visar CPU-användning
            print(
                f"Minnesanvändning:\t{memory_info.percent}% "
                f"({memory_info.used / (1024 ** 3):.2f} GB of "
                f"{memory_info.total / (1024 ** 3):.2f} GB used)"
            )  # Visar minnesanvändning
            print(
                f"Diskanvändning:\t\t{disk_usage.percent}% "
                f"({disk_usage.used / (1024 ** 3):.2f} GB out of "
                f"{disk_usage.total / (1024 ** 3):.2f} GB used)",
                end="\n\n"
            )  # Visar diskens användning
            logformon.log(  # Loggar ögonblicksbild av resursanvändning
                f"Användaren har hämtat ögonblicksbild av resursanvändningen:\n"
                f"Mätvärden\n"
                f"CPU Användning: {cpu_usage}%\n"
                f"Minnessanvändning: {memory_info.percent}% "
                f"({memory_info.used / (1024 ** 3):.2f} GB of "
                f"{memory_info.total / (1024 ** 3):.2f} GB used)\n"
                f"Diskanvändning: {disk_usage.percent}% "
                f"({disk_usage.used / (1024 ** 3):.2f} GB out of "
                f"{disk_usage.total / (1024 ** 3):.2f} GB used)"
            )
            
        while True:
            user_input = input("Tryck endast på 'Enter' för att fortsätta: ")  # Väntar på användarinmatning
            if user_input == "":
                os.system("cls" if os.name == "nt" else "clear")  # Rensar skärmen
                print("\nBekräftelse mottagen! Återgår till huvudmenu...")  # Bekräftar återgång
                time.sleep(0.6)  # Väntar en kort stund
                os.system("cls" if os.name == "nt" else "clear")  # Rensar skärmen igen
                break  # Avslutar loopen
            else:
                print("Du måste trycka på endast 'Enter'. Försök igen.")  # Meddelande om felaktig inmatning

    def check_status(self, alarm_manager):
        cpu_usage = psutil.cpu_percent(interval=0)  # Hämtar aktuell CPU-användning
        memory_usage = psutil.virtual_memory().percent  # Hämtar aktuell minnesanvändning
        disk_usage = psutil.disk_usage('/').percent  # Hämtar aktuell disk-användning
        
        alarm_manager.check_alarm(cpu_usage, memory_usage, disk_usage)  # Kontrollerar larm med aktuella användningsvärden
