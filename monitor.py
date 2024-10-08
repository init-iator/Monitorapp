# imoprt nödvändiga moduler
import psutil
from logger import Logger

logformon = Logger()

class Monitor: # vi skapar class men namnet Monitor
    def __init__(self): # __init__ är en inbyggd funktion som ska initiera objektet i en viss status, i denna fall vi -
        self.active = False # tilldelar attribut "active" och sätter värde "False" vid initieringen.

    def start_monitoring(self): # funktion som ska byta värdet på attributet till "True" denna måste köras minst en gång för att .active ska få värdet True
        self.active = True
        print("Övervakning startad.")
        logformon.log("Övervakning startad.")

    def display_status(self): # funktion som visa statusen.
        if not self.active: # om self.active har värdet False kommer koden att köras.
            print("Ingen övervakning är aktiv.")
        else: # annars om self.active är True kommer koden nedan att köras.
            cpu_usage = psutil.cpu_percent(interval=1)  # vi skapar variabel som heter cpu_usage och använder denna variabel för att lagra data som är skapad av-
            memory_info = psutil.virtual_memory()       # -cpu_percent funktionen från psutil biblioteket och vi sätter intervallet lika med 1, vilket betyder-
            disk_usage = psutil.disk_usage('/')         # -cpu_percent kommer mäta prosessorn i 1 sekund och returnerar medelvärdet av användningen av cpu.
                                                        # Samma för memory_info och disk_usage
            # Utskrift av värden med hjälp av formaterad sträng
            print(f"CPU Användning: {cpu_usage}%")
            # {memory_info.percent} minnes användning i procent, {memory_info.used / (1024 ** 3):.2f} använt minne konverterad till GB .2f för utskrift med 2 st decimaler
            print(f"Minnesanvändning: {memory_info.percent}% ({memory_info.used / (1024 ** 3):.2f} GB of {memory_info.total / (1024 ** 3):.2f} GB used)")
            print(f"Diskanvändning: {disk_usage.percent}% ({disk_usage.used / (1024 ** 3):.2f} GB out of {disk_usage.total / (1024 ** 3):.2f} GB used)")

            logformon.log(f"Användaren har hämtat ögonblicksbild av resusrsanvändningen:\nMätvärden\nCPU Användning: {cpu_usage}%\nMinnesanvändning: {memory_info.percent}% ({memory_info.used / (1024 ** 3):.2f} GB of {memory_info.total / (1024 ** 3):.2f} GB used)\nDiskanvändning: {disk_usage.percent}% ({disk_usage.used / (1024 ** 3):.2f} GB out of {disk_usage.total / (1024 ** 3):.2f} GB used)")
            
        while True:
            user_input = input("Tryck endast på 'Enter' för att fortsätta: ")
            if user_input == "":
                print("Bekräftelse mottagen!")
                break

            else:
                print("Du måste trycka på endast 'Enter'. Försök igen.")

    def check_status(self, alarm_manager): # metod som loopas i bakrunden som hämtar nya värden genom varje loop och dessa värden läses av larm hanteraren.
        cpu_usage = psutil.cpu_percent(interval=0)
        memory_usage = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage('/').percent
        
        alarm_manager.check_alarm(cpu_usage, memory_usage, disk_usage)  # Här anropas check_alarm-metoden på alarm_manager, 
                                                                        # och de insamlade mätvärdena för CPU, minne och disk skickas som argument.
