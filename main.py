# imortera nödvändiga classer, funktioner och moduler.
from monitor import Monitor
from alarm import AlarmManager
from logger import Logger
import time
import psutil

monitor = Monitor() # monitor variabeln refererar till Monitor classen i filen monitor.py
alarm_manager = AlarmManager() # liknande här också
logger = Logger() # även här.
logger.log("Applikationen startad")

def main_menu(): # funktion för menu val.
    while True: # loop för att komma tillbaka till menu i fall felaktig inmatning sker
        print("\n*** Övervakningsapplikation ***") # Skriv ut alternativen i menu
        print("1. Starta övervakning")
        print("2. Lista aktiv övervakning")
        print("3. Skapa larm")
        print("4. Visa larm")
        print("5. Starta övervakningsläge")
        print("6. Ta bort larm")
        print("7. Realtidsövervakning (Prestanda)")
        print("0. Avsluta")

        choice = input("Välj ett alternativ: ") # inmatning med meddelande utskrift, kommer lagras i choice variabeln
        
        for i in choice:
            i = int(choice)
            if i >= 1 and i <= 7:
                logger.log(f"Användaren har gjort val {i} från huvudmenun")
        
        if choice == '1': # if sats för anrop av gällande class eller funktion
            monitor.start_monitoring() # om choise motsavar 1 körs koden i start_monitor funktionen från filen monitor.py
        elif choice == '2': # liknande som ovan
            monitor.display_status() # liknande som ovan
        elif choice == '3': # liknande som ovan
            alarm_manager.configure_alarm() # liknande som ovan
        elif choice == '4': # liknande som ovan
            alarm_manager.display_alarms() # liknande som ovan
        elif choice == '5': # liknande som ovan
            start_monitoring_mode() # liknande som ovan
        elif choice == '6': # liknande som ovan
            alarm_manager.remove_alarm() # liknande som ovan
        elif choice == '7': # om valet är 7 körs nedanstårnde kod
            try: # Testkör nedanstående koden
                while True: # loop för realtids utskrift av system resusrsernas tillstånd
                    # vi skickar argument till funktionen start_realtimemonitor, argumenten skickar värden till motsvarande-
                    # parametrar i funktionen. argumenten är returnerade värden från psutil modulens motsavrande funktiner.
                    start_realtimemonitor(psutil.cpu_percent(), psutil.virtual_memory().percent, psutil.disk_usage("/").percent, 30)
                    time.sleep(0.5) # vänta angiven tid innan loopen körs vidare.
            except KeyboardInterrupt: # trigga exeption men hjälp av tangentbort avbrytning ctrl+c
                pass # kör koden vidare utan atta få felmeddelande
        elif choice == '0':# om valet är 0 -
            print("\nHejdå...\n") # denna meddelande visas i consollen och -
            logger.log("Applikationen avslutad")
            break # programmet avslutas
        else: # hantering av felaktig inmanting
            print("Felaktigt val, försök igen.") # programmet fortsätter till if satsen. rad 77
            logger.log("Användaren har gjort felaktig val")
            

def start_monitoring_mode(): # funktion för att starta övervakningen.
    print("Övervakning är aktiv, tryck på \"Crtl+c\" för att återgå till menu") # tryck på valfri tangent för att återgå till menyn
    logger.log("Övervakningsläge startat") # logga starten
    try: # testkör nedanstående koden
        while True: # loop för status kontroll för larm hanterare
            monitor.check_status(alarm_manager)
            time.sleep(5)
    except KeyboardInterrupt:
        pass # programmet fortsätter till if satsen. rad 77

def start_realtimemonitor(cpu_usage, mem_usage, disk_usage, bars=50): # funktion för ögonblicksbild av resursernas tillstånd.
    cpu_percent = (cpu_usage / 100.0) # kod för bar
    cpu_bar = '█' * int(cpu_percent * bars) + '-' * (bars - int(cpu_percent * bars)) # kod för bar
    mem_procent = (mem_usage / 100.0) # kod för bar
    mem_bar = '█' * int(mem_procent * bars) + '-' *(bars - int(mem_procent * bars)) # kod för bar
    # Disk usage bar
    disk_percent = (disk_usage / 100.0) # kod för bar
    disk_bar = '█' * int(disk_percent * bars) + '-' * (bars - int(disk_percent * bars)) # kod för bar
    # print för utskrift av resultatet, jag använder formaterad sträng och \n för att fina till utskriften.
    print(f"\n\nCPU Usage:  |{cpu_bar}| {cpu_usage:.2f}%\n\nMEM Usage:  |{mem_bar}| {mem_usage:.2f}%\n\nDISK Usage: |{disk_bar}| {disk_usage:.2f}%")
    # print för avbrott och lämna realtids bevaknings läge.
    print("Press \"Ctrl+c\" to interrupt the performance monitor & go back to headmenu: ", end="\n")

if __name__ == "__main__": # if sats för att återgå till huvud menu, __name__ lika med "__main__" om skriptet är ej importerad och körs som huvudprogramm
    main_menu() # om __name__ lika med __main__ körs main_menu igen.