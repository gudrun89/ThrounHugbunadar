#!/usr/bin/python
# -*- coding: utf-8 -*-

# newclass.py

import wx
from loanGUI import *
from savingsGUI import *

class startGUI(wx.Frame):
  
    def __init__(self, parent, title):    
        super(startGUI, self).__init__(parent, title=title, size=(270, 150))
    
        self.InitUI()
        self.Show() 
        
    def InitUI(self):
      
        panel = wx.Panel(self)
        sizer = wx.GridBagSizer(2, 3)

        # Window Title
        guiTitle = wx.StaticText(panel, label="Choose a calculator:")
        #titleFont = wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.BOLD)             # TO-DO: Breyta fontinum, er ljotur nuna
        #guiTitle.SetFont(titleFont)
        sizer.Add(guiTitle, pos=(0, 0), flag=wx.ALL, border=15)
        line = wx.StaticLine(panel)
        sizer.Add(line, pos=(1, 0), span=(1, 3), flag=wx.EXPAND|wx.BOTTOM, border=10)

        savingsButton = wx.Button(panel, label='Savings Calculator')
        savingsButton.Bind(wx.EVT_BUTTON, self.openSavings)
        sizer.Add(savingsButton, pos=(2,0), flag=wx.LEFT, border=5)
        
        loanButton = wx.Button(panel, label='Loan Calculator')
        loanButton.Bind(wx.EVT_BUTTON, self.openLoans)
        sizer.Add(loanButton, pos=(2,1))
                   
        panel.SetSizer(sizer)

    def openSavings(self, event):
        app = wx.App()
        savingsGUI(None, title="Money Thinker")
        app.MainLoop()

    def openLoans(self, event):
        app = wx.App()
        loanGUI(None, title="Money Thinker")
        app.MainLoop()
        
    
if __name__ == '__main__':
  
    app = wx.App()
    startGUI(None, title="Money Thinker")
    app.MainLoop()
