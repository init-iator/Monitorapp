Monitoring Application README
Description

This Python application helps you monitor system resources such as CPU, memory, and disk usage. You can set alarm levels for these resources and receive email notifications if usage exceeds the specified level. The app also offers a real-time monitoring mode that continuously displays resource usage.

Installation

Requirements: Make sure you have Python 3 and the following libraries installed:
sendgrid
psutil
datetime
json
os
time
Cloning the Project:
Bash
git clone https://github.com/init-iator/Monitorapp.git

Create .env File: Copy the .env.example file to .env and fill in your SendGrid API key, recipient email address, and sender email address.
Running

Start the Application:
Bash
python main.py

Usage

The application presents a main menu with various options:

Start Monitoring: Starts a monitoring session where you can retrieve snapshots of system resources.
List Active Monitoring: Checks if a monitoring session is active.
Create Alarm: Set alarm levels for CPU, memory, and disk usage.
View Alarms: View saved alarm levels.
Start Monitoring Mode: Opens a real-time mode that continuously displays system resource usage.
Remove Alarm: Remove previously configured alarms.
Real-time Monitoring (Performance): Starts real-time monitoring of resources.
Check .env File for Email Sending: Checks the contents of the .env file.
Exit Program: Closes the application.
Example

To start a monitoring session and retrieve a snapshot of system resources, choose option 1 in the main menu. To configure an alarm for CPU usage, choose option 3 and enter a percentage level. The application will then send an email notification if CPU usage exceeds the specified level.

Contributions

We welcome contributions to this application! You can suggest improvements, report bugs, or submit pull requests on GitHub.

License

This application is licensed under the MIT License. See the LICENSE file for more information.