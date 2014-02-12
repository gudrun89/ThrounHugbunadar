from Account import *
from Loan import *

def savingsCalc():
    print '%-6s %-24s %-10s %-14s' % ('No.', 'Account type', 'Interest', 'Fixed period')
    print '--------------------------------------------------------'
    for cls in enumerate(Account.__subclasses__()):
        print '%-6s %-24s %-10.2f %-14.2f' % (cls[0], cls[1].__name__, 100*cls[1](0,0).interest, cls[1](0,0).fixed)
    print '\n'

    accs = Account.__subclasses__()
    accNum = int(raw_input('Enter the number of your account type shown above (0-9) : '))
    deposit = float(raw_input('Enter the amount you want to deposit: '))
    goalCredit = float(raw_input('Enter the goal credit you want to reach: '))
    months = int(raw_input('Enter the number of months you want to deposit: '))
    acc = accs[accNum](deposit, 0)

    print '\n'
    print 'RESULTS'
    print '---------------------------------------------------------'
    if (acc.fixed > months):
        print 'This account is fixed after ', months, ' months'
    else:
        print 'After', months, 'months, you will have', '%-30.2f' % (acc.creditAfterMonths(deposit, months))
    if (acc.fixed > acc.monthsToGoal(goalCredit)):
        print 'After the fixed period,', acc.fixed, 'months, the credit will be', acc.creditAfterMonths(deposit, months)
    else:
        print 'You will reach your goal credit after', int(acc.monthsToGoal(goalCredit)), 'months'
    print getBestAccount(5000,5)
    teiknaspari(acc,months)

def loanCalc():
    principal = float(raw_input('Enter the initial principal of the loan:'))
    intrst = float(raw_input('Enter the interest rate of the loan (e.g. 0.05 for 5%):'))
    evPay = raw_input('Is the loan on even payments (1) or even reduction of principal (2):')
    if (evPay == '1'):
        evenPaym = True
    else:
        evenPaym = False
    mon = int(raw_input('How long should the loan be in months:'))
    lan = Loan(principal, intrst, False, evenPaym, mon)
    lan.plotLoanDevelopment()


if __name__ == "__main__":
    calc = raw_input('Choose the Savings calculator (1) or the Loan calculator (2): ')
    while (calc != 1 or calc != 2):
        if calc == '1':
            savingsCalc()
        elif calc == '2':
            loanCalc()
        else:
            print 'You must enter either 1 or 2'
            calc = raw_input('Choose the Savings calculator (1) or the Loan calculator (2): ')

