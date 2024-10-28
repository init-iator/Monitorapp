import threading
import time

# Definiera funktionen för loopen som ska köras i en separat tråd
def oandlig_loop():
    while True:
        print("Loopen körs...")
        time.sleep(1)  # Fördröjning för att undvika att den körs för snabbt

# Definiera funktionen som ska invänta Ctrl+C
def vänta_på_ctrl_c():
    try:
        print("Tryck Ctrl+C för att stoppa loopen.")
        while True:
            time.sleep(0.1)  # Vänta och gör ingenting
    except KeyboardInterrupt:
        print("\nCtrl+C upptäckt! Avslutar programmet.")
        # Om `KeyboardInterrupt` fångas, avsluta programmet
        exit(0)

# Starta den oändliga loopen i en separat tråd
loop_tråd = threading.Thread(target=oandlig_loop)
loop_tråd.daemon = True  # Sätter tråden som daemon så att den avslutas när huvudprogrammet avslutas
loop_tråd.start()

# Kör funktionen för att vänta på Ctrl+C i huvudtråden
vänta_på_ctrl_c()
