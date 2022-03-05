import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Email Account
email_sender_account = "reconnect.hack@gmail.com" #I'm not sure about this one.
email_sender_username = "reconnect.hack@gmail.com"
email_sender_password = "ReconnectP@ssword"
email_smtp_server = "smtp.gmail.com"
email_smtp_port = 587 #Email Content
recipient = "<recepient1>"
email_subject = "<Email Subject>"
email_body = "Hello! This is a reminder that you need to re-connect with " + "<Person's name>" + ". Click on the followng link once you have done so."
                #Make sure to provide a link.
#login to email server
server = smtplib.SMTP(email_smtp_server,email_smtp_port)
server.starttls()
server.login(email_sender_username, email_sender_password)#For loop, sending emails to all email recipients
    
print(f"Sending email to {recipient}")
message = MIMEMultipart('alternative')
message['From'] = email_sender_account
message['To'] = recipient
message['Subject'] = email_subject
message.attach(MIMEText(email_body, 'html'))
text = message.as_string()
server.sendmail(email_sender_account,recipient,text)#All emails sent, log out.

server.quit()