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
        self.monthPaym = monthPaym      #listi ef jafnar afborganir (evenPayments = False)
        if self.months is None and self.monthPaym is None:
            raise Exception('Either months or monthPaym must be specified')
        if self.months is None:
            self.months = self.monthsToPay(float(self.monthPaym))
        if self.monthPaym is None:
            if (self.evenPayments):
                self.monthPaym = self.paymentPerMonth(self.months)[0]
            else:
                self.monthPaym = self.paymentPerMonth(self.months)  #ath. tetta er listi
            

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
            payms = [self.principal*(self.interest/12 +  (self.interest/12)/((1+self.interest/12)**months - 1)) for _ in range(months+1)]
            return payms
        payms = []
        p = self.principal
        monPay = self.principal/float(months)
        for m in range(months):
            payms.append(monPay + p*self.interest/12)
            p = p*(1+self.interest/12) - (monPay + p*self.interest/12)
        return payms

    
    # returns the remaining principal after 'months' months
    def principalAfterMonths(self, months=None):
        if months is None:
            months = self.months
        if (self.evenPayments):
            p = self.principal
            for _ in range(months):
                p = p*(1+self.interest/12) - self.monthPaym
            return p
        return self.principal - (self.principal/float(self.months))*months
    

    # returns a list of the remaining balance each month for 'months' months
    def balanceDevelopment(self, months=None):
        if months is None:
            months = self.months
        b = self.principal
        if (self.evenPayments):
            bal = []
            #bal.append(b)
            for _ in range(months):
                b = b*(1+self.interest/12) - self.monthPaym
                bal.append(b)
            return bal
        balance = []
        for m in range(months):
            b = b*(1+self.interest/12) - self.monthPaym[m]
            balance.append(b)
        return balance

    # returns a list of the accumulated paid balance over months
    def principalPayments(self, months=None):
        if months is None:
            months = self.months
        return map(lambda x: self.principal-x, self.balanceDevelopment(months))

    # returns a list of the accumulated paid interests over months
    def interestPayments(self, months=None):
        if months is None:
            months = self.months
        bal = self.balanceDevelopment(months)               # list of balance value over months
        interests = map(lambda x: x*self.interest/12, bal)  # list of interests paid over months
        intPaym = []
        i = 0
        for m in range(months):
            i += interests[m]
            intPaym.append(i)
        return intPaym

    # plots the accumulated interests paid, accumulated paid balance and the remaining balance
    def plotLoanDevelopment(self, m=None):
        if m is None:
            m = self.months
        plt.plot(range(m), self.balanceDevelopment(m), 'r--', range(m), self.principalPayments(m), 'b--', range(m), self.interestPayments(m), 'g--')
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
