import ftpKundensystemService
import ftpZahlsystemService
import parseInvoices.csvToTxt as csvToTxt
import parseInvoices.dataToCsv as dataToCsv
import parseInvoices.csvToXml as csvToXml



ftpKundensystemService.grabFile('/out/AP18dChristen')
parsedText = dataToCsv.parse_csv('temp-files/invoices/data/rechnung21003.data')
csvToTxt.parse_to_txt(parsedText)
csvToXml.parse_to_xml(parsedText)
ftpZahlsystemService.placeFiles('/in/AP18dChristen', 'invoice_out')

# Todo:
# DONE rechnungs abholen
# löschen der rechnung
# DONE Rechnung zu txt
# DONE Rechnung zu xml
# DONE abgabe der rechnung als txt
# DONE abgabe der Rechnung als xml
# DONE Abholung der Quittung
# Erstellung der bestätigungsmeldung per Mail
# Zip erstellen
# Zip auf KundenServer legen

# Skript 1: abholung rechnung und abgabe
# Skript 2: Abholen der Quittung, Mail, ZIP


