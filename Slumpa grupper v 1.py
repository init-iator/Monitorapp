import random, os
namnlista = []
gruppstorlek = 0

def read_file():
    try:
        with open("names.txt", "r",encoding='UTF-8') as file:
            for line in file:
                namnlista.append(line.strip())
    except FileNotFoundError:
        print("File not found")
# Menu

def menu():
    print("Program för att skapa grupper\nVälja val: ")
    print("""1. Mata in namn
2. Ta bort namn
3. Välj gruppstorlek
4. Skapa grupper
5. Avsluta programmet.""")
    val = input("Välj alternativ: ")
    return val
    

def mata_in():
    namn = input("Mata in namn eller skriv done när du är färdig och/eller om du vill gå tillbaka ")
    while namn != "done": 
        namnlista.append(namn)
        print(f"{namn} har lagts till.")
        namn = input("Mata in namn eller skriv done när du är färdig och/eller om du vill gå tillbaka ")
    print(namnlista)

def del_name():
    namn = input("Ange ett namn att ta bort: ")
    if namn in namnlista:
        namnlista.remove(namn)
        print(f"{namn} har tagits bort.")
    else:
        print(f"{namn} finns inte i listan.")

def group_size():
    global gruppstorlek 
    gruppstorlek = int(input("Ange gruppstorlek: "))
    print(f"Gruppstorleken har satts till {gruppstorlek}.")

def create_group():
    if gruppstorlek == 0:
        print("\n\nGruppstorlek är ej vald, Välj först gruppstorlek.\nProgrammet har startas om:")
    elif len(namnlista) == 0:
        print("\n\nListan med namn är tom. Lägg till namn först.\nProgrammet har startats om:")
    else:
        random.shuffle(namnlista)  # Slumpa namnen
        grupper = [namnlista[i:i + gruppstorlek] for i in range(0, len(namnlista), gruppstorlek)]
       #5 print(grupper)
        for i, grupp in enumerate(grupper, start=1):
            print(f"Grupp {i}: {', '.join(grupp)}")
read_file()
while True:
        val = menu()
        if val == "1":
            mata_in()
        elif val == "2":
            del_name()
        elif val == "3":
            group_size()
        elif val == "4":
            create_group()
        elif val == "5":
            print("\nProgrammet avslutas:.......")
            break
        else:
            print("felaktig val! Försök igen: \nProgrammet startas om....")



# import random.random (0, len (lista) -1)
# grupplista.append (losta [index])

# sätt 2
# random.sample(lista,5)