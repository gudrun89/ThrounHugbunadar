import csv

verdbolga = {}

with open('verdbolga1990-2014.csv', 'rb') as inflation:
    inflationreader = csv.reader(inflation, delimiter=',')
    for row in inflationreader:
        try:
            float(row[1])
            verdbolga[row[0]] = row[1]
        except:
            print row
