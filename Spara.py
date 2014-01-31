# Notkun: x = Spara(eign, innb, mark, tegund)
# Fyrir: Ekkert
# Eftir: Nyr Sparireikningur med tilheyrandi eiginleikum
#
# Breytur:
#   eign: Upphafleg eign notanda, ma vera 0
#   innb: Þad sem notandi getur lagt a reikning manadarlega
#   mark: Uppi hvad vill notandi safna uppi
#   tegund: Fyrirframskilgreind tegund reiknings
class Spara:

    #Bua til nyjan reikning
    def __init__(self, eign, innb, mark, tegund):
        self.eign = eign
        self.innb = innb
        self.mark = mark
        if (tegund == 0):   #Tegund 0 er heidursmerki
            self.vextir = 4.2
            self.verdt = 0.0
        elif (tegund == 1): #Tegunr 1 er Sparileid 1
            self.vextir = 1.7
            self.verdt = 4;
        elif (tegund == 2): #Tegund 2 er Sparileid 2
            self.vextir = 1.8
            self.verdt = 4
        elif (tegund == 3): #Tegund 3 er Sparileid 3
            self.vextir = 1.8
            self.verdt = 4;


