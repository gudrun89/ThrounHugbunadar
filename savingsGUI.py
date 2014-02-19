#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx
from Account import *
from startGUI import *

class savingsGUI(wx.Frame):

    def __init__(self, parent, title):    
        super(savingsGUI, self).__init__(parent, title=title,size=(550, 450))
        self.InitUI()
        self.Show()
        self.userAccounts = []

    def InitUI(self):
      
        panel = wx.Panel(self)
        sizer = wx.GridBagSizer(5, 5)

        # Window title
        guiTitle = wx.StaticText(panel, label="Savings")
        titleFont = wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.BOLD)             # TO-DO: Breyta fontinum, er ljotur nuna
        guiTitle.SetFont(titleFont)
        sizer.Add(guiTitle, pos=(0, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=15)
        line = wx.StaticLine(panel)
        sizer.Add(line, pos=(1, 0), span=(1, 5), flag=wx.EXPAND|wx.BOTTOM, border=10)

        # Account type combo box
        accType = wx.StaticText(panel, label="Account Type")
        sizer.Add(accType, pos=(2, 0), flag=wx.LEFT, border=10)
        accs = [acc.__name__ for acc in Account.__subclasses__()]
        self.accTypeInput = wx.ComboBox(panel, choices=accs, style=wx.CB_READONLY)
        #self.accTypeInput.SetValue(accs[0])
        self.accTypeInput.Bind(wx.EVT_COMBOBOX, self.onAccTypeChange)
        sizer.Add(self.accTypeInput, pos=(2, 1), flag=wx.TOP|wx.EXPAND)

        # Initial credit input box
        creditLabel = wx.StaticText(panel, label='Initial credit')
        sizer.Add(creditLabel, pos=(3,0), flag=wx.LEFT, border=10)
        self.creditInput = wx.TextCtrl(panel)
        sizer.Add(self.creditInput, pos=(3,1), flag=wx.TOP|wx.EXPAND)
        iskLabel = wx.StaticText(panel, label="ISK")
        sizer.Add(iskLabel, pos=(3,2), flag=wx.LEFT|wx.TOP, border = 10)

        # Monthly deposit input box
        depositLabel = wx.StaticText(panel, label='Monthly deposit')
        sizer.Add(depositLabel, pos=(4,0), flag=wx.LEFT, border=10)
        self.depositInput = wx.TextCtrl(panel)
        sizer.Add(self.depositInput, pos=(4,1), flag=wx.TOP|wx.EXPAND)
        iskLabel = wx.StaticText(panel, label="ISK")
        sizer.Add(iskLabel, pos=(4,2), flag=wx.LEFT|wx.TOP, border = 10)

        # Monthly deposit input box 2
        dep2Label = wx.StaticText(panel, label='Monthly deposit 2')
        sizer.Add(dep2Label, pos=(5,0), flag=wx.LEFT, border=10)
        self.dep2Input = wx.TextCtrl(panel)
        sizer.Add(self.dep2Input, pos=(5,1), flag=wx.TOP|wx.EXPAND)
        iskLabel = wx.StaticText(panel, label="ISK")
        sizer.Add(iskLabel, pos=(5,2), flag=wx.LEFT|wx.TOP, border = 10)

        # Goal credit input box
        goalLabel = wx.StaticText(panel, label="Goal credit")
        sizer.Add(goalLabel, pos=(6, 0), flag=wx.LEFT, border=10)
        self.goalInput = wx.TextCtrl(panel)
        sizer.Add(self.goalInput, pos=(6, 1), flag=wx.TOP|wx.EXPAND)
        iskLabel = wx.StaticText(panel, label="ISK")
        sizer.Add(iskLabel, pos=(6,2), flag=wx.LEFT|wx.TOP, border = 10)

        # Interest input box
        interestLabel = wx.StaticText(panel, label="Interest")
        sizer.Add(interestLabel, pos=(7, 0), flag=wx.LEFT|wx.TOP, border=10)
        self.interestInput = wx.TextCtrl(panel)
        sizer.Add(self.interestInput, pos=(7, 1), flag=wx.TOP|wx.EXPAND, border=5)
        intPercent = wx.StaticText(panel, label="%")
        sizer.Add(intPercent, pos=(7,2), flag=wx.LEFT|wx.TOP, border = 10)

        # Fixed duration input box
        fixedLabel = wx.StaticText(panel, label='Fixed length')
        sizer.Add(fixedLabel, pos=(8, 0), flag=wx.LEFT|wx.TOP, border=10)
        self.fixedInput = wx.TextCtrl(panel)
        sizer.Add(self.fixedInput, pos=(8,1), flag=wx.TOP|wx.EXPAND, border=5)
        monLabel = wx.StaticText(panel, label="Months")
        sizer.Add(monLabel, pos=(8,2), flag=wx.LEFT|wx.TOP, border = 10)

        # Saving duration input box
        durLabel = wx.StaticText(panel, label="Saving duration")
        sizer.Add(durLabel, pos=(9, 0), flag=wx.TOP|wx.LEFT, border=10)
        self.durInput = wx.TextCtrl(panel)
        sizer.Add(self.durInput, pos=(9,1), flag=wx.TOP|wx.EXPAND, border=5)
        monLabel = wx.StaticText(panel, label="Months")
        sizer.Add(monLabel, pos=(9,2), flag=wx.LEFT|wx.TOP, border = 10)

        # Back, OK and Quit buttons
        backButton = wx.Button(panel, label='Back')
        backButton.Bind(wx.EVT_BUTTON, self.onBackButton)
        sizer.Add(backButton, pos=(11, 0), flag=wx.LEFT, border=10)
        
        okButton = wx.Button(panel, label="OK")
        okButton.Bind(wx.EVT_BUTTON, self.onOkButton)
        sizer.Add(okButton, pos=(11, 1))

        compareButton = wx.Button(panel, label="Compare with no deposit")
        compareButton.Bind(wx.EVT_BUTTON, self.onCompareButton)
        sizer.Add(compareButton, pos=(11, 2))

        quitButton = wx.Button(panel, label="Quit")
        quitButton.Bind(wx.EVT_BUTTON, self.onQuitButton)
        sizer.Add(quitButton, pos=(11, 3), flag=wx.BOTTOM|wx.RIGHT, border=5)

        panel.SetSizer(sizer)

    def onAccTypeChange(self, event):
        accTypeNum = event.GetEventObject().GetCurrentSelection()
        acc = Account.__subclasses__()[accTypeNum](0,0)                # creates new instance of the account type
        self.interestInput.SetValue(str(acc.interest*100))
        self.fixedInput.SetValue(str(acc.fixed))

    def onOkButton(self, event):
        accTypeNum = self.accTypeInput.GetCurrentSelection()
        acc = Account.__subclasses__()[accTypeNum](float(self.creditInput.GetValue()), float(self.depositInput.GetValue()))
        if (self.durInput.GetValue() == ''):
            acc.plotAcc(goal=float(self.goalInput.GetValue()))
        else:
            acc.plotAcc(int(self.durInput.GetValue()), float(self.goalInput.GetValue()))

    def onCompareButton(self, event):
        accTypeNum = self.accTypeInput.GetCurrentSelection()
        acc = Account.__subclasses__()[accTypeNum](float(self.creditInput.GetValue()), float(self.depositInput.GetValue()))
        if (self.dep2Input.GetValue() == ''):
            self.dep2Input.SetValue('0')
        noDepAcc = Account.__subclasses__()[accTypeNum](float(self.creditInput.GetValue()), float(self.dep2Input.GetValue()))
        comparePlots(acc, noDepAcc, int(self.durInput.GetValue()), 'Monthly deposit', 'No deposit')

    def onBackButton(self, event):
        self.Close()
        app = wx.App()
        startGUI(None, title="Money Thinker")
        app.MainLoop()

    def onQuitButton(self, event):
        self.Close()
        

if __name__ == '__main__':
  
    app = wx.App()
    savingsGUI(None, title="Money Thinker™")
    app.MainLoop()
