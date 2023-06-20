import smtplib, ssl, os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


message = MIMEMultipart('alternative')
message['Subject'] = 'multipart test'
message['From'] = os.environ.get('bmmusadjanov@gmail.com')
message['To'] = 'pabloskipubgm@gmail.com'
email_sender = os.environ.get('bmmusadjanov@gmail.com')
email_password = os.environ.get('xgyacgfprobdcagh')
email_receiver = 'pabloskipubgm@gmail.com'


# Create the plain-text and HTML version of your message
text = """\
Hi,
How are you?
Real Python has many great tutorials:
www.realpython.com"""
html = """\
<html>
  <body>
    <p>Hi,<br>
       How are you?<br>
       <a href="http://www.realpython.com">Real Python fourth time</a> 
       has many great tutorials.
    </p>
  </body>
</html>
"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

# Create secure connection with server and send email
context = ssl.create_default_context()
print('Sending email...')
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
    server.login(email_sender, email_password)
    server.sendmail(
        email_sender, email_receiver, message.as_string()
    )
    print('Email was sent!')

