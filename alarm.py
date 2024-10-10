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
            print("\n1. CPU användning")
            print("2. Minnesanvändning")
            print("3. Diskanvändning")
            print("4. Tillbaka till huvudmeny")

            choice = input("Välj larmtyp (1-3) eller 4 för att återgå: ")
            for i in choice:
                if choice == "1":
                    i = "cpu"
                elif choice == "2":
                    i = "minnes"
                elif choice == "3":
                    i = "disk"

            if choice == '4':
                os.system("cls" if os.name == "nt" else "clear")
                print("\nÅtergår till huvudmenyn...")
                time.sleep(0.4)
                os.system("cls" if os.name == "nt" else "clear")
                break  # Avbryt loopen och återgå till huvudmenyn
            
            if choice in ['1', '2', '3']:
                while True:
                    level = input(f"\nStäll in nivå för {i} alarm mellan 0-100:\nEller '<' för att gå tillbaka\nVäntar på input: ")
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
                            os.system("cls" if os.name == "nt" else "clear")
                            print(f"{i.capitalize()} larm satt till {level}%")
                            self.save_alarms()
                            break
                        else:
                            os.system("cls" if os.name == "nt" else "clear")
                            print("Felaktig nivå. Ange en siffra mellan 1-100.")
                    except ValueError:
                        os.system("cls" if os.name == "nt" else "clear")
                        print("Felaktig input. Ange en siffra mellan 1-100.")
            else:
                os.system("cls" if os.name == "nt" else "clear")
                print("Felaktigt val. Välj ett alternativ mellan 1 och 4.")

    def display_alarms(self):
        os.system("cls" if os.name == "nt" else "clear")
        print("Lista: lagrade larm.\n")
        for category in ["CPU", "Memory", "Disk"]:
            for level in sorted(self.alarms[category]):
                print(f"{category} larm {level}%")
        input("\nTryck 'Enter' för att gå tillbaka till huvudmenyn.")
        os.system("cls" if os.name == "nt" else "clear")

    def remove_alarm(self):
        os.system("cls" if os.name == "nt" else "clear")
        while True:
            try:
                alarm_list = []
                index = 1
                print("Lista: Lagrade larm.\n")
                for category in ["CPU", "Memory", "Disk"]:
                    for level in sorted(self.alarms[category]):
                        alarm_list.append((category, level))
                        print(f"{index}. {category} larm {level}%")
                        index += 1
                if not alarm_list:
                    os.system("cls" if os.name == "nt" else "clear")
                    print("Inga larm att ta bort.")
                    return  # Avsluta metoden om det inte finns några larm

                choice = int(input("\nVälj ett larm att ta bort (ange siffra)\neller välj '0' för att återgå till huvudmenyn: "))
                if 1 <= choice <= len(alarm_list):
                    category, level = alarm_list[choice - 1]
                    self.alarms[category].remove(level)
                    os.system("cls" if os.name == "nt" else "clear")
                    print(f"\nLarm {category} {level}% borttaget. Återgår till huvudmenyn...")
                    self.save_alarms()
                    break  # Avsluta loopen om larmet har tagits bort
                elif choice == 0:
                    os.system("cls" if os.name == "nt" else "clear")
                    break
                else:
                    os.system("cls" if os.name == "nt" else "clear")
                    print("\nOgiltigt val, försök igen.")
                    # Loopen kommer automatiskt gå vidare här
            except ValueError:
                os.system("cls" if os.name == "nt" else "clear")
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