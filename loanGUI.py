#!/usr/bin/python
# -*- coding: utf-8 -*-

# newclass.py

import wx
from Loan import *
from verdbolga import *



class loanGUI(wx.Frame):

    def __init__(self, parent, title):    
        super(loanGUI, self).__init__(parent, title=title, 
            size=(450, 450))

        self.InitUI()
        self.Centre()
        self.Show()
    
   

    def InitUI(self):
      
        panel = wx.Panel(self)
        
        sizer = wx.GridBagSizer(10, 8)
        
    #Titill
        text1 = wx.StaticText(panel, label="Loan Calculator")
        sizer.Add(text1, pos=(0, 1), flag=wx.TOP|wx.LEFT|wx.BOTTOM,
            border=15)

        line = wx.StaticLine(panel)
        sizer.Add(line, pos=(1, 0), span=(1, 5), 
            flag=wx.EXPAND|wx.BOTTOM, border=10)

    #Rammarnir
        text2 = wx.StaticText(panel, label="Principal")
        sizer.Add(text2, pos=(2, 0), flag=wx.LEFT, border=10)

        tc1 = wx.TextCtrl(panel)
        sizer.Add(tc1, pos=(2, 1), span=(1, 1), flag=wx.TOP|wx.EXPAND)
        
        isk = wx.StaticText(panel, label="ISK")
        sizer.Add(isk, pos=(2,2), flag=wx.LEFT, border = 10)

        text6 = wx.StaticText

        text3 = wx.StaticText(panel, label="Duration")
        sizer.Add(text3, pos=(3, 0), flag=wx.LEFT|wx.TOP, border=10)

        tc2 = wx.TextCtrl(panel)
        sizer.Add(tc2, pos=(3, 1), span=(1, 1), flag=wx.TOP|wx.EXPAND,
            border=5)
            
        mon = wx.StaticText(panel, label="Months")
        sizer.Add(mon, pos=(3,2), flag=wx.LEFT, border = 10)

        text4 = wx.StaticText(panel, label="Interest")
        sizer.Add(text4, pos=(4, 0), flag=wx.TOP|wx.LEFT, border=10)
        
        tc3 = wx.TextCtrl(panel)
        sizer.Add(tc3, pos=(4,1), span=(1,1), flag=wx.TOP|wx.EXPAND,
        border=5)
        
        
        interest = wx.StaticText(panel, label="%")
        sizer.Add(interest, pos=(4,2), flag=wx.LEFT, border = 10)
    
        text5 = wx.StaticText(panel, label="Inflation")
        sizer.Add(text5, pos=(5, 0), flag=wx.TOP|wx.LEFT, border=10)

        tc4 = wx.TextCtrl(panel)
        sizer.Add(tc4, pos=(5,1), span=(1,1), flag=wx.TOP|wx.EXPAND,
        border=5)
        
        infla = wx.StaticText(panel, label="%")
        sizer.Add(infla, pos=(5,2), flag=wx.LEFT, border = 10)
    
    
    #Krossarnir
        sb = wx.StaticBox(panel, label="Indexed")

        boxsizer = wx.StaticBoxSizer(sb, wx.VERTICAL)
        boxsizer.Add(wx.RadioButton(panel, label="Yes"),
            flag=wx.LEFT|wx.TOP, border=5)
        boxsizer.Add(wx.RadioButton(panel, label="No"),
            flag=wx.LEFT, border=5)
        sizer.Add(boxsizer, pos=(6, 0), span=(1, 1),
            flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT , border=10)
            
            
        sb = wx.StaticBox(panel, label="Type of payment")
            
        boxsizer = wx.StaticBoxSizer(sb, wx.VERTICAL)
        boxsizer.Add(wx.RadioButton(panel, label="Even payment"),
            flag=wx.LEFT|wx.TOP, border=5)
        boxsizer.Add(wx.RadioButton(panel, label="Even pricipal reduction"),
            flag=wx.LEFT, border=5)
        sizer.Add(boxsizer, pos=(6, 1), span=(1, 1),
            flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT , border=10)

        button3 = wx.Button(panel, label="Back")
        sizer.Add(button3, pos=(9, 0))

        button4 = wx.Button(panel, label="Add")
        sizer.Add(button4, pos=(9, 1))
        
        def teikna():
            #pri = tc1.GetValue()
            #dur = tc2.GetValue()
            #interests = tc3.GetValue()
            #inflation = float(tc4.GetValue())
            lan = Loan(1000, 0.11, False, True, 12)
            lan.plotLoanDevelopment()
        
        button6 = wx.Button(panel, label="Plot", teikna())
        sizer.Add(button6, pos=(9, 2))

        button5 = wx.Button(panel, label="Cancel")
        sizer.Add(button5, pos=(9, 3))

        sizer.AddGrowableCol(2)
        
        panel.SetSizer(sizer)


if __name__ == '__main__':
    
    app = wx.App()
    loanGUI(None, title="Money Thinker™")
    app.MainLoop()
