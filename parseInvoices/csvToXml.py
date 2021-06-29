from jinja2.runtime import StrictUndefined
from parseInvoices import dataToCsv
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
from jinja2 import Template, Environment, FileSystemLoader, StrictUndefined
from pathlib import Path
import localMethods



def parse_to_xml(billData):
    file_path_template = 'templates'
    file_path_outcome = 'temp-files/invoices/xml'
    fileName = 'invoice_template.xml'
    env = Environment(loader=FileSystemLoader(file_path_template), trim_blocks=True, lstrip_blocks=True, undefined=StrictUndefined)
    t = env.get_template(fileName)
    test = t.render({
        'rechnung_nummer': billData[0][0].split('_')[1],
        'auftrag_numer': billData[0][1].split('_')[1],
        'rechnung_datum': billData[0][3],
        'rechnung_datum_timestamp': localMethods.getCurrentTimestamp(),
        'rechnung_zahlungsziel': localMethods.getCalculatedDate(billData[0][3], int(billData[0][5].split('_')[1])),
        'herkunft_nummer': billData[1][1],
        'herkunft_name': billData[1][3],
        'herkunft_addresse': billData[1][4],
        'herkunft_ort': billData[1][5],
        'herkunft_mwst': billData[1][6],
        'enkunde_nummer': billData[2][1],
        'enkunde_name': billData[2][2],
        'enkunde_addresse': billData[2][3],
        'enkunde_ort': billData[2][4],
        'total_amount': localMethods.getTotalAmount(billData),
    })
    (Path(file_path_outcome) /'invoice_out.xml').write_text(test)

# def parse_to_xml_3(billDate):
#     filePath = 'temp-files/invoices/xml/invoice_template.xml'
#     tree = ET.parse(filePath)
#     tree.find('.//IC-SENDER/Pid').text = 'test'
#     tree.write(filePath)


# def parse_to_xml_2(billData):
#     file = open('temp-files/invoices/xml/invoice_template.xml', 'rb')
#     lines_of_file = file.readlines()
#     for line in lines_of_file:
#         print(line)

# def parse_to_xml_1(billData):
#     # create the file structure
#     data = ET.Element('data')
#     items = ET.SubElement(data, 'items')
#     item1 = ET.SubElement(items, 'item')
#     item2 = ET.SubElement(items, 'item')
#     item1.set('name','item1')
#     item2.set('name','item2')
#     item1.text = 'item1abc'
#     item2.text = 'item2abc'

#     # create a new XML file with the results
#     mydata = ET.tostring(data)
#     with open("temp-files/invoices/xml/invoice.xml", "wb") as f:
#         f.write(mydata)
