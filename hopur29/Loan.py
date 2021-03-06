import math
import matplotlib.pyplot as plt

class Loan:
    # evenPayments = True => Jafngreidslulan: greidslur eru jafn haar
    # evenPayments = False => Jafnar afborganir: hofudstoll laekkar jafn mikid

    # Pre:  principal is the inital principal of the loan, interest is the loan interests, indexed
    #       is true if the loan is indexed, otherwise false. evenPayments if true if the loan is
    #       on even payments (jafngreidslulan), otherwise false (jafnar afborganir). months is
    #       the length of the loan in months, monthPaym is the monthly payment of the loan
    # Post: an object of type Loan has been created
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
        self.nameString = ''

    # Pre:  name is a string with the name of the loan
    # Post: self.nameString = name
    def setName(self, name):
        self.nameString = name

    # Pre:  amount is the amount to be paid on the loan
    # Post: the loan principal has been decreased the principal by 'amount'
    def makePayment(self, amount):
        self.principal -= amount

    # Pre:  amount is the monthly payment if the loan is on even payments, otherwise
    #       it is the monthly decrease of the principal
    # Post: returns for how many months the loan needs to be paid off, given the monthly
    #       payment
    def monthsToPay(self, amount):
        if (self.evenPayments):
            return math.log(self.interest/(amount/self.principal-self.interest)+1)/math.log(self.interest+1)
        return self.principal/float(amount)

    # Pre:  months is the length of the loan in months
    # Post: returns a list of the payment to be paid each month
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

    # Pre:  months is the number of months to calculate the loan development for
    # Post: returns the remaining principal after 'months' months
    def principalAfterMonths(self, months=None):
        if months is None:
            months = self.months
        if (self.evenPayments):
            p = self.principal
            for _ in range(months):
                p = p*(1+self.interest/12) - self.monthPaym
            return p
        return self.principal - (self.principal/float(self.months))*months
    
    # Pre:  months is the number of months to calculate the loan development for
    # Post: returns a list of the remaining balance each month for 'months' months
    def balanceDevelopment(self, months=None):
        if months is None:
            months = self.months
        b = self.principal
        if (self.evenPayments):
            bal = []
            for _ in range(months):
                b = b*(1+self.interest/12) - self.monthPaym
                bal.append(b)
            return bal
        balance = []
        for m in range(months):
            b = b*(1+self.interest/12) - self.monthPaym[m]
            balance.append(b)
        return balance

    # Pre:  months is the number of months to calculate the loan development for
    # Post: returns a list of the accumulated paid balance over months
    def principalPayments(self, months=None):
        if months is None:
            months = self.months
        return map(lambda x: self.principal-x, self.balanceDevelopment(months))

    # Pre:  months is the number of months to calculate the loan development for
    # Post: returns a list of the accumulated paid interests over months
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

    # Pre:  m is the number of months to calculate the loan development for
    # Post: plots the accumulated interests paid, accumulated paid balance and the remaining balance
    def plotLoanDevelopment(self, m=None):
        if m is None:
            m = self.months
        p1, = plt.plot(range(m), self.balanceDevelopment(m), 'r--')
        p2, = plt.plot(range(m), self.principalPayments(m), 'b--')
        p3, = plt.plot(range(m), self.interestPayments(m), 'g--')
        plt.legend([p1, p2, p3], ['Balance', 'Paid Principal', 'Paid Interests'], loc=2)
        plt.xlabel('Months')
        plt.ylabel('ISK')
        plt.title('Loan Development')
        plt.ylim(ymin=0)
        plt.grid()
        plt.show()

 
    # Post: returns how much interests you have paid back at the end of the loan
    def loanBreakdown(self):
        totPaym = sum(self.paymentPerMonth())
        totInterest = totPaym - self.principal
        return [totInterest, totInterest/float(self.principal)]

        
    # Post: plots the breakdown of the loan payments into principal and interests
    def plotBreakdown(self):
        labels = 'Principal', 'Interests'
        amount = [self.principal, self.loanBreakdown()[0]]
        plt.pie(amount, labels=labels)
        plt.show()

    # Pre:  amnt is the amount to pay on the loan
    # Post: returns the decrease in the loan principal after paying amnt on it
    def monthPrinDecrease(self, amnt):
        return amnt*(self.interest/12)
