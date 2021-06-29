import ftpZahlsystemService
import zipService
import mailService
import localMethods
import storeMailInJson


receipt_numbers = ftpZahlsystemService.grab_receipts('/out/AP18dChristen')

for receipt_number in receipt_numbers:
    print(receipt_number)
    zipService.zip_directory(receipt_number)

    rechnung_nummern = localMethods.get_rechung_nummer_of_receipt(receipt_number)

    for rechnung_nummer in rechnung_nummern:
        mail_address = storeMailInJson.get_mail_from_rechnung_nummer(rechnung_nummer)
        #Mail
        mailService.login()
        message = 'Dies ist das Mail mit der Quittung: ' + receipt_number 
        to = mail_address
        mailService.sendMail(message, to, 'temp-files/zip-files', receipt_number + '.zip')
        # mailService.exitServer()
        # EROOR: smtplib.SMTPServerDisconnected: please run connect() first


    



