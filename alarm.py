import json, os, time
from logger import Logger
from email_alert import send_email_alert

alarmlogger = Logger()
class AlarmManager:
    def __init__(self):
        self.alarms = {"CPU": [], "Memory": [], "Disk": []}
        self.load_alarms()
        
    def configure_alarm(self):
        while True:
            #os.system("cls" if os.name == "nt" else "clear")
            print("\n1. CPU användning")
            print("2. Minnesanvändning")
            print("3. Diskanvändning")
            print("4. Tillbaka till huvudmeny")

            choice = input("Välj larmtyp (1-3) eller 4 för att återgå: ")

            if choice == '4':
                os.system("cls" if os.name == "nt" else "clear")
                print("\nÅtergår till huvudmenyn...")
                time.sleep(0.4)
                break  # Avbryt loopen och återgå till huvudmenyn
            
            if choice in ['1', '2', '3']:
                while True:
                    level = input("\nStäll in nivå för alarm mellan 0-100:\nEller '<' för att gå tillbaka\nVäntar på input: ")
                    if level == "<":
                        os.system("cls" if os.name == "nt" else "clear")
                        print("Går tillbaka till val av larmtyp...")
                        time.sleep(0.4)
                        break  # Bryt loopen och gå tillbaka till val av larmtyp
                    try:                        
                        level = int(level)
                        if 0 < level <= 100:
                            if choice == '1':
                                self.alarms["CPU"].append(level)
                            elif choice == '2':
                                self.alarms["Memory"].append(level)
                            elif choice == '3':
                                self.alarms["Disk"].append(level)
                            print(f"Larm satt till {level}%")
                            self.save_alarms()
                            break
                        else:
                            print("Felaktig nivå. Ange en siffra mellan 1-100.")
                    except ValueError:
                        print("Felaktig input. Ange en siffra mellan 1-100.")
            else:
                print("Felaktigt val. Välj ett alternativ mellan 1 och 4.")

    def display_alarms(self):
        for category in ["CPU", "Memory", "Disk"]:
            for level in sorted(self.alarms[category]):
                print(f"{category} larm {level}%")
        input("Tryck valfri tangent för att gå tillbaka till huvudmenyn.")

    def remove_alarm(self):
        alarm_list = []
        index = 1
        for category in ["CPU", "Memory", "Disk"]:
            for level in sorted(self.alarms[category]):
                alarm_list.append((category, level))
                print(f"{index}. {category} larm {level}%")
                index += 1
                
        if not alarm_list:
            print("Inga larm att ta bort.")
            return

        try:
            choice = int(input("Välj ett larm att ta bort (siffra): "))
            if 1 <= choice <= len(alarm_list):
                category, level = alarm_list[choice - 1]
                self.alarms[category].remove(level)
                print(f"Larm {category} {level}% borttaget.")
                self.save_alarms()
            else:
                print("\nOgiltigt val, försök igen.")
        except ValueError:
            print("\nFelaktig input, försök igen.")
    
    def check_alarm(self, cpu, memory, disk):
        triggered = []
        for level in sorted(self.alarms["CPU"], reverse=True):
            if cpu > level:
                triggered.append(f"*** VARNING, CPU ANVÄNDNING ÖVERSTIGER\t\t\t{level}% ***")
                break
        
        for level in sorted(self.alarms["Memory"], reverse=True):
            if memory > level:
                triggered.append(f"*** VARNING, MINNESANVÄNDNING ÖVERSTIGER\t\t{level}% ***")
                break
        
        for level in sorted(self.alarms["Disk"], reverse=True):
            if disk > level:
                triggered.append(f"*** VARNING, DISKANVÄNDNING ÖVERSTIGER\t\t\t{level}% ***")
                break
        
        for message in triggered:
            print(message)
            alarmlogger.log(f"{message}")
            #Logger.log(message)
            #send_email_alert(message)  # Skicka e-post

    def save_alarms(self):
        with open('alarms.json', 'w') as f:
            json.dump(self.alarms, f)

    def load_alarms(self):
        try:
            with open('alarms.json', 'r') as f:
                self.alarms = json.load(f)
        except FileNotFoundError:
            pass