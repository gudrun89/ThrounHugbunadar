import math

class Loan:
    def __init__(self, principal, interest, indexed, months=None, monthPaym=None):
        self.principal = float(principal)
        self.interest = float(interest)
        self.indexed = indexed
        self.months = months
        self.monthPaym = monthPaym
        if self.months is None and self.monthPaym is None:
            raise Exception('Either months or monthPaym must be specified')
        if self.months is None:
            self.months = self.monthsToPay(float(self.monthPaym))
        if self.monthPaym is None:
            self.monthPaym = self.paymentPerMonth(float(self.months))
            

    def makePayment(self, amount):
        self.principal -= amount

    # amount = payment per month
    # returns how many months need to be paid
    def monthsToPay(self, amount):
        print self.interest, self.principal, amount
        return math.log(self.interest/(amount/self.principal-self.interest)+1)/math.log(self.interest+1)

    # months = length of loan
    # returns the payment to be paid each month
    def paymentPerMonth(self, months):
        return self.principal*(self.interest +  self.interest/((1+self.interest)**months - 1))
