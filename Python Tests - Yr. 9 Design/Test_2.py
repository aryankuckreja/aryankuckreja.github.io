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
To: {receiver}
From: {sender}

message = """\
Subject: Daily News!

Hi,
How are you?
Real Python has many great tutorials:
www.realpython.com"""
html = """\
<html>
  <body>
    <p>Hi,<br>
       How are you?<br>
       <a href="http://www.realpython.com">Real Python</a> 
       has many great tutorials.
    </p>
  </body>
</html>
"""

part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

message.attach(part1)
message.attach(part2)

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(login, password)
    server.sendmail(sender, receiver, message.as_string()
)
    


  