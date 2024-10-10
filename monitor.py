from logger import Logger
import psutil, os

logformon = Logger()

class Monitor:
    def __init__(self):
        self.active = False

    def start_monitoring(self):
        self.active = True
        os.system("cls" if os.name == "nt" else "clear")
        while True:
            user_input_start_mon = input("Övervakning startad! Tryck 'Enter' för att återgå till huvudmenu ")
            if user_input_start_mon == "":
                os.system("cls" if os.name == "nt" else "clear")
                print("\nBekräftelse mottagen! Återgår till huvudmenu...")
                break
            else:
                print("Du måste trycka på endast 'Enter'. Försök igen.")

        logformon.log("Övervakning startad.")

    def display_status(self):
        if not self.active:
            print("Ingen övervakning är aktiv.")
        else:
            cpu_usage = psutil.cpu_percent(interval=0)
            memory_info = psutil.virtual_memory()
            disk_usage = psutil.disk_usage('/')
            
            os.system("cls" if os.name == "nt" else "clear")

            print("Snapshot av resurs användningen:")
            print(f"CPU Användning:\t\t{cpu_usage}%")
            print(f"Minnesanvändning:\t{memory_info.percent}% ({memory_info.used / (1024 ** 3):.2f} GB of {memory_info.total / (1024 ** 3):.2f} GB used)")
            print(f"Diskanvändning:\t\t{disk_usage.percent}% ({disk_usage.used / (1024 ** 3):.2f} GB out of {disk_usage.total / (1024 ** 3):.2f} GB used)", end="\n\n")

            logformon.log(f"Användaren har hämtat ögonblicksbild av resusrsanvändningen:\nMätvärden\nCPU Användning: {cpu_usage}%\nMinnesanvändning: {memory_info.percent}% ({memory_info.used / (1024 ** 3):.2f} GB of {memory_info.total / (1024 ** 3):.2f} GB used)\nDiskanvändning: {disk_usage.percent}% ({disk_usage.used / (1024 ** 3):.2f} GB out of {disk_usage.total / (1024 ** 3):.2f} GB used)")

        while True:
            user_input = input("Tryck endast på 'Enter' för att fortsätta: ")
            if user_input == "":
                os.system("cls" if os.name == "nt" else "clear")
                print("\nBekräftelse mottagen! Återgår till huvudmenu...")
                break
            else:
                print("Du måste trycka på endast 'Enter'. Försök igen.")

    def check_status(self, alarm_manager):
        cpu_usage = psutil.cpu_percent(interval=0)
        memory_usage = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage('/').percent
        
        alarm_manager.check_alarm(cpu_usage, memory_usage, disk_usage)
