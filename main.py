import ftpKundensystemService
import ftpZahlsystemService
import parseInvoices.csvToTxt as csvToTxt
import parseInvoices.dataToCsv as dataToCsv


ftpKundensystemService.grabFile('/out/AP18dChristen', 'rechnung21003.data')
parsedText = dataToCsv.parse_csv('temp-files/invoices/data/rechnung21003.data')
csvToTxt.parse_to_txt(parsedText)
ftpZahlsystemService.placeFile('/in/AP18dChristen', 'invoice.txt')
#ftpZahlsystemService.grabReceipts('/out/AP18dChristen')


