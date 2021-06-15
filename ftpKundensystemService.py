from ftplib import FTP
ftp = FTP("ftp.haraldmueller.ch")
ftp.login("schoolerinvoices", "Berufsschule8005!")

def grabFile():
    dirName = "/out/AP18dChristen"
    ftp.cwd(dirName)
    filename = 'rechnung21003.data'
    localfile = open(filename, 'wb')
    ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
    ftp.quit()
    localfile.close()

def placeFile():
    dirName = "/in/AP18dChristen"
    ftp.cwd(dirName)
    filename = 'fileName.txt'
    ftp.storbinary('STOR' + filename, open(filename, 'rb'))
    ftp.quit()