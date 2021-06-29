import ftpKundensystemService
import ftpZahlsystemService
import parseInvoices.csvToTxt as csvToTxt
import parseInvoices.dataToCsv as dataToCsv
import parseInvoices.csvToXml as csvToXml
import storeMailInJson



file_names = ftpKundensystemService.grab_files('/out/AP18dChristen')

for file_name in file_names:
    parsed_text = dataToCsv.parse_csv('temp-files/invoices/data/' + file_name)
    filename_txt = csvToTxt.parse_to_txt(parsed_text)
    filename_xml = csvToXml.parse_to_xml(parsed_text)
    storeMailInJson.store_mail(parsed_text[1][7], parsed_text[0][0].split('_')[1])
    ftpZahlsystemService.placeFile('/in/AP18dChristen', filename_txt)
    ftpZahlsystemService.placeFile('/in/AP18dChristen', filename_xml)

# Todo:
# löschen der rechnung
# Erstellung der bestätigungsmeldung per Mail
# Zip auf KundenServer legen

# Skript 1: abholung rechnung und abgabe
# Skript 2: Abholen der Quittung, Mail, ZIP


