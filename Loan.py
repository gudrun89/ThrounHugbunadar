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
            self.monthPaym = self.paymentPerMonth(self.principal, float(self.months))
            

    def makePayment(self, amount):
        self.principal -= amount

    # amount = payment per month
    # returns how many months need to be paid
    def monthsToPay(self, amount):
        print self.interest, self.principal, amount
        return math.log(self.interest/(amount/self.principal-self.interest)+1)/math.log(self.interest+1)

    # months = length of loan
    # returns the payment to be paid each month
    def paymentPerMonth(self, principal, months):
        return principal*(self.interest +  self.interest/((1+self.interest)**months - 1))

    def principalAfterMonths(self, months):
        if (months == 1):
            return self.principal - self.paymentPerMonth(self.principal, self.months)
        return self.principalAfterMonths(months-1) - self.paymentPerMonth(self.principalAfterMonths(months-1), self.months-(months-1))


    def loanDevelopment(self, months):
        return [principalAfterMonths(i) for i in range(1,months+1)]

    def plotLoanDevelopment(self, months):
        months = [i for i in range(1,months+1)]
        principals = self.loanDevelopment(months)
        line, = plt.plot(months, principals)
        
