#!/usr/bin/python
# -*- coding: utf-8 -*-

# newclass.py

import wx

class savingsGUI(wx.Frame):

    def __init__(self, parent, title):    
        super(savingsGUI, self).__init__(parent, title=title, 
            size=(450, 270))

        self.InitUI()
        self.Centre()
        self.Show()     


    def InitUI(self):
      
        panel = wx.Panel(self)
        
        sizer = wx.GridBagSizer(5, 5)

        text1 = wx.StaticText(panel, label="Savings")
        sizer.Add(text1, pos=(0, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, 
            border=15)

        line = wx.StaticLine(panel)
        sizer.Add(line, pos=(1, 0), span=(1, 5), 
            flag=wx.EXPAND|wx.BOTTOM, border=10)


	lanteg = ["Heiðursmerki", "Sparileið 36", "Sparileið 48", "Sparileið 60", "Vaxtarsproti", "Vaxtaþrep", "Fastvaxtareikningur 1", "Fastvaxtareikningur 3", "Fastvaxtareikningur 6", "Fastvaxtareikningur 12"]
	acctype = wx.StaticText(panel, label="Account Type")
        sizer.Add(acctype, pos=(2, 0), flag=wx.LEFT, border=10)
	
	cb1 = wx.ComboBox(panel, choices=lanteg, style=wx.CB_READONLY)
	sizer.Add(cb1, pos=(2, 1), span=(1, 3), flag=wx.TOP|wx.EXPAND)


        text2 = wx.StaticText(panel, label="Goal")
        sizer.Add(text2, pos=(3, 0), flag=wx.LEFT, border=10)

        tc1 = wx.TextCtrl(panel)
        sizer.Add(tc1, pos=(3, 1), span=(1, 3), flag=wx.TOP|wx.EXPAND)

        text3 = wx.StaticText(panel, label="Interest")
        sizer.Add(text3, pos=(4, 0), flag=wx.LEFT|wx.TOP, border=10)

        tc2 = wx.TextCtrl(panel)
        sizer.Add(tc2, pos=(4, 1), span=(1, 3), flag=wx.TOP|wx.EXPAND, 
            border=5)

        text4 = wx.StaticText(panel, label="Savings of time")
        sizer.Add(text4, pos=(5, 0), flag=wx.TOP|wx.LEFT, border=10)

        tc3 = wx.TextCtrl(panel)
        sizer.Add(tc3, pos=(5,1), span=(1,3), flag=wx.TOP|wx.EXPAND,
	    border=5)

        button3 = wx.Button(panel, label='Back')
        sizer.Add(button3, pos=(7, 0), flag=wx.LEFT, border=10)

        button4 = wx.Button(panel, label="Ok")
        sizer.Add(button4, pos=(7, 3))

        button5 = wx.Button(panel, label="Cancel")
        sizer.Add(button5, pos=(7, 4), span=(1, 1),  
            flag=wx.BOTTOM|wx.RIGHT, border=5)

        sizer.AddGrowableCol(2)
        
        panel.SetSizer(sizer)
        
        #self.Bind(wx.EVT_BUTTON, self.OnClose, id =1)
	
	#def OnClose(self,event):
	 # self.Close()

if __name__ == '__main__':
  
    app = wx.App()
    savingsGUI(None, title="Money Thinker™")
    app.MainLoop()
