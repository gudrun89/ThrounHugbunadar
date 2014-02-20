import csv

verdbolga = {}

with open('verdbolga1.csv', 'rb') as inflation:
    inflationreader = csv.reader(inflation, delimiter=',')
    for row in inflationreader:
        try:
            float(row[1])
            verdbolga[row[0]] = row[1]
        except:
            pass

# Tekur inn tolu sem samsvarar dagsetningu(ur rodudum dagsetningum, elsta dagsetningin er nr null og nyjasta nr 288) og reiknar medalverdbolgu a thvi timabili
# Default er reiknud medalverdbolga sidustu 12 manudi, t.e.a.s. verdbolgadefault = averageindexed(276,288)
#Notkun: x = averageindexed(date1, date2)
#Fyrir: date1 og date2 eru heiltolur fra 0 uppi 288
#Eftir: x inniheldur medalverdbolgu milli dagsetninga date1 og date2
def averageindexed(date1, date2):
    dagsetn = sorted(verdbolga.keys())
    
    if (date2 < date1):
        return averageindexed(date2, date1)
    
    elif (date1 == date2):
        return verdbolga[dagsetn[date1]]
    
    sum = 0.0
    for i in range(date1, date2):
        sum += float(verdbolga[dagsetn[i]])
    return (sum/(date2 - date1))/100

