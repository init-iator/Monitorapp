# import json

# def validate_alarm_level(level):
#     try:
#         level = int(level)
#         if 0 < level <= 100:
#             return level
#         else:
#             print("Felaktig nivå. Ange en siffra mellan 1-100.")
#             return None
#     except ValueError:
#         print("Felaktig input, försök igen.")
#         return None

# def sort_alarms(alarms):
#     sorted_alarms = []
#     for category in ["CPU", "Memory", "Disk"]:
#         sorted_alarms.extend(sorted(alarms[category]))
#     return sorted(sorted_alarms)

# def load_json(file_path):
#     try:
#         with open(file_path, 'r') as f:
#             return json.load(f)
#     except FileNotFoundError:
#         return {}

# def save_json(data, file_path):
#     with open(file_path, 'w') as f:
#         json.dump(data, f)

# def prompt_user(message):
#     return input(f"{message} ")
