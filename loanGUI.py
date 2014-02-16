#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx
from Loan import *
from verdbolga import *


class loanGUI(wx.Frame):

    def __init__(self, parent, title):    
        super(loanGUI, self).__init__(parent, title=title, size=(650, 400))
        self.InitUI()
        self.Show()
        self.userLoans = []

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
    
        # Loan indexed radio buttons    
        self.indexBox = wx.RadioBox(panel,  label='Indexed', choices=['Yes', 'No'])
        sizer.Add(self.indexBox, pos=(6, 0), flag=wx.LEFT, border=10)

        # Type of payment radio buttons
        self.paymentBox = wx.RadioBox(panel, label='Type of payment', choices=['Even Payment', 'Even Principal reduction'])
        sizer.Add(self.paymentBox, pos=(6, 1), border=10)

        # Back, Add, Plot and Cancel buttons
        backButton = wx.Button(panel, label="Back")
        sizer.Add(backButton, pos=(8, 0), flag=wx.LEFT, border=10)
        addButton = wx.Button(panel, label="Add")
        addButton.Bind(wx.EVT_BUTTON, self.addLoan)         # clicking addButton calls the function addLoan()
        sizer.Add(addButton, pos=(8, 1))
        plotButton = wx.Button(panel, label="Plot")
        plotButton.Bind(wx.EVT_BUTTON, self.plotLoan)       # clicking plotButton calls the function plotLoan()
        sizer.Add(plotButton, pos=(8, 2))
        cancelButton = wx.Button(panel, label="Cancel")
        sizer.Add(cancelButton, pos=(8, 3))
        
        panel.SetSizer(sizer)


    def plotLoan(self, event):
        #btn = event.GetEventObject()                   # Getum notad ef vid turfum ad nalgast upplysingar um takkann
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
        loan = Loan(prin, interest, False, True, dur)
        self.userLoans.append(loan)

if __name__ == '__main__':
    
    app = wx.App()
    loanGUI(None, title="Money Thinker™")
    app.MainLoop()
