import smtplib
from email.message import EmailMessage

textfile = 'emailtest.txt'
with open(textfile) as fp:
    # Create a text/plain message
    msg = EmailMessage()
    msg.set_content(fp.read())

msg['Subject'] = f'The contents of {textfile}'
msg['From'] = 'yanick.christen@gmail.com'
msg['To'] = 'yanick.christen@gmail.com'

# Send the message via our own SMTP server.
s = smtplib.SMTP('localhost')   
s.send_message(msg)
s.quit()