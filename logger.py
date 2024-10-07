import datetime

class Logger:
    def __init__(self):
        self.filename = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S.log")

    def log(self, message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.filename, 'a') as f:
            f.write(f"{timestamp} - {message}\n")
