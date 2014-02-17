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

    def monthProfit(self, amnt):
        return amnt * self.interest/12 
    
    #Notkun: self.plotAcc(months)
    #Fyrir: Acc er hlutur af taginu Account og months er heiltala
    #Eftir: Buid er ad teikna voxt reikningsins yfir manadarfjolda months
    def plotAcc(self, months=None, goal=None):

        if (months is None):
            months = int(self.monthsToGoal(goal))
        cred = self.credit
        intrst = self.interest      
        if (self.indexed):
            infl = averageindexed(276, 288) # medaltal verdbolgu sidustu 2 manada ef reikn er verdtryggdur, annars 0
        infl = 0
        
        #Teiknar voxt reiknings manadarlega
        for m in range(0, months):
            A = cred*(1+(intrst+infl)/12)
            if (m < self.fixed):
                p1, = plt.plot([m,m+1],[cred,A], 'r')
            else:
                p2, = plt.plot([m,m+1],[cred,A], 'g')
            cred = A
        if (goal is not None):
            p3, = plt.plot(self.monthsToGoal(goal), goal, 'b*')

        plt.xlabel('Months')
        plt.ylabel('Credit [ISK]')
        plt.title('Account Development')
        plt.grid()
        if (months > self.fixed and goal is not None):
            plt.legend([p1, p2, p3],['Fixed', 'Open', 'Goal'], loc = 2)
        elif(months > self.fixed):
            plt.legend([p1, p2],['Fixed', 'Open'], loc = 2)
        else:
            plt.legend([p1], ['Fixed'], loc = 2)
        plt.show()


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
        

