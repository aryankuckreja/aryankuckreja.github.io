# user: dsghjfkl@gmail.com
# password:thisIsatestPassword

import smtplib, ssl
from socket import gaierror

port = 465
smtp_server = "smtp.gmail.com"
login = "dsghjfkl@gmail.com"
password = "thisIsatestPassword"
sender = "dsghjfkl@gmail.com"
receiver = "akuckreja30@gmail.com"

message = f"""\
Subject: Daily News!
To: {receiver}
From: {sender}

WHATS GOOOOOOOD
<a href="https://www.youtube.com">Click here to go into youtube</a>
This was sent by Aryan Kuckreja's Robot.
"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(login, password)
    server.sendmail(sender, receiver, message)

  