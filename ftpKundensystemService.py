from ftplib import FTP
ftp = FTP("ftp.haraldmueller.ch")
ftp.login("schoolerinvoices", "Berufsschule8005!")

def grabFile(dir, fileName):
    ftp.cwd(dir)
    localfile = open('temp-files/invoices/data/' + fileName, 'wb')
    ftp.retrbinary('RETR ' + fileName, localfile.write, 1024)
    # ftp.delete(fileName)
    ftp.quit()
    localfile.close()

#def placeFile():
#    dirName = "/in/AP18dChristen"
#    ftp.cwd(dirName)
#    filename = '/files/incoive.txt'
#    ftp.storbinary('STOR' + filename, open(filename, 'rb'))
#    ftp.quit()

#grabFile('/out/AP18dChristen', 'rechnung21003.data')    
