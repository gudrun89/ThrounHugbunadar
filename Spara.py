import math
# Notkun: x = Spara(eign, innb, mark, tegund)
# Fyrir: Efst i koda verdur ad vera, from Spara import *
# Eftir: Nyr Sparireikningur med tilheyrandi eiginleikum
#
# Breytur:
#   eign: Upphafleg eign notanda, ma vera 0
#   innb: Thad sem notandi getur lagt a reikning manadarlega
#   mark: Uppi hvad vill notandi safna uppi
#   tegund: Fyrirframskilgreind tegund reiknings
#   vextir: Avoxtun sparireiknings
#   verdt: Verdtrygging reiknings, ma vera 0
class Spara:

    #Smidur klasans
    #Eftir: Buid er ad gefa upphafsgildi, t.e.a.s. nyr sparireikningur er til
    def __init__(self, eign, innb, mark, tegund):
        self.eign = eign
        self.innb = innb
        self.mark = mark
        if (tegund == 0):   #Tegund 0 er heidursmerki
            self.vextir = 0.042 #Vextir eru 4,2%
            self.verdt = 0.0
        elif (tegund == 1): #Tegunr 1 er Sparileid 1
            self.vextir = 0.017 #Vextir eru 1,7%
            self.verdt = 0.04
        elif (tegund == 2): #Tegund 2 er Sparileid 2
            self.vextir = 0.018 #Vextir eru 1,8%
            self.verdt = 0.04
        elif (tegund == 3): #Tegund 3 er Sparileid 3
            self.vextir = 0.019 #Vextir eru 1,9%
            self.verdt = 0.04


    #Reiknar ut hve marga manudi thad tekur ad safna fyrir markupphaed
    #Notkun: x = Timetoachieve(s)
    #Fyrir: s er breyta af taginu Spara
    #Eftir: x inniheldur fjolda manuda sem tekur ad safna uppi markupphaed
    def Timetoachieve(self):
        manudir = 0
        hofud = self.eign
        raunvextir = (self.verdt + self.vextir)/12  #Arsvextir eru reiknadir manadarlega svo deila tharf med manadarfjolda arsins
        while (self.mark > hofud):
            hofud = math.pow((hofud+self.innb),(1+raunvextir))
            manudir += 1
        return manudir

