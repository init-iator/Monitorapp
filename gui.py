# import tkinter as tk
# import psutil
# from monitor import Monitor
# from alarm import AlarmManager

# monitor = Monitor()
# alarm_manager = AlarmManager()

# def update_status():
#     if monitor.active:
#         cpu_usage = psutil.cpu_percent(interval=1)
#         memory_info = psutil.virtual_memory()
#         disk_usage = psutil.disk_usage('/')
#         status_label.config(text=f"CPU: {cpu_usage}%, RAM: {memory_info.percent}%, Disk: {disk_usage.percent}%")
#         root.after(5000, update_status)  # Uppdaterar var 5:e sekund

# def start_monitoring():
#     monitor.start_monitoring()
#     update_status()

# def show_alarms():
#     alarm_window = tk.Toplevel(root)
#     alarm_window.title("Konfigurerade Larm")
    
#     text_widget = tk.Text(alarm_window)
#     text_widget.pack()
    
#     alarms = alarm_manager.alarms
#     for category, levels in alarms.items():
#         for level in levels:
#             text_widget.insert(tk.END, f"{category} larm {level}%\n")

# root = tk.Tk()
# root.title("Övervakningsapplikation")

# start_button = tk.Button(root, text="Starta Övervakning", command=start_monitoring)
# start_button.pack(pady=10)

# show_alarms_button = tk.Button(root, text="Visa Larm", command=show_alarms)
# show_alarms_button.pack(pady=10)

# status_label = tk.Label(root, text="Övervakning ej aktiv")
# status_label.pack(pady=10)

# root.mainloop()


import tkinter as tk
from tkinter import scrolledtext, messagebox, simpledialog
from monitor import Monitor
from alarm import AlarmManager
from logger import Logger
from test import ResourceMonitorApp
import psutil
import threading

# Skapa instanser av Monitor, AlarmManager och Logger
monitor = Monitor()
alarm_manager = AlarmManager()
logger = Logger()

class MonitoringApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Övervakningsapplikation")

        # Skapa ram för knappar
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)

        # Knappar placerade i en rad
        self.start_monitoring_btn = tk.Button(self.button_frame, text="1. Starta Övervakning", command=self.start_monitoring)
        self.start_monitoring_btn.pack(side=tk.LEFT, padx=5)

        self.show_status_btn = tk.Button(self.button_frame, text="2. Lista aktiv övervakning", command=self.display_status)
        self.show_status_btn.pack(side=tk.LEFT, padx=5)

        self.configure_alarm_btn = tk.Button(self.button_frame, text="3. Skapa larm", command=self.configure_alarm)
        self.configure_alarm_btn.pack(side=tk.LEFT, padx=5)

        self.show_alarms_btn = tk.Button(self.button_frame, text="4. Visa Larm", command=self.show_alarms)
        self.show_alarms_btn.pack(side=tk.LEFT, padx=5)

        self.remove_alarm_btn = tk.Button(self.button_frame, text="5. Starta övervakningsläge", command=self.remove_alarm)
        self.remove_alarm_btn.pack(side=tk.LEFT, padx=5)

        self.start_realtime_monitor_btn = tk.Button(self.button_frame, text="6. Ta bort larm", command=self.start_realtime_monitor)
        self.start_realtime_monitor_btn.pack(side=tk.LEFT, padx=5)

        self.start_realtime_monitor_btn = tk.Button(self.button_frame, text="7. Realtidsövervakning (Prestanda)", command=self.start_realtime_monitor)
        self.start_realtime_monitor_btn.pack(side=tk.LEFT, padx=5)

        self.quit_btn = tk.Button(self.button_frame, text="0. Avsluta", command=self.root.quit)
        self.quit_btn.pack(side=tk.LEFT, padx=5)

        # Loggfält
        self.log_text = scrolledtext.ScrolledText(self.root, width=80, height=20)
        self.log_text.pack(pady=10)

    def start_monitoring(self):
        """Starta monitorering i en separat tråd."""
        logger.log("Övervakning startad.")
        self.log_text.insert(tk.END, "Övervakning startad.\n")
        self.log_text.see(tk.END)  # Scrolla till slutet
        monitor.active = True
        # threading.Thread(target=self.monitor_resources, daemon=True).start()

    def monitor_resources(self):
        """Övervaka resurser och logga status."""
        while monitor.active:
            cpu_usage = psutil.cpu_percent(interval=1)
            memory_info = psutil.virtual_memory()
            disk_usage = psutil.disk_usage('/')
            
            log_message = (
                f"CPU Användning: {cpu_usage}% | "
                f"Minne: {memory_info.percent}% | "
                f"Disk: {disk_usage.percent}%\n"
            )
            self.log_text.insert(tk.END, log_message)
            self.log_text.see(tk.END)  # Scrolla till slutet
            logger.log(log_message)

            # Kontrollera larm
            alarm_manager.check_alarm(cpu_usage, memory_info.percent, disk_usage.percent)

    def display_status(self):
        """Visa aktuell status i loggfältet."""
        if not monitor.active:
            self.log_text.insert(tk.END, "Ingen övervakning är aktiv.\n")
            return
        
        cpu_usage = psutil.cpu_percent(interval=0)
        memory_info = psutil.virtual_memory()
        disk_usage = psutil.disk_usage('/')

        status_message = (
            f"CPU Användning: {cpu_usage}%\n"
            f"Minne: {memory_info.percent}% ({memory_info.used / (1024 ** 3):.2f} GB av "
            f"{memory_info.total / (1024 ** 3):.2f} GB)\n"
            f"Disk: {disk_usage.percent}% ({disk_usage.used / (1024 ** 3):.2f} GB av "
            f"{disk_usage.total / (1024 ** 3):.2f} GB)\n"
        )
        self.log_text.insert(tk.END, status_message)
        self.log_text.see(tk.END)

    def configure_alarm(self):
        """Konfigurera ett nytt larm."""
        try:
            cpu_threshold = simpledialog.askfloat("Konfigurera Larm", "Ange CPU-tröskelvärde (%):", minvalue=0, maxvalue=100)
            mem_threshold = simpledialog.askfloat("Konfigurera Larm", "Ange Minnes-tröskelvärde (%):", minvalue=0, maxvalue=100)
            disk_threshold = simpledialog.askfloat("Konfigurera Larm", "Ange Disk-tröskelvärde (%):", minvalue=0, maxvalue=100)

            if cpu_threshold is not None and mem_threshold is not None and disk_threshold is not None:
                alarm_manager.set_alarm(cpu_threshold, mem_threshold, disk_threshold)
                self.log_text.insert(tk.END, "Larm konfigurerat:\n"
                                              f"CPU: {cpu_threshold}%, "
                                              f"Minne: {mem_threshold}%, "
                                              f"Disk: {disk_threshold}%\n")
            else:
                self.log_text.insert(tk.END, "Larmkonfiguration avbruten.\n")
        except Exception as e:
            self.log_text.insert(tk.END, f"Fel vid konfiguration av larm: {e}\n")

        self.log_text.see(tk.END)

    def show_alarms(self):
        """Visa larm i loggfältet."""
        alarms = alarm_manager.get_alarms()  # Anta att get_alarms() finns
        if alarms:
            self.log_text.insert(tk.END, "Befintliga larm:\n" + "\n".join(alarms) + "\n")
        else:
            self.log_text.insert(tk.END, "Inga larm konfigurerade.\n")
        self.log_text.see(tk.END)

    def remove_alarm(self):
        """Ta bort ett larm (placeholder för framtida implementering)."""
        messagebox.showinfo("Ta bort Larm", "Här kan du ta bort ett larm (ej implementerat).")
        self.log_text.insert(tk.END, "Larm borttaget (ej implementerat).\n")
        self.log_text.see(tk.END)

    def start_realtime_monitor(self):
        """Starta realtidsövervakning."""
        self.log_text.insert(tk.END, "Realtidsövervakning startad (ej implementerat).\n")
        self.log_text.see(tk.END)
        ResourceMonitorApp(None)
        # Här kan du implementera realtidsövervakning med grafer, staplar etc.

if __name__ == "__main__":
    root = tk.Tk()
    app = MonitoringApp(root)
    root.mainloop()
