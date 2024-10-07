import json
from logger import Logger
from email_alert import send_email_alert

class AlarmManager:
    def __init__(self):
        self.alarms = {"CPU": [], "Memory": [], "Disk": []}
        self.load_alarms()

    def configure_alarm(self):
        print("\n1. CPU användning")
        print("2. Minnesanvändning")
        print("3. Diskanvändning")
        print("4. Tillbaka till huvudmeny")

        choice = input("Välj larmtyp: ")
        
        if choice in ['1', '2', '3']:
            level = input("Ställ in nivå för alarm mellan 0-100: ")
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
                else:
                    print("Felaktig nivå. Ange en siffra mellan 1-100.")
            except ValueError:
                print("Felaktig input, försök igen.")
    
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
                print("Ogiltigt val, försök igen.")
        except ValueError:
            print("Felaktig input, försök igen.")
    
    def check_alarm(self, cpu, memory, disk):
        triggered = []
        for level in sorted(self.alarms["CPU"], reverse=True):
            if cpu > level:
                triggered.append(f"***VARNING, CPU ANVÄNDNING ÖVERSTIGER {level}%***")
                break
        
        for level in sorted(self.alarms["Memory"], reverse=True):
            if memory > level:
                triggered.append(f"***VARNING, MINNESANVÄNDNING ÖVERSTIGER {level}%***")
                break
        
        for level in sorted(self.alarms["Disk"], reverse=True):
            if disk > level:
                triggered.append(f"***VARNING, DISKANVÄNDNING ÖVERSTIGER {level}%***")
                break
        
        for message in triggered:
            print(message)
            Logger.log(message)
            send_email_alert(message)  # Skicka e-post

    def save_alarms(self):
        with open('alarms.json', 'w') as f:
            json.dump(self.alarms, f)

    def load_alarms(self):
        try:
            with open('alarms.json', 'r') as f:
                self.alarms = json.load(f)
        except FileNotFoundError:
            pass
