import math
# Notkun: x = Lan(stada, innb, timi, vextir, verdt)
# Fyrir: Efst i kodanum verdur ad vera: from Lan import *
# Eftir: Nytt lan med tilheyrandi eiginleikum
#
# Breytur:
#   stada: Hver hofurstoll a lani er
#   innb: Þad sem notandi borgar manadarlega i lanid
#   vextir: vextir lans
#   verdt: Verdtrygging lans, 0 ef engin.
class Lan:
    
    #Smidur klasans
    #Byr til nytt lan
    def __init__(self, stada, innb, timi, vextir, verdt):
        self.stada = stada
        self.innb = innb
        self.timi = timi
        self.vextir = vextir
        self.verdt = verdt

    #Notkun: x = TotalPay(l)
    #Fyrir: l er breyta af taginu Lan
    #Eftir: x inniheldur samanlagdan kostnad allra afborgana, t.e.a.s. hversu mikid var borgad til baka alls af lani
    def TotalPay(self):
        

