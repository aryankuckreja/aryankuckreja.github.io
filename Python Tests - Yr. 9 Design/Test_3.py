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
From: {sender}"""

WHATS GOOOOOOOD
This was sent by Aryan Kuckreja's Robot.

html_txt = """\
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Made By Aryan Kuckreja's Robot</title>
  </head>
  <body>
    <h1>Made By Aryan Kuckreja's Robot</h1>
    <button style="background-color: #df0040;" >hello</button>
    
  </body>
</html>

"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(login, password)
    server.sendmail(sender, receiver, message)

  