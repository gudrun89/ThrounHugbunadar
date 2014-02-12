import math
import numpy as np
import matplotlib.pyplot as plt
import math
from verdbolga import *

class Account(object):
    def __init__(self, credit, deposit):
        self.credit = credit
        self.deposit = deposit
        

    def getName(self):
        return self.__class__.__name__

    def transfer(self, amount):
        self.credit += amount

    # Tekur inn upphaed og fjolda manuda
    # Skilar hversu ha upphaedin verdur ordin a reikningnum ad manudunum loknum, ef reikningur er ekki bundinn tad lengi, annars -inf
    def creditAfterMonths(self, deposit, months):
        if (months < self.fixed):
            return float('-infinity')
        return deposit*(self.interest/12+1)**(months)

    # returns number of months required to reach the goal credit
    def monthsToGoal(self, goal):
        return math.ceil(math.log(goal/self.credit)/math.log(self.interest/12+1))

    # returns the development of the account for 'months' months
    def accountDevelopment(self, months):
        return map(lambda x: self.creditAfterMonths(self.credit,x), range(months+1))
        
    

# Inherits from Account
class Heidursmerki(Account):
    def __init__(self, credit, deposit):
        self.interest = 0.042
        self.indexed = False
        self.fixed = 0.33
        self.monthly = True
        super(Heidursmerki, self).__init__(credit, deposit)


# Inherits from Account
class Sparileid36(Account):
    def __init__(self, credit, deposit):
        self.interest = 0.017
        self.indexed = True
        self.fixed = 36
        self.monthly = True
        super(Sparileid36, self).__init__(credit, deposit)


# Inherits from Account
class Sparileid48(Account):
    def __init__(self, credit, deposit):
        self.interest = 0.018
        self.indexed = True
        self.fixed = 48
        self.monthly = True
        super(Sparileid48, self).__init__(credit, deposit)


# Inherits from Account
class Sparileid60(Account):
    def __init__(self, credit, deposit):
        self.interest = 0.019
        self.indexed = True
        self.fixed = 60
        self.monthly = True
        super(Sparileid60, self).__init__(credit, deposit)


# Inherits from Account
class Vaxtasproti(Account):
    def __init__(self, credit, deposit):
        self.interest = 0.036
        self.indexed = False
        self.fixed = 0
        self.monthly = False
        super(Vaxtasproti, self).__init__(credit, deposit)


# Inherits from Account
class Vaxtathrep(Account):
    def __init__(self, credit, deposit):
        if (credit < 1000000):
            self.interest = 0.032
        elif (credit < 5000000):
            self.interest = 0.036
        elif (credit < 20000000):
            self.interest = 0.039
        elif (credit < 75000000):
            self.interest = 0.042
        else:
            self.interest = 0.045
        self.indexed = False
        self.fixed = 0.33
        self.monthly = True
        super(Vaxtathrep, self).__init__(credit, deposit)


# Inherits from Account
class Fastvaxtareikningur1(Account):
    def __init__(self, credit, deposit):
        self.interest = 0.0392
        self.indexed = False
        self.fixed = 1
        self.monthly = True
        super(Fastvaxtareikningur1, self).__init__(credit, deposit)


# Inherits from Account
class Fastvaxtareikningur3(Account):
    def __init__(self, credit, deposit):
        self.interest = 0.0491
        self.indexed = False
        self.fixed = 3
        self.monthly = True
        super(Fastvaxtareikningur3, self).__init__(credit, deposit)


# Inherits from Account
class Fastvaxtareikningur6(Account):
    def __init__(self, credit, deposit):
        self.interest = 0.0506
        self.indexed = False
        self.fixed = 6
        self.monthly = True
        super(Fastvaxtareikningur6, self).__init__(credit, deposit)


# Inherits from Account
class Fastvaxtareikningur12(Account):
    def __init__(self, credit, deposit):
        self.interest = 0.0538
        self.indexed = False
        self.fixed = 12
        self.monthly = True
        super(Fastvaxtareikningur12, self).__init__(credit, deposit)

# Tekur inn upphaed og fjolda manada
# Skilar teim reikningi sem gefur haesta upphaed ad manudunum loknum og hversu ha hun er
def getBestAccount(deposit, months):
    accs = [cls(0,0) for cls in Account.__subclasses__()]   #einn hlutur af hverjum klasa
    return max([(acc.creditAfterMonths(deposit, months), acc) for acc in accs])
        

#Notkun: plotAcc(Acc, months)
#Fyrir: Acc er hlutur af taginu Account og months er heiltala
#Eftir: Buid er ad teikna voxt reikningsins yfir manadarfjolda months
def plotAcc(Acc, months):
    
    #Byr til nytt plot
    plt.figure()
    
    #Setur innstaedu reikningsins i C og vexti hans i i
    C = Acc.credit
    i = Acc.interest
    
    #Verdbolga er null nema reikningur se verdtryggdur
    v = 0
    
    #Naer i verdbolgutolu ef reikn er verdtryggdur, verdbolgan er medaltal sidustu 12 manada
    if (Acc.indexed):
        v = averageindexed(276, 288)
    
    #Teiknar voxt reiknings manadarlega
    for k in range(0, months):
        A = C*(1+(i+v)/12)
        if (k < Acc.fixed):
            p1, = plt.plot([k,k+1],[C,A], 'r')
        else:
            p2, = plt.plot([k,k+1],[C,A], 'g')
        C = A
    
    #Asar grafsins skyrdir
    plt.xlabel("Months")
    plt.ylabel("Credit [ISK]")
    
    #Titill plotts
    plt.title("Account Development")
    
    #Setur grid a grafid
    plt.grid()
    
    #Teiknar legend a graf
    if (months > Acc.fixed):
        plt.legend([p1, p2],['Fixed', 'Open'], loc = 2)
    else:
        plt.legend([p1], ['Fixed'], loc = 2)
    
    #Synir plottid
    plt.show()
