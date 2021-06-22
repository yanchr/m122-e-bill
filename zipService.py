from zipfile import ZipFile


def zipFiles():
    zipObj = ZipFile('K821_21003.zip', 'w')
    zipObj.write('K821_21003_invoice.txt')
    zipObj.write('K821_21003_invoice.xml')
    zipObj.close()

zipFiles()    