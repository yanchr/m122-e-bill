from os import write
import csv
from typing import DefaultDict

invoiceFileName = 'rechnung21003.data'


def parse_csv():
    csv_data = []
    with open(invoiceFileName, 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in spamreader:
            csv_data.append(row)
    return csv_data

def parse_to_txt(billData):
    invoiceFileTxt = open("files/invoice.txt", "w")
   
    rechnungsNummer=billData[0][0].split('_')[1]
    auftragsNummer=billData[0][1].split('_')[1]
    absendeOrt=billData[0][2]
    rechnungsDatum=billData[0][3]
    rechungsZeit=billData[0][4]
    zahlungsZielInTagen=billData[0][5]

    kundenNummer=billData[1][2]
    name=billData[1][3]
    adresse=billData[1][4]
    wohnort=billData[1][5]
    mwsNummer=billData[1][6]

    endkundenName=billData[2][2]
    endkundenAdresse=billData[2][3]
    endkundenOrt=billData[2][4]

    invoiceFileTxt.write(anfangsText(rechnungsNummer, auftragsNummer, absendeOrt, rechnungsDatum,
    kundenNummer, name, adresse, wohnort, mwsNummer, endkundenName, endkundenAdresse, endkundenOrt))
    
    totalBetrag = 0
    for rechungsOptionNr in range(3, len(billData)):
        rechungsPositionsNummer=billData[rechungsOptionNr][1]
        rechnungsPostitionsBezeichnung=billData[rechungsOptionNr][2]
        anzahlDerEinheit=billData[rechungsOptionNr][3]
        preisProEinheit=billData[rechungsOptionNr][4]
        mengeMalPreis=billData[rechungsOptionNr][5]
        mehrwertsteuer=billData[rechungsOptionNr][6].split('_')[1]
        totalBetrag += float(mengeMalPreis)
        invoiceFileTxt.write(rechungsText(rechungsPositionsNummer, rechnungsPostitionsBezeichnung, anzahlDerEinheit, preisProEinheit, mengeMalPreis, mehrwertsteuer))
     
    invoiceFileTxt.write(endText(endkundenName, endkundenAdresse, endkundenOrt, totalBetrag))

    invoiceFileTxt.close()

def anfangsText(rechnungsNummer, auftragsNummer, absendeOrt, rechungsDatum,
    kundenNummer, name, adresse, wohnort, mwsNummer, endkundenName, endkundenAdresse, endkundenOrt):
    return f"""



{name} 
{adresse}
{wohnort}

{mwsNummer}




{absendeOrt}, den {rechungsDatum}                               {endkundenName}
                                                     {endkundenAdresse}
                                                     {endkundenOrt}

Kundennummer:      {kundenNummer}
Auftragsnummer:    {auftragsNummer}

Rechnung Nr       {rechnungsNummer}
-----------------------"""

def rechungsText(rechungsPositionsNummer, rechnungsPostitionsBezeichnung, anzahlDerEinheit, preisProEinheit, mengeMalPreis, mehrwertsteuer):
    return f"""
    {rechungsPositionsNummer}   {rechnungsPostitionsBezeichnung}              {anzahlDerEinheit}      {preisProEinheit}  CHF      {mengeMalPreis}  {mehrwertsteuer}"""


def endText(endkundenName, endkundenAdresse, endkundenOrt, totalBetrag):
    return f"""
                                                                -----------       
                                                Total CHF         1350.00

                                                MWST  CHF            0.00
















Zahlungsziel ohne Abzug 30 Tage (30.08.2020)

Einzahlungsschein











    {totalBetrag}                    {totalBetrag}     {endkundenName}
                                               {endkundenAdresse}
0 00000 00000 00000                            {endkundenOrt}

Autoleasing AG
Gewerbestrasse 100
5000 Aarau
    """

