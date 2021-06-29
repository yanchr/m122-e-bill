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