#!/usr/bin/python

import unittest
from Account import * 
from Spara import *
from Loan import *

class Test(unittest.TestCase):
  
  def test_Account1(self):
    acc = Heidursmerki(100,5000)
    self.assertGreater(acc.creditAfterMonths(acc.credit,acc.deposit,12),5000)
      
  def test_Account2(self):
    acc = Sparileid36(100,5000)
    self.assertLess(acc.monthsToGoal(6000),12)
      
  def test_Account3(self):
    acc = Sparileid48(100,5000)
    self.assertGreater(acc.accountDevelopment(12),11)
	
  def test_Account4(self):
	acc1 = Vaxtathrep(999999, 1000)
	acc2 = Vaxtathrep(1000000, 1000)
	self.assertLess(acc1.interest,acc2.interest)
	
  def test_Account5(self):
	acc1 = Vaxtathrep(70000000, 1000)
	acc2 = Vaxtathrep(80000000, 1000)
	self.assertLess(acc1.interest, acc2.interest)

  def test_Spara1(self):
    test = Spara(1000,100,2000,1)
    self.assertGreater(test.Timetoachieve(),5)
    
  def test_Spara2(self):
    avg = averageindexed(200,250)
    self.assertLess(0.02,avg)
    
  def test_Loan1(self):
    t1 = Loan(1000, 5, 0, 0, 12, )
    self.assertLess(t1.makePayment(500), 1000)
    
  def test_Loan2(self):
    t1 = Loan(1000, 5, 0, 0, 12, )
    self.assertGreater(t1.monthsToPay,5)
    
  def test_Loan3(self):
    t1 = Loan(1000, 5, 0, 0, 12, )
    self.assertLess(t1.principalAfterMonths(2),1000)
    
  def test_Loan4(self):
    t1 = Loan(1000, 5, 0, 0, 12, )
    self.assertGreater(t1.loanBreakdown(),50)
    
  def test_Loan5(self):
    t1 = Loan(1000, 5, 0, 0, 12, )
    t2 = [100]
    self.assertLess(t1.principalPayments,t2)
    
    

if __name__== '__main__':
  unittest.main()
