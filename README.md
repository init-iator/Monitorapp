<h1>Monitoring Application README</h1>

<h2>Description</h2>
<p>
  This Python application helps you monitor system resources such as CPU, memory, and disk usage. You can set alarm levels for these resources and receive email notifications if usage exceeds the specified level. The app also offers a real-time monitoring mode that continuously displays resource usage.
</p>

<h2>Installation</h2>

<h3>Requirements</h3>
<p>
  Make sure you have Python 3 and the following libraries installed:
</p>
<ul>
  <li>sendgrid</li>
  <li>psutil</li>
  <li>datetime</li>
  <li>json</li>
  <li>os</li>
  <li>time</li>
</ul>

<h3>Cloning the Project</h3>
<pre><code>git clone https://github.com/init-iator/Monitorapp.git</code></pre>

<h3>Create .env File</h3>
<p>
  Copy the <code>.env.example</code> file to <code>.env</code> and fill in your SendGrid API key, recipient email address, and sender email address.
</p>

<h2>Running</h2>
<h3>Start the Application:</h3>
<pre><code>python main.py</code></pre>

<h2>Usage</h2>
<p>
  The application presents a main menu with various options:
</p>
<ul>
  <li><strong>Start Monitoring</strong>: Starts a monitoring session where you can retrieve snapshots of system resources.</li>
  <li><strong>List Active Monitoring</strong>: Checks if a monitoring session is active.</li>
  <li><strong>Create Alarm</strong>: Set alarm levels for CPU, memory, and disk usage.</li>
  <li><strong>View Alarms</strong>: View saved alarm levels.</li>
  <li><strong>Start Monitoring Mode</strong>: Opens a real-time mode that continuously checks system resource usage and triggers alarms and email notification if usage exceeds the specified level.</li>
  <li><strong>Remove Alarm</strong>: Remove previously configured alarms.</li>
  <li><strong>Real-time Monitoring (Performance)</strong>: Starts real-time monitoring of resources.</li>
  <li><strong>Check .env File for Email Sending</strong>: Checks the contents of the .env file.</li>
  <li><strong>Exit Program</strong>: Closes the application.</li>
</ul>

<h2>Example</h2>
<p>
  To start a monitoring session and retrieve a snapshot of system resources, choose option 1 in the main menu. To configure an alarm for CPU usage, choose option 3 and enter a percentage level. The application will then send an email notification if CPU usage exceeds the specified level.
</p>

<h2>Contributions</h2>
<p>
  We welcome contributions to this application! You can suggest improvements, report bugs, or submit pull requests on GitHub.
</p>

<h2>License</h2>
<p>
  This application is licensed under the MIT License. See the LICENSE file for more information.
</p>
