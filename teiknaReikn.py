import numpy as np
import matplotlib.pyplot as plt
from Account import *
import math
from verdbolga import *


#Notkun: teiknaspari(h, m)
#Fyrir: Acc er hlutur af taginu Account og months er heiltala
#Eftir: Buid er ad teikna voxt reikningsins yfir manadarfjolda m
def teiknaspari(Acc, months):
    
    #Byr til nytt plot
    plt.figure()
    
    #Setur innstaedu reikningsins i C og vexti hans i i
    C = Acc.credit
    i = Acc.interest
    
    #Verdbolga er null reikningur se verdtryggdur
    v = 0
    
    #Naer i verdbolgutolu ef reikn er verdtryggdur, verdbolgan er medaltal sidustu 12 manada
    if (Acc.indexed):
        v = averageindexed(276, 288)
    
    #Teiknar voxt reiknings manadarlega
    for k in range(0, months):
        A = C*(1+(i+v)/12)
        plt.plot([k,k+1],[C,A], color="r")
        C = A
    
    #Teiknar linu thegar reikningur er aflaestur
    if (Acc.fixed > 0):
        plt.plot([Acc.fixed, Acc.fixed],[Acc.credit, C], color="k")

    #Asar grafsins skyrdir
    plt.xlabel("Manudir")
    plt.ylabel("Innistaeda [ISK]")

    #Titill plotts
    plt.title("Voxtur reiknings")

    #Setur grid a grafid
    plt.grid()

    #Synir plottid
    plt.show()


H = Heidursmerki(5000,0)

teiknaspari(H, 12)
