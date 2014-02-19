import math
import numpy as np
import matplotlib.pyplot as plt
import math
from verdbolga import *

class Account(object):
    def __init__(self, credit, deposit):
        self.credit = credit                # initial account credit
        self.deposit = deposit              # monthly deposit on the account
        
    def getName(self):                      # returns the name of the account type
        return self.__class__.__name__

    def transfer(self, amount):             # adds amount to the account credit
        self.credit += amount

    # Tekur inn upphaed og fjolda manuda
    # Skilar hversu ha upphaedin verdur ordin a reikningnum ad manudunum loknum, ef reikningur er ekki bundinn tad lengi, annars -inf
    def creditAfterMonths(self, credit, deposit, months):
        #if (months < self.fixed):
        #    return float('-infinity')
        interest = self.interest
        if (self.indexed):
            interest += averageindexed(276, 288)
        for m in range(months):
            credit += deposit
            credit *= (interest/12+1)
        return credit

    # returns number of months required to reach the goal credit
    def monthsToGoal(self, goal):
        credit = self.credit
        m = 0
        while (credit < goal):
            credit += self.deposit
            credit *= (self.interest/12+1)
            m += 1
        return m

    # returns the development of the account for 'months' months
    def accountDevelopment(self, months):
        return map(lambda x: self.creditAfterMonths(self.credit, self.deposit, x), range(months+1))

    # returns the increased profit after one month from adding amnt on the account
    def monthProfit(self, amnt):
        return amnt * self.interest/12 
    
    #Notkun: self.plotAcc(months)
    #Fyrir: Acc er hlutur af taginu Account, months og goal eru heiltolur 
    #Eftir: Buid er ad teikna voxt reikningsins yfir manadarfjolda months
    def plotAcc(self, months=None, goal=None):

        if (months is None):
            months = int(self.monthsToGoal(goal))

        p2, = plt.plot(range(months+1), self.accountDevelopment(months), 'g')
        p1, = plt.plot(range(min(int(self.fixed), months)+1), self.accountDevelopment(min(self.fixed, months)), 'r')
        if (goal is not None):
            p3, = plt.plot(self.monthsToGoal(goal), goal, 'b*')

        plt.xlabel('Months')
        plt.ylabel('Credit [ISK]')
        plt.title('Account Development')
        plt.grid()
        if (months > self.fixed):
            if (goal is not None):
                plt.legend([p1, p2, p3],['Fixed', 'Open', 'Goal'], loc = 2)
            else:
                plt.legend([p1, p2],['Fixed', 'Open'], loc = 2)
        elif (goal is not None):
            plt.legend([p1,p3], ['Fixed', 'Goal'], loc = 2)
        else:
            plt.legend([p1], ['Fixed'], loc = 2)
        plt.show()


class Heidursmerki(Account):
    def __init__(self, credit, deposit):
        self.interest = 0.042
        self.indexed = False
        self.fixed = 0.33
        self.monthly = True
        super(Heidursmerki, self).__init__(credit, deposit)


class Sparileid36(Account):
    def __init__(self, credit, deposit):
        self.interest = 0.017
        self.indexed = True
        self.fixed = 36
        self.monthly = True
        super(Sparileid36, self).__init__(credit, deposit)


class Sparileid48(Account):
    def __init__(self, credit, deposit):
        self.interest = 0.018
        self.indexed = True
        self.fixed = 48
        self.monthly = True
        super(Sparileid48, self).__init__(credit, deposit)


class Sparileid60(Account):
    def __init__(self, credit, deposit):
        self.interest = 0.019
        self.indexed = True
        self.fixed = 60
        self.monthly = True
        super(Sparileid60, self).__init__(credit, deposit)


class Vaxtasproti(Account):
    def __init__(self, credit, deposit):
        self.interest = 0.036
        self.indexed = False
        self.fixed = 0
        self.monthly = False
        super(Vaxtasproti, self).__init__(credit, deposit)


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


class Fastvaxtareikningur1(Account):
    def __init__(self, credit, deposit):
        self.interest = 0.0392
        self.indexed = False
        self.fixed = 1
        self.monthly = True
        super(Fastvaxtareikningur1, self).__init__(credit, deposit)


class Fastvaxtareikningur3(Account):
    def __init__(self, credit, deposit):
        self.interest = 0.0491
        self.indexed = False
        self.fixed = 3
        self.monthly = True
        super(Fastvaxtareikningur3, self).__init__(credit, deposit)


class Fastvaxtareikningur6(Account):
    def __init__(self, credit, deposit):
        self.interest = 0.0506
        self.indexed = False
        self.fixed = 6
        self.monthly = True
        super(Fastvaxtareikningur6, self).__init__(credit, deposit)


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
    return max([(acc.creditAfterMonths(deposit, 0, months), acc) for acc in accs])

def comparePlots(acc1, acc2, months, accName1=None, accName2=None):
    p1, = plt.plot(range(months+1), acc1.accountDevelopment(months), 'g')
    p2, = plt.plot(range(months+1), acc2.accountDevelopment(months), 'm')

    
    plt.xlabel('Months')
    plt.ylabel('Credit [ISK]')
    plt.title('Account Development')
    plt.grid()
    if (accName1 is None):
        accName1 = 'Account 1'
    if (accName2 is None):
        accName2 = 'Account 2'
    plt.legend([p1,p2], [accName1, accName2], loc = 2)
    plt.show()
        

