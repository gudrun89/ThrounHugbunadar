#!/usr/bin/python
# -*- coding: utf-8 -*-

# newclass.py

import wx

class startGUI(wx.Frame):
  
    def __init__(self, parent, title):    
        super(startGUI, self).__init__(parent, title=title, 
        size=(250, 80))
    
        self.InitUI()
        self.Centre()
        self.Show() 
        
    def InitUI(self):
      
        panel = wx.Panel(self)
        
        sizer = wx.GridBagSizer(2, 2)

        button1 = wx.Button(panel, label='Savings')
        sizer.Add(button1, pos=(1,1))
        
        button2 = wx.Button(panel, label='Loan Repayment')
        sizer.Add(button2, pos=(1,2))
           
        
        sizer.AddGrowableCol(2)
        
        panel.SetSizer(sizer)
    
    
if __name__ == '__main__':
  
    app = wx.App()
    startGUI(None, title="Money Thinker™")
    app.MainLoop()
