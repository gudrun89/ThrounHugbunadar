#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx
from Account import *

class savingsGUI(wx.Frame):

    def __init__(self, parent, title):    
        super(savingsGUI, self).__init__(parent, title=title, size=(500, 350))
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
        cb1 = wx.ComboBox(panel, choices=accs, style=wx.CB_READONLY)
        sizer.Add(cb1, pos=(2, 1), flag=wx.TOP|wx.EXPAND)

        # Initial credit input box
        creditLabel = wx.StaticText(panel, label='Initial credit')
        sizer.Add(creditLabel, pos=(3,0), flag=wx.LEFT, border=10)
        creditInput = wx.TextCtrl(panel)
        sizer.Add(creditInput, pos=(3,1), flag=wx.TOP|wx.EXPAND)

        # Goal credit input box
        goalLabel = wx.StaticText(panel, label="Goal credit")
        sizer.Add(goalLabel, pos=(4, 0), flag=wx.LEFT, border=10)
        goalInput = wx.TextCtrl(panel)
        sizer.Add(goalInput, pos=(4, 1), flag=wx.TOP|wx.EXPAND)

        # Interest input box
        interestLabel = wx.StaticText(panel, label="Interest")
        sizer.Add(interestLabel, pos=(5, 0), flag=wx.LEFT|wx.TOP, border=10)
        interestInput = wx.TextCtrl(panel)
        sizer.Add(interestInput, pos=(5, 1), flag=wx.TOP|wx.EXPAND, border=5)

        # Saving duration input box
        durLabel = wx.StaticText(panel, label="Saving duration")
        sizer.Add(durLabel, pos=(6, 0), flag=wx.TOP|wx.LEFT, border=10)
        durInput = wx.TextCtrl(panel)
        sizer.Add(durInput, pos=(6,1), flag=wx.TOP|wx.EXPAND, border=5)


        # Back, OK and Cancel buttons
        backButton = wx.Button(panel, label='Back')
        sizer.Add(backButton, pos=(8, 0), flag=wx.LEFT, border=10)
        
        okButton = wx.Button(panel, label="OK")
        sizer.Add(okButton, pos=(8, 3))

        cancelButton = wx.Button(panel, label="Cancel")
        sizer.Add(cancelButton, pos=(8, 4), flag=wx.BOTTOM|wx.RIGHT, border=5)

        panel.SetSizer(sizer)


if __name__ == '__main__':
  
    app = wx.App()
    savingsGUI(None, title="Money Thinker™")
    app.MainLoop()
