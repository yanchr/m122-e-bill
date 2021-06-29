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

def placeFiles(directory, filename):
    ftp = connect()
    print('connection')
    ftp.cwd(directory)
    ftp.storbinary('STOR ' + filename + '.txt', open('temp-files/invoices/txt/' + filename + '.txt', 'rb'))
    ftp.storbinary('STOR ' + filename + '.xml', open('temp-files/invoices/xml/' + filename + '.xml', 'rb'))
    ftp.quit()

