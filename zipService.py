from zipfile import ZipFile, ZIP_DEFLATED
import os


def zip_files():
    zip_directory = 'temp-files/zip-files/zip'
    zip_obj = ZipFile(zip_directory, "w", ZIP_DEFLATED)
    write_in_zip(zip_obj, 'txt')
    write_in_zip(zip_obj, 'xml')
    zip_obj.close()


def write_in_zip(zip_obj, file_ending):
    base_directory = 'temp-files/invoices'
    base_file_name = 'invoice_out'
    abs_src = os.path.abspath(base_directory)
    absname = os.path.abspath(os.path.join(base_directory + '/' + file_ending + '/', base_file_name + '.' + file_ending))
    arcname= absname[len(abs_src) + 1:]
    zip_obj.write(absname, arcname)


def zip(src, dst):
    zf = ZipFile("%s.zip" % (dst), "w", ZIP_DEFLATED)
    abs_src = os.path.abspath(src)
    for dirname, subdirs, files in os.walk(src):
        for filename in files:
            absname = os.path.abspath(os.path.join(dirname, filename))
            arcname = absname[len(abs_src) + 1:]
            print ('zipping %s as %s' % (os.path.join(dirname, filename),
                                        arcname))
            zf.write(absname, arcname)
    zf.close()

zip_files()