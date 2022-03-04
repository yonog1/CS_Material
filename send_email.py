from email import message
import smtplib
import ssl
from email.message import EmailMessage

import keyring

subject = "Email from Python"
body = "If this works go eat"
sender_email = "smurfforcr420@gmail.com"
receiver_email = "yonatangoldin69@gmail.com"
password = input("enter a password: ")

SERVICE_ID = "gmail.com"

keyring.set_password(SERVICE_ID, sender_email, password)

message = EmailMessage()

message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

html = f"""
<html>
    <body>
        <h1>{subject}</h1>
        <p>{body}</p>
    </body>
</html>
"""

message.add_alternative(html, subtype = "html")

context = ssl.create_default_context()

print("Sending Email")
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    try:
        server.login(sender_email, keyring.get_password(SERVICE_ID, sender_email))
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Successs")
    except smtplib.SMTPAuthenticationError or TypeError:
        print("Wrong password, please try again.")
