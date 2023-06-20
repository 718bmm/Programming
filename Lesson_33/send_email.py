import os 
import ssl
import smtplib
from email.message import EmailMessage

email_sender = 'EMAIL'
email_password = 'EMAIL_PASSWORD'
email_receiver = "elbekcoriev17@gmail.com","pabloskipubgm@gmail.com"


subject = "Check out my video"
body = """
Hi, My name is Chicky
"""

e_m = EmailMessage()
e_m['From'] = email_sender
e_m['To'] = email_receiver
e_m['Subject'] = subject
e_m.set_content(body)

context = ssl.create_default_context()
print("Sending email")
with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as server:
    server.login(email_sender,email_password)
    server.sendmail(
        email_sender,email_receiver,e_m.as_string()

    )
    print("Email was sent")
