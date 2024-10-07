import tkinter as tk
import psutil
from monitor import Monitor
from alarm import AlarmManager

monitor = Monitor()
alarm_manager = AlarmManager()

def update_status():
    if monitor.active:
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_info = psutil.virtual_memory()
        disk_usage = psutil.disk_usage('/')
        status_label.config(text=f"CPU: {cpu_usage}%, RAM: {memory_info.percent}%, Disk: {disk_usage.percent}%")
        root.after(5000, update_status)  # Uppdaterar var 5:e sekund

def start_monitoring():
    monitor.start_monitoring()
    update_status()

def show_alarms():
    alarm_window = tk.Toplevel(root)
    alarm_window.title("Konfigurerade Larm")
    
    text_widget = tk.Text(alarm_window)
    text_widget.pack()
    
    alarms = alarm_manager.alarms
    for category, levels in alarms.items():
        for level in levels:
            text_widget.insert(tk.END, f"{category} larm {level}%\n")

root = tk.Tk()
root.title("Övervakningsapplikation")

start_button = tk.Button(root, text="Starta Övervakning", command=start_monitoring)
start_button.pack(pady=10)

show_alarms_button = tk.Button(root, text="Visa Larm", command=show_alarms)
show_alarms_button.pack(pady=10)

status_label = tk.Label(root, text="Övervakning ej aktiv")
status_label.pack(pady=10)

root.mainloop()
