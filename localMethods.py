import datetime

def getCalculatedDate(billDate, addDays):
    date_1 = datetime.datetime.strptime(billDate, "%d.%m.%Y")
    end_date = date_1 + datetime.timedelta(days=addDays)
    return end_date.date().__format__("%d.%m.%Y")

def getCurrentTimestamp():
    return datetime.datetime.now().timestamp()

def getTotalAmount(billData):
    totalBetrag = 0
    for rechungsOptionNr in range(3, len(billData)):
        totalBetrag += float(billData[rechungsOptionNr][5])
    return '000' + str(round(totalBetrag)) + '000'


def get_rechung_nummer_of_receipt(receipt_number):
    rechnung_nummern = []
    with open('temp-files/receipt-folders/' + receipt_number + '/quittungsfile' + receipt_number + '.txt') as infile:
        for line in infile:
             if(int(line.split('--')[0].find('xml')) > 0):
               rechnung_nummern.append(line.split('--')[1].split('/')[1][4:])
    return rechnung_nummern