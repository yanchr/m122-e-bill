from ftplib import FTP
import re
def connect():
    ftp = FTP("134.119.225.245")    
    ftp.login("310721-297-zahlsystem", "Berufsschule8005!")
    return ftp

def grabReceipts(dir):
    ftp = connect()
    ftp.cwd(dir)
    for receipt in ftp.nlst():
        if(re.search("^quittungsfile.*$", receipt)):
            localfile = open('temp-files/receipts/' + receipt, 'wb')
            ftp.retrbinary('RETR ' + receipt, localfile.write, 1024)
            ftp.delete(receipt)
            localfile.close()
    ftp.quit()

def placeFile(directory, filename):
    ftp = connect()
    ftp.cwd(directory)
    ftp.storbinary('STOR ' + filename, open('temp-files/invoices/txt/' + filename, 'rb'))
    ftp.quit()

