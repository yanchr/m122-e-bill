from zipfile import ZipFile, ZIP_DEFLATED
import os


def zip_directory(receipt_number):
    base_directory = 'temp-files/receipt-folders/' + receipt_number

    zip_directory = 'temp-files/zip-files/'
    zip_object = ZipFile(zip_directory+receipt_number + '.zip', 'w', ZIP_DEFLATED)
    for root, dirs, files in os.walk(base_directory):
        for file in files:
             zip_object.write(os.path.join(root, file), 
                       os.path.relpath(os.path.join(root, file), 
                                       os.path.join(base_directory, '..')))
      
    zip_object.close()