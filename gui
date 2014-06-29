#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import pymongo
import datetime
import ssl
from pymongo import MongoClient


try:
    import wx
except ImportError:
    raise ImportError,"The wxPython module is required to run this program"

client = MongoClient('data.asteroid.ventures',27017)


class simpleapp_wx(wx.Frame):
    def __init__(self,parent,id,title):
        wx.Frame.__init__(self,parent,id,title)
        self.parent = parent
        self.initialize()

    def initialize(self):
        sizer = wx.GridBagSizer()

        self.username = wx.TextCtrl(self,-1,value=u"User Name")
        sizer.Add(self.username,(0,0),(1,1),wx.EXPAND)
        self.Bind(wx.EVT_TEXT_ENTER, self.OnPressEnter, self.username)

        self.password = wx.TextCtrl(self,-1,value=u"Password")
        sizer.Add(self.password,(1,0),(1,2),wx.EXPAND)
        self.Bind(wx.EVT_TEXT_ENTER, self.OnPressEnter, self.password)

        self.ass = wx.TextCtrl(self,-1,value=u"Favorite Asteroid")
        sizer.Add(self.ass,(2,0),(1,2),wx.EXPAND)
        self.Bind(wx.EVT_TEXT_ENTER, self.OnPressEnter, self.ass)

        button = wx.Button(self,-1,label="Submit")
        sizer.Add(button, (4,1))
        self.Bind(wx.EVT_BUTTON, self.OnButtonClick, button)


        self.label = wx.StaticText(self,-1,label=u'Spaaaaaace')
        self.label.SetBackgroundColour(wx.BLUE)
        self.label.SetForegroundColour(wx.WHITE)
        sizer.Add( self.label, (3,0),(1,2), wx.EXPAND )

        sizer.AddGrowableCol(0)
        self.SetSizerAndFit(sizer)
        self.SetSizeHints(-1,self.GetSize().y,-1,self.GetSize().y );
        self.username.SetFocus()
        self.username.SetSelection(-1,-1)
        self.Show(True)

    def OnButtonClick(self,event):
        self.label.SetLabel( self.username.GetValue() + " (You clicked the button)" )
        self.username.SetFocus()
        self.username.SetSelection(-1,-1)
        db=client.users
        collection=db.users
        data={"user":self.username.GetValue(),
        "password":self.password.GetValue(),
        "fav_ass":self.ass.GetValue(),
        "date":datetime.datetime.utcnow()}

        db.test_user.insert(data)

    def OnPressEnter(self,event):
        self.label.SetLabel( self.entry.GetValue() + " (You pressed ENTER)" )
        self.entry.SetFocus()
        self.entry.SetSelection(-1,-1)

if __name__ == "__main__":
    app = wx.App()
    frame = simpleapp_wx(None,-1,'my application')
    app.MainLoop()