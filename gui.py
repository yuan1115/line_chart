# -*- coding: utf-8 -*-
# @Author: jmx
# @Date:   2019-03-25 11:13:21
# @Last Modified by:   jmx
# @Last Modified time: 2019-03-26 10:10:41
# -*- coding: utf-8 -*-

###########################################################################
# Python code generated with wxFormBuilder (version Jun 17 2015)
# http://www.wxformbuilder.org/
##
# PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid
import images
from os import path

###########################################################################
# Class MyFrame1
###########################################################################


class MyFrame1 (wx.Frame):

    def __init__(self, parent):

        data = path.exists('data')
        if data == False:
            open('data', 'w')

        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title='', pos=wx.DefaultPosition, size=wx.Size(
            407, 377), style=wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_3DLIGHT))
        self.SetIcon(images.AppIcon.GetIcon())

        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1 = wx.StaticText(
            self, wx.ID_ANY, u"数据格式：时间；数据1；数据2（如：3.22；1.54；2）一行一条", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        bSizer1.Add(self.m_staticText1, 0, wx.ALL, 5)

        self.m_textCtrl1 = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(520, 260), wx.TE_MULTILINE)
        bSizer1.Add(self.m_textCtrl1, 0,
                    wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        self.sublimeBnt = wx.Button(
            self, wx.ID_ANY, u"折线图", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.sublimeBnt, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self.listBnt = wx.Button(
            self, wx.ID_ANY, u"历史数据表", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.listBnt, 0, wx.ALL, 5)

        bSizer1.Add(bSizer2, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.sublimeBnt.Bind(wx.EVT_BUTTON, self.sublime)
        self.listBnt.Bind(wx.EVT_BUTTON, self.listact)

    def __del__(self):
        pass


###########################################################################
# Class dataList
###########################################################################

class dataList (MyFrame1):

    def __init__(self, parent):

        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title='历史数据', pos=wx.DefaultPosition, size=wx.Size(
            300, 377), style=wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.TAB_TRAVERSAL)

        self.SetIcon(images.AppIcon.GetIcon())

        bSizer3 = wx.BoxSizer(wx.VERTICAL)

        self.m_grid1 = wx.grid.Grid(
            self, wx.ID_ANY, wx.DefaultPosition, wx.Size(349, -1), 0)

        # Grid
        data = open("data", 'r', encoding='utf-8').readlines()
        for i in data:
            if i == "\n":
                data.remove(i)
        self.m_grid1.CreateGrid(len(data), 2)
        self.m_grid1.EnableEditing(True)
        self.m_grid1.EnableGridLines(True)
        self.m_grid1.EnableDragGridSize(False)
        self.m_grid1.SetMargins(0, 0)

        # Columns
        self.m_grid1.EnableDragColMove(False)
        self.m_grid1.EnableDragColSize(False)
        self.m_grid1.SetColLabelSize(30)
        self.m_grid1.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
        self.m_grid1.SetColLabelValue(0, u"数据1")
        self.m_grid1.SetColLabelValue(1, u"数据2")

        # Rows
        self.m_grid1.EnableDragRowSize(True)
        self.m_grid1.SetRowLabelSize(80)
        self.m_grid1.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        j = 0
        for i in range(len(data)):
            if data[i] == '\n':
                j += 1
                continue
            rows = data[i].replace('；', ';').split(";")
            self.m_grid1.SetRowLabelValue(i-j, rows[0])
            self.m_grid1.SetCellValue(i-j, 0, rows[1])
            self.m_grid1.SetCellValue(i-j, 1, rows[2])

        # Label Appearance

        # Cell Defaults
        self.m_grid1.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        bSizer3.Add(self.m_grid1, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self.SetSizer(bSizer3)
        self.Layout()

    def __del__(self):
        pass
