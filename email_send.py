import smtplib
from email.mime.text import MIMEText

# Email configuration
smtp_server = "smtp.gmail.com"  # Updated for Gmail
port = 587
username = "minsaq43@gmail.com" # Your sender email

# IMPORTANT: This must be a 16-character "App Password", NOT your regular password.
password = "ehllmhabwizuweas"
# Email content
msg = MIMEText("Sir , I am a student of Great Learning and I don't have money . I am student . I want linux tutorials certificate for free.")
msg['Subject'] = "Request for Free Linux Tutorials Certificate."
msg['From'] = "minsaq43@gmail.com"
msg['To'] = "info@greatlearning.in"   # Great Learning's support email

# Send email
with smtplib.SMTP(smtp_server, port) as server:
    server.starttls()
    server.login(username, password)
    server.send_message(msg)
    password = "ehll mhab wizu weas"
print("Email sent successfully!")