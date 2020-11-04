# user: dsghjfkl@gmail.com
# password:thisIsatestPassword
 

import smtplib, ssl

port = 465
sender = "dsghjkl@gmail.com";
password = "thisIsatestPassword";
emailtest = input("Please enter the message you would like to send:\n");
print (emailtest);
receiver = "akuckreja30@gmail.com"

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
	server.login(sender, password)
	server.sendmail(sender, reciever, emailtest)











