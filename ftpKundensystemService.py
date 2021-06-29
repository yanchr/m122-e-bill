from ftplib import FTP
import re

ftp = FTP("ftp.haraldmueller.ch")
ftp.login("schoolerinvoices", "Berufsschule8005!")

def grabFile(dir):
    ftp.cwd(dir)
    for invoice in ftp.nlst():
        if(re.search("^rechnung.*$", invoice)):
            localfile = open('temp-files/invoices/data/' + invoice, 'wb')
            ftp.retrbinary('RETR ' + invoice, localfile.write, 1024)
            #ftp.delete(invoice)
            localfile.close()
    ftp.quit()

#def placeFile():
#    dirName = "/in/AP18dChristen"
#    ftp.cwd(dirName)
#    filename = '/files/incoive.txt'
#    ftp.storbinary('STOR' + filename, open(filename, 'rb'))
#    ftp.quit()

#grabFile('/out/AP18dChristen', 'rechnung21003.data')    
