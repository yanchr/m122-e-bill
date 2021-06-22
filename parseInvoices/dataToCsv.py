import csv


def parse_csv(invoiceFileName):
    csv_data = []
    with open(invoiceFileName, 'r') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in spamreader:
            csv_data.append(row)
    return csv_data 