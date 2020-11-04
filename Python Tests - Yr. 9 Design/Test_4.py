import smtplib, ssl

#User configuration
sender_email = 'dsghjfkl@gmail.com'
reciever_Email = 'akuckreja30@gmail.com'

password = input('Please, type your password:\n')

#Email Body
email_body = '''
 This is a test email sent by Python. Isn't that cool?
'''

print('Sending the email....')
try:
 server = smtplib.SMTP('smtp.gmail.com'', 587)
 context = ssl.create_default_context()
 server.starttls(context=context)
 server.login(sender_email, password)
 server.sendmail(sender_email, reciever_email, email_body)
 print('email sent')
except Exception as e:
 print(f'Oh no! Something bad happened!\n{e]')
finally:
print('closing the server')
server.quit()