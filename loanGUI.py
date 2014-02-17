#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx
from Loan import *
from Account import *
from verdbolga import *
from startGUI import *

class loanGUI(wx.Frame):

    def __init__(self, parent, title):    
        super(loanGUI, self).__init__(parent, title=title, size=(750, 500))
        self.userLoans = []
        self.InitUI()
        self.Show()

    def InitUI(self):

        panel = wx.Panel(self)
        sizer = wx.GridBagSizer(10, 5)
        
        # Window Title
        guiTitle = wx.StaticText(panel, label="Loan Calculator")
        titleFont = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD)             # TO-DO: Breyta fontinum, er ljotur nuna
        guiTitle.SetFont(titleFont)
        sizer.Add(guiTitle, pos=(0, 0), flag=wx.ALL, border=15)
        line = wx.StaticLine(panel)
        sizer.Add(line, pos=(1, 0), span=(1, 5), flag=wx.EXPAND|wx.BOTTOM, border=10)

        # Loan principal input box
        principalLabel = wx.StaticText(panel, label="Principal")
        sizer.Add(principalLabel, pos=(2, 0), flag=wx.LEFT, border=10)
        self.principalInput = wx.TextCtrl(panel)                                    
        sizer.Add(self.principalInput, pos=(2, 1), flag=wx.TOP|wx.EXPAND)
        iskLabel = wx.StaticText(panel, label="ISK")
        sizer.Add(iskLabel, pos=(2,2), flag=wx.LEFT|wx.TOP, border = 10)

        # Loan duration input box
        durLabel = wx.StaticText(panel, label="Duration")
        sizer.Add(durLabel, pos=(3, 0), flag=wx.LEFT|wx.TOP, border=10)
        self.durInput = wx.TextCtrl(panel)                                          
        sizer.Add(self.durInput, pos=(3, 1),flag=wx.TOP|wx.EXPAND, border=5) 
        monLabel = wx.StaticText(panel, label="Months")
        sizer.Add(monLabel, pos=(3,2), flag=wx.LEFT|wx.TOP, border = 10)

        # Loan interest input box
        interestLabel = wx.StaticText(panel, label="Interest")
        sizer.Add(interestLabel, pos=(4, 0), flag=wx.TOP|wx.LEFT, border=10)
        self.interestInput = wx.TextCtrl(panel)                                     
        sizer.Add(self.interestInput, pos=(4,1), flag=wx.TOP|wx.EXPAND, border=5)
        intPercent = wx.StaticText(panel, label="%")
        sizer.Add(intPercent, pos=(4,2), flag=wx.LEFT|wx.TOP, border = 10)

        # Loan inflation input box   
        inflationLabel = wx.StaticText(panel, label="Inflation")
        sizer.Add(inflationLabel, pos=(5, 0), flag=wx.TOP|wx.LEFT, border=10)
        self.inflationInput = wx.TextCtrl(panel)                                    
        sizer.Add(self.inflationInput, pos=(5,1), flag=wx.TOP|wx.EXPAND, border=5)
        inflPercent = wx.StaticText(panel, label="%")
        sizer.Add(inflPercent, pos=(5,2), flag=wx.LEFT|wx.TOP, border = 10)

        # Default inflation button
        inflButton = wx.Button(panel, label="Default inflation")
        inflButton.Bind(wx.EVT_BUTTON, self.onInflButton)
        sizer.Add(inflButton, pos=(5, 3), flag=wx.LEFT, border=10)
    
        # Loan indexed radio buttons    
        self.indexBox = wx.RadioBox(panel,  label='Indexed', choices=['Yes', 'No'])
        sizer.Add(self.indexBox, pos=(6, 0), flag=wx.LEFT, border=10)

        # Type of payment radio buttons
        self.paymentBox = wx.RadioBox(panel, label='Type of payment', choices=['Even Payment', 'Even Principal reduction'])
        sizer.Add(self.paymentBox, pos=(6, 1), span=(1,3), border=10)

        # Where to put a savings amount
        savingsLabel = wx.StaticText(panel, label="What should I do with my money?")
        sizer.Add(savingsLabel, pos=(2, 3), span=(1,2), flag=wx.LEFT, border=10)
        saveAmountLabel = wx.StaticText(panel, label="Amount")
        sizer.Add(saveAmountLabel, pos=(3, 3), flag=wx.LEFT, border=10)
        self.saveAmountInput = wx.TextCtrl(panel)                                    
        sizer.Add(self.saveAmountInput, pos=(3, 4), flag=wx.TOP|wx.EXPAND)
        savingsButton = wx.Button(panel, label="Calculate")
        savingsButton.Bind(wx.EVT_BUTTON, self.onCalculateButton)
        sizer.Add(savingsButton, pos=(4, 4), flag=wx.LEFT, border=10)

        # List of user loans
        userLoanLabel = wx.StaticText(panel, label="Your loans:")
        sizer.Add(userLoanLabel, pos=(7, 0), flag=wx.LEFT, border=10)
        self.userLoanInput = wx.ComboBox(panel, choices=self.userLoans, style=wx.CB_READONLY)
        self.userLoanInput.Bind(wx.EVT_COMBOBOX, self.onUserLoanChange)
        sizer.Add(self.userLoanInput, pos=(7, 1), span=(1,2), flag=wx.TOP|wx.EXPAND)
        

        # Back, Add, Plot and Cancel buttons
        backButton = wx.Button(panel, label="Back")
        backButton.Bind(wx.EVT_BUTTON, self.onBackButton)
        sizer.Add(backButton, pos=(9, 0), flag=wx.LEFT, border=10)

        addButton = wx.Button(panel, label="Add")
        addButton.Bind(wx.EVT_BUTTON, self.addLoan)         # clicking addButton calls the function addLoan()
        sizer.Add(addButton, pos=(9, 1))

        plotButton = wx.Button(panel, label="Plot")
        plotButton.Bind(wx.EVT_BUTTON, self.plotLoan)       # clicking plotButton calls the function plotLoan()
        sizer.Add(plotButton, pos=(9, 2))

        cancelButton = wx.Button(panel, label="Cancel")
        cancelButton.Bind(wx.EVT_BUTTON, self.onCancelButton)
        sizer.Add(cancelButton, pos=(9, 3))
        
        panel.SetSizer(sizer)


    def plotLoan(self, event):
        prin = self.principalInput.GetValue()
        dur = int(self.durInput.GetValue())
        interest = float(self.interestInput.GetValue())/100.0
        infl = float(self.inflationInput.GetValue())/100.0
        loan = Loan(prin, interest, False, True, dur)
        loan.plotLoanDevelopment()

    def addLoan(self, event):
        prin = self.principalInput.GetValue()
        dur = int(self.durInput.GetValue())
        interest = float(self.interestInput.GetValue())/100.0
        infl = float(self.inflationInput.GetValue())/100.0
        ind = False
        if (self.indexBox.GetSelection() == 0):
            ind = True
        evPaym = False
        if (self.paymentBox.GetSelection() == 0):
            evPaym = True
        loan = Loan(prin, interest, ind , evPaym, dur)
        self.userLoans.append(loan)
        self.userLoanInput.Append(loan.nameString)

    def onCancelButton(self, event):
        self.Close()

    def onBackButton(self, event):
        self.Close()
        app = wx.App()
        startGUI(None, title="Money Thinker™")
        app.MainLoop()

    def onUserLoanChange(self, event):
        loanNum = event.GetEventObject().GetCurrentSelection()
        loan = self.userLoans[loanNum]
        self.principalInput.SetValue(str(loan.principal))
        self.interestInput.SetValue(str(loan.interest*100))
        self.durInput.SetValue(str(loan.months))
        if (loan.indexed):
            self.indexBox.SetSelection(0)
        else:
            self.indexBox.SetSelection(1)
        if (loan.evenPayments):
            self.paymentBox.SetSelection(0)
        else:
            self.paymentBox.SetSelection(1)


    def onCalculateButton(self, event):
        accs = [cls(0,0) for cls in Account.__subclasses__()] 
        maxLn = max([(ln.monthPrinDecrease(float(self.saveAmountInput.GetValue())), ln.nameString) for ln in self.userLoans])
        maxSave = max([(acc.monthProfit(float(self.saveAmountInput.GetValue())), acc.getName()) for acc in accs])
        print max(maxLn, maxSave)
        return max(maxLn, maxSave)

    def onInflButton(self, event):
        self.inflationInput.SetValue(str(averageindexed(276,288)*100))
        
if __name__ == '__main__':
    
    app = wx.App()
    loanGUI(None, title="Money Thinker™")
    app.MainLoop()
