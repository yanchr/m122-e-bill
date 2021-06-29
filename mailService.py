# Step 1 - Import required packages
from email.message import MIMEPart
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
import smtplib

server = smtplib.SMTP_SSL("smtp.gmail.com:465")
msg = MIMEMultipart()
 
def login():
    password = "a123456789!"
    username = "m122.yanick@gmail.com"
    #server.ehlo()
    server.login(username, password)

def sendMail(message, mail_to, path, filename):
    msg['From'] = "m122.yanick@gmail.com"
    msg['To'] = mail_to
    msg['Subject'] = message
    msg.attach(MIMEText(message, 'plain'))

    print(mail_to)
    

    jpgpart = MIMEApplication(open(path + '/' + filename, 'rb').read())
    jpgpart.add_header('Content-Disposition', 'attachment', filename=filename)
    msg.attach(jpgpart)
    print('sendet')
    server.sendmail(msg['From'], msg['To'], msg.as_string())


def exitServer():
    server.quit()

