import math
import matplotlib.pyplot as plt

class Loan:
    # evenPayments = True => Jafngreidslulan: greidslur eru jafn haar
    # evenPayments = False => Jafnar afborganir: hofudstoll laekkar jafn mikid
    def __init__(self, principal, interest, indexed, evenPayments, months=None, monthPaym=None):
        self.principal = float(principal)
        self.interest = float(interest)
        self.indexed = indexed
        self.evenPayments = evenPayments
        self.months = months
        self.monthPaym = monthPaym
        if self.months is None and self.monthPaym is None:
            raise Exception('Either months or monthPaym must be specified')
        if self.months is None:
            self.months = self.monthsToPay(float(self.monthPaym))
        if self.monthPaym is None:
            self.monthPaym = self.paymentPerMonth(self.months)[0]
            

    # decreases the principal by 'amount'
    def makePayment(self, amount):
        self.principal -= amount

    # amount = greidsla a manudi ef jafngreislulan, afborgun hofudstols ef lan a jofnum afborgunum
    # returns how many months need to be paid
    def monthsToPay(self, amount):
        if (self.evenPayments):
            return math.log(self.interest/(amount/self.principal-self.interest)+1)/math.log(self.interest+1)
        return self.principal/float(amount)

    # months = length of loan
    # returns a list of the payment to be paid each month
    def paymentPerMonth(self, months=None):
        if months is None:
            months = self.months
        if (self.evenPayments):
            payms = [self.principal*(self.interest +  self.interest/((1+self.interest)**months - 1)) for _ in range(months+1)]
            return payms
        payms = []
        p = self.principal
        for m in range(months+1):
            payms.append(p/float(months) + p*self.interest)
            p = p - p/float(months)
        return payms

    
    # returns the remaining principal after 'months' months
    def principalAfterMonths(self, months=None):
        if months is None:
            months = self.months
        if (self.evenPayments):
            p = self.principal
            for _ in range(months):
                p *= (1+self.interest)
                p -= self.monthPaym
            return p
        return self.principal - (self.principal/float(self.months))*months
    

    # returns a list of the remaining principal each month for 'months' months
    def loanDevelopment(self, months):
        p = self.principal
        if (self.evenPayments):
            prin = []
            prin.append(p)
            for _ in range(months):
                p *= (1+self.interest)
                p -= self.monthPaym
                prin.append(p)
            return prin
        pr = []
        for m in range(months+1):
            p *= (1+self.interest)
            pr.append(p - (p/float(self.months))*m)
        return pr
        

    # plots the remaining principal as a function of months
    def plotLoanDevelopment(self, months=None):
        if months is None:
            months = self.months
        principals = self.loanDevelopment(months)
        line, = plt.plot(range(0,months+1), principals)
        plt.show()


    # returns how much interests you have paid back at the end of the loan
    def loanBreakdown(self):
        totPaym = sum(self.paymentPerMonth())
        totInterest = totPaym - self.principal
        return [totInterest, totInterest/float(self.principal)]

        
    # plots the breakdown of the loan payments into principal and interests
    def plotBreakdown(self):
        labels = 'Principal', 'Interests'
        amount = [self.principal, self.loanBreakdown()[0]]
        plt.pie(amount, labels=labels)
        plt.show()
