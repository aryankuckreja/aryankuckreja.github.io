# user: dsghjfkl@gmail.com
# password:thisIsatestPassword

import smtplib, ssl     #I mentioned how it is beneficial to import smtplib and ssl. They way to get it is to type "pip install smtplib" in your cmd or terminal 

port = 465      #It doesn't matter whether I have a port here as if I didn't then it would automatically assume that the port is 465 (standard port for smtp servers)
smtp_server = "smtp.gmail.com"      #this helps me send the email
login = "dsghjfkl@gmail.com"        #random email with less secure apps on
password = "thisIsatestPassword" 
sender = "dsghjfkl@gmail.com"
receiver = "akuckreja30@gmail.com"  #this is my home email, but you can include your email if you want

#The message
message = f"""\
Subject: Daily Updates To Create More Awareness
To: {receiver}
From: {sender}

This email is about the social awareness of students, as I feel it is slowly decreasing day by day. Social awareness helps children in improving their social skills by interacting with people from diverse backgrounds. Students who are socially aware can recognize the resources available and use them to address the needs of society. It also reflects in their behaviour in the classroom and creates an environment that is ideal for learning. It teaches the skills of communication, collaboration, social responsibility, and professionalism, which are helpful in their professional life.

| Three Website Links |
CBC News link: https://www.cbc.ca/news
This leads you to the front page of what's going on in the news today. Currently, there are many pages about the debate between Trump & Biden.

COVID-19 Tracker link: https://www.coronatracker.com/
This shows the amount of cases that are known of around the world and in specifics part of the world.

Weather Website link: https://weather.com/weather/today/l/43.75,-79.36?par=google&temp=c
This shows the daily weather everyday in all parts of the world.

| Homework |
You have input the following homework:                    Due dates:
Design - Finish Criterion B                               Today at 6 pm
English - Finish the hero summative task                  Today at midnight
Music - Record the pieces                                 Today at midnight

| Concerns about the email |
You have input your response:
No concerns.

Stay tuned for tomorrow's daily updates! - Daily Update Team


."""

context = ssl.create_default_context()      
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:    
    server.login(login, password)
    server.sendmail(sender, receiver, message) 

  