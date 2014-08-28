# ! /usr/bin/env python
# -*- coding: utf-8 -*-
#

import wx

import laserbox_gui as q

if __name__ == '__main__':
    app = wx.App()
    z = q.MyFrame1(None)
    z.Show()

    app.MainLoop()


