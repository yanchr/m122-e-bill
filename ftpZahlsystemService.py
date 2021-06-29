from ftplib import FTP
import re
import os 

def connect():
    ftp = FTP("134.119.225.245")    
    ftp.login("310721-297-zahlsystem", "Berufsschule8005!")
    return ftp

def grab_receipts(dir):
    ftp = connect()
    ftp.cwd(dir)
    receipt_numbers = []
    for receipt in ftp.nlst():
        if(re.search("^quittungsfile.*$", receipt)):
           receipt_numbers.append(grab_receipt(ftp, receipt))
    return receipt_numbers


def grab_receipt(ftp, receipt):
        #grab archive files
        receipt_number = get_number_of_receipt(receipt)
        grab_files_from_receipt_archive(receipt_number)

        localfile = open('temp-files/receipt-folders/' + receipt_number + '/' + receipt, 'wb')
        ftp.retrbinary('RETR ' + receipt, localfile.write, 1024)
        localfile.close()
        # ftp.delete(receipt)
        return receipt_number


def placeFile(directory, file_name):
    file_ending = file_name.split('.')[1]
    ftp = connect()
    ftp.cwd(directory)
    ftp.storbinary('STOR ' + file_name, open('temp-files/invoices/'+file_ending+'/' + file_name, 'rb'))
    ftp.quit()

def get_number_of_receipt(receipt):
    disallowed_characters = "abcdefghijklmnopqrstuvwxyz.-!?"

    for character in disallowed_characters:
	    receipt = receipt.replace(character, "")

    return receipt

def grab_files_from_receipt_archive(receipt_number):
    ftp = connect()
    ftp.cwd('/in/AP18dChristen/archive/' + receipt_number)
    path = os.path.join('temp-files/receipt-folders/', receipt_number) 
    try: 
        os.mkdir(path)
        print('Pfad erstellt:' + path)
    except OSError as error: 
        print('Pfad exisitert bereits')  

    for file in ftp.nlst():
        if(re.search("^.*invoice.*$", file)):
            localfile = open('temp-files/receipt-folders/' + receipt_number + '/' + file, 'wb')
            ftp.retrbinary('RETR ' + file, localfile.write, 1024)


