import json, os, time  # Importerar nödvändiga bibliotek för JSON-hantering, systemkommandon och tidskontroll
from logger import Logger
from email_alert import send_email_alert
from textdecor import textdec

alarmlogger = Logger()  # Skapar en instans av Logger
txd = textdec()

class AlarmManager:
    def __init__(self):
        # Initierar larm som en dictionary för CPU, minne och disk
        self.alarms = {"CPU": [], "Memory": [], "Disk": []}
        self.load_alarms()

    def configure_alarm(self):
        while True:
            # Visar alternativ för larmkonfiguration
            print(f"\n{txd.BLUE}1.{txd.END} CPU användning")
            print(f"{txd.BLUE}2.{txd.END} Minnesanvändning")
            print(f"{txd.BLUE}3.{txd.END} Diskanvändning")
            print(f"{txd.RED}4.{txd.END} Tillbaka till huvudmeny")

            choice = input("Välj larmtyp (1-3) eller 4 för att återgå: ")  # Tar emot användarens val

            # Bestäm vilken kategori som valdes
            if choice == "1":
                category = "CPU"
            elif choice == "2":
                category = "Memory"
            elif choice == "3":
                category = "Disk"
            elif choice == "4":
                os.system("cls" if os.name == "nt" else "clear")
                print(f"\n{txd.CYAN}Återgår till huvudmenyn...{txd.END}")
                time.sleep(0.4)
                os.system("cls" if os.name == "nt" else "clear")
                break
            else:
                os.system("cls" if os.name == "nt" else "clear")
                print(f"{txd.RED}Felaktigt val. Välj ett alternativ mellan 1 och 4.{txd.END}")
                continue

            # Om valet är giltigt
            while True:
                # Ber användaren att ställa in larmnivå
                level = input(f"{txd.YELLOW}\nStäll in nivå för {txd.RED}{category}"
                              f"{txd.END}{txd.YELLOW} alarm mellan 0-100:\nEller '{txd.BLUE}<{txd.END}"
                              f"{txd.YELLOW}' för att gå tillbaka{txd.END}\nVäntar på input: ")

                if level == "<":
                    os.system("cls" if os.name == "nt" else "clear")
                    print(f"{txd.GREEN}Tillbaka till val av larmtyp...{txd.END}")
                    time.sleep(0.4)
                    break

                try:
                    level = int(level)  # Konverterar inmatningen till ett heltal

                    if 0 < level <= 100:
                        # Kolla om nivån redan finns i den valda kategorin
                        if level in self.alarms[category]:
                            os.system("cls" if os.name == "nt" else "clear")
                            print(f"{txd.RED}{category}-larm på {level}% finns redan!{txd.END}")
                            print(f"Befintliga {category}-larm: {self.alarms[category]}")
                        else:
                            self.alarms[category].append(level)  # Lägger till larmnivån om den inte redan finns
                            os.system("cls" if os.name == "nt" else "clear")
                            print(f"{txd.YELLOW}{category.capitalize()} larm satt till{txd.END} {txd.GREEN}{level}%{txd.END}")
                            self.save_alarms()
                            alarmlogger.log(f"{category.capitalize()}   \tlarm är konfigurerat och satt till\t|{level} %|")
                            break

                    else:
                        os.system("cls" if os.name == "nt" else "clear")
                        print(f"{txd.RED}Felaktig nivå.{txd.END} {txd.YELLOW}Ange en siffra mellan 1-100.{txd.END}")

                except ValueError:
                    os.system("cls" if os.name == "nt" else "clear")
                    print(f"{txd.RED}Felaktig input.{txd.END} {txd.YELLOW}Ange en siffra mellan 1-100.{txd.END}")

    def display_alarms(self):
        os.system("cls" if os.name == "nt" else "clear")

        # Funktionell visning av larmkategorier och nivåer
        print(f"{txd.GREEN}Lista: lagrade larm.\n{txd.END}")

        # Använd map och lambda för att hantera kategorier och larmnivåer
        display = lambda category: list(map(lambda level: print(f"{category}\tlarm\t{level}%"), sorted(self.alarms[category])))
        list(map(display, ["CPU", "Memory", "Disk"]))  # Använd map för att iterera över kategorier

        # Väntar på användarinmatning (sidoeffekt !)
        input(f"{txd.YELLOW}\nTryck '{txd.BLUE}Enter{txd.END}{txd.YELLOW}' för att återgå till huvudmeny{txd.END} ")
        os.system("cls" if os.name == "nt" else "clear")
        alarmlogger.log("Lista med lagrade larm har visats i skärmen")

    def remove_alarm(self):
        os.system("cls" if os.name == "nt" else "clear")
        
        while True:
            try:
                alarm_list = []  # Lista för att lagra larm
                index = 1  # Räknare för larm
                
                # Visar en lista över lagrade larm
                print(f"{txd.YELLOW}Lista: Lagrade larm.\n{txd.END}")  
                
                for category in ["CPU", "Memory", "Disk"]:  # Loopar igenom larmkategorier
                    for level in sorted(self.alarms[category]):  # Sorterar och visar larmnivåer
                        alarm_list.append((category, level))  # Lägger till larm i listan
                        print(f"{txd.BLUE}{index}.{txd.END}\t{category}\tlarm\t{level}%")  # Visar larm med index
                        index += 1
                
                if not alarm_list:  # Om inga larm finns
                    os.system("cls" if os.name == "nt" else "clear")
                    print(f"{txd.YELLOW}Inga larm att ta bort.{txd.END}")
                    return

                # Tar emot användarens val för vilket larm som ska tas bort
                choice = int(input(f"{txd.YELLOW}\nVälj ett larm att ta bort (ange siffra)\neller välj '{txd.BLUE}0{txd.END}"
                                   f"{txd.YELLOW}' för att återgå till huvudmenyn: {txd.END}"))  
                
                if 1 <= choice <= len(alarm_list):  # Kontrollerar giltigt val
                    category, level = alarm_list[choice - 1]  # Hämta larmkategori och nivå
                    self.alarms[category].remove(level)  # Tar bort larm från kategorin
                    
                    os.system("cls" if os.name == "nt" else "clear")
                    print(f"{txd.YELLOW}\nLarm {category} {level}% borttaget. Återgår till huvudmenyn...{txd.END}")
                    self.save_alarms()
                    alarmlogger.log(f"Larm för\t|{category}|   \t|{level} %| är borttaget")
                    break
                
                elif choice == 0:
                    os.system("cls" if os.name == "nt" else "clear")
                    break
                
                else:
                    os.system("cls" if os.name == "nt" else "clear")
                    print(f"\n{txd.RED}Ogiltigt val, försök igen.{txd.END}")

            except ValueError:  # Hantering av ogiltig inmatning
                os.system("cls" if os.name == "nt" else "clear")
                print(f"\n{txd.RED}Felaktig input, försök igen.{txd.END}")

    def check_alarm(self, cpu, memory, disk):
        triggered = []  # Lista för att lagra utlösta larm
        
        # Loopar igenom CPU-larm och kontrollerar om användningen överskrider nivån
        for level in sorted(self.alarms["CPU"], reverse=True):  
            if cpu > level:  # Kontrollerar om CPU-användningen överskrider nivån
                triggered.append(f"*** VARNING, CPU ANVÄNDNING ÖVERSTIGER   \t\t|{level}%| ***")  # Lägger till varning
                break  # Avbryter loopen efter att första varningen har lagts till
        
        for level in sorted(self.alarms["Memory"], reverse=True):  
            if memory > level:
                triggered.append(f"*** VARNING, MINNESANVÄNDNING ÖVERSTIGER\t\t|{level}%| ***")
                break

        for level in sorted(self.alarms["Disk"], reverse=True):  
            if disk > level:
                triggered.append(f"*** VARNING, DISKANVÄNDNING ÖVERSTIGER   \t\t|{level}%| ***")
                break
        
        for message in triggered:  # Loopar igenom utlösta larm
            print(message)  # Visar varning på skärmen
            alarmlogger.log(f"Larm AKTIVERAD {message}")  # Loggar varningen
            send_email_alert(message)  # Skickar e-postvarning

    def save_alarms(self):
        # Öppnar (eller skapar) en fil för att spara larm
        with open('alarms.json', 'w') as f:  
            json.dump(self.alarms, f)  # Sparar larmen i JSON-format

    def load_alarms(self):
        try:
            # Försöker öppna filen med larm
            with open('alarms.json', 'r') as f:  
                self.alarms = json.load(f)  # Laddar larm från fil
        except FileNotFoundError:  # Hantering av fel om filen inte finns
            alarmlogger.log("Kunde inte ladda filen med lagrade larm")
            pass  # Inga åtgärder vid fil inte hittades
