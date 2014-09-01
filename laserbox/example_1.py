# ! /usr/bin/env python
# -*- coding: utf-8 -*-
#

import Tkinter
import argparse
import collections


class Params(object):
    def __init__(self):
        self.pcb_x = 100
        self.pcb_y = 160
        self.pcb_h = 25
        self.pcb_spacing = 2
        self.hole_x_spacing = 90
        self.hole_y_spacing = 150
        self.hole_diameter = 3

class Plaatje(object):
    def __init__(self):
        pass


def my_hover(event):
    # print args
    id, = event.widget.find_withtag('current')
    tags = event.widget.gettags('current')
    print 'tags of selected ='
    print tags
    print event.widget.coords(id)
    # if 'text' in tags:  # the current item is the text in the box
    # id = self.canvas.find_withtag(self.canvas.itemcget(id, 'text'))
    # return id


def doe_het_echte_werk(canvas=None, p=None):
    # assert parameters is Params

    if canvas:
        scalefactor = 1
        spacing = 5

        front = [0, 0, p.pcb_x, p.pcb_y]  # x by y
        back = [0, 0, p.pcb_x, p.pcb_y]  # x by y
        left = [0, 0, p.pcb_h, p.pcb_y]  #
        right = [0, 0, p.pcb_h, p.pcb_y]  #
        top = [0, 0, p.pcb_x, p.pcb_h]  #
        bot = [0, 0, p.pcb_x, p.pcb_h]  #

        # calculate mounting hole
        cx = p.pcb_x / 2.0
        dy = p.pcb_y / 2.0

        pcb_holes = list()
        hx = p.hole_x_spacing / 2.0
        hy = p.hole_y_spacing / 2.0

        pcb_holes.append((cx - hx, dy - hy, p.hole_diameter, 'gat-1'))
        pcb_holes.append((cx - hx, dy + hy, p.hole_diameter, 'gat-2'))
        pcb_holes.append((cx + hx, dy - hy, p.hole_diameter, 'gat-3'))
        pcb_holes.append((cx + hx, dy + hy, p.hole_diameter, 'gat-4'))

        parameters = {'outline': '#FFFFFF', 'fill': '#60e060', 'activefill': '#404080'}
        front_rect = canvas.create_rectangle(front, tag='FRONT', **parameters)
        print front_rect
        canvas.move(front_rect, spacing, spacing)

        mybox = canvas.bbox(front_rect)
        back_rect = canvas.create_rectangle(back, tag='BACK', **parameters)
        canvas.move(back_rect, mybox[2] + spacing, spacing)
        # gaten in de back
        # for h in pcb_holes:

        mybox = canvas.bbox(back_rect)
        left_rect = canvas.create_rectangle(left, tag='LEFT', **parameters)
        canvas.move(left_rect, mybox[2] + spacing, spacing)

        mybox = canvas.bbox(left_rect)
        right_rect = canvas.create_rectangle(right, tag='RIGHT', **parameters)
        canvas.move(right_rect, mybox[2] + spacing, spacing)

        # nu de top en bottom plaatjes (niet front en back)
        mybox = canvas.bbox(front_rect)
        top_rect = canvas.create_rectangle(top, tag='TOP', **parameters)
        # verschuif naar onder de Front rectangle
        canvas.move(top_rect, spacing, mybox[3] + spacing)

        mybox = canvas.bbox(back_rect)
        bottom_rect = canvas.create_rectangle(bot, tag='BOTTOM', **parameters)
        canvas.move(bottom_rect, mybox[0], mybox[3] + spacing)

        mybox = canvas.bbox(right_rect)
        pcb_rect = canvas.create_rectangle(bot, tag='PCB', **parameters)
        canvas.move(pcb_rect, mybox[2] + spacing, spacing)

        # canvas.bind(front_rect, my_hover)

        # canvas.tag_bind(front_rect, '<Enter>', my_hover)
        # canvas.tag_bind(front_rect, '<Leave>', my_hover)
        canvas.tag_bind('all', '<Enter>', my_hover)
        canvas.tag_bind('all', '<Leave>', my_hover)


class my_app(Tkinter.Tk):
    def __init__(self, parent):
        Tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()


    def initialize(self):
        self.grid()

        self.entryVariable = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self, textvariable=self.entryVariable)
        self.entry.grid(column=0, row=0, sticky='EW')
        self.entry.bind("<Return>", self.OnPressEnter)
        self.entryVariable.set(u"Enter text here.")

        button = Tkinter.Button(self, text=u"Click me !", command=self.OnButtonClick)
        button.grid(column=1, row=0)

        self.labelVariable = Tkinter.StringVar()
        label = Tkinter.Label(self, textvariable=self.labelVariable, anchor="w", fg="white", bg="orange")
        label.grid(column=0, row=1, columnspan=2, sticky='EW')
        self.labelVariable.set(u"Hello !")

        self.grid_columnconfigure(0, weight=1)
        self.canvas1 = Tkinter.Canvas(self)
        self.canvas1.config(background="#3c88c9")
        self.canvas1.grid(row=2, column=0, columnspan=2, sticky='NSEW')
        self.grid_rowconfigure(2, weight=1)

        params = Params()
        params.pcb_x=160
        params.pcb_y=100
        params.front_thickness = 6
        params.back_thickness = 6
        params.wall_thickness = 3

        doe_het_echte_werk(canvas=self.canvas1, p=params)

    def OnButtonClick(self):
        self.labelVariable.set(self.entryVariable.get() + " (You clicked the button)")
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)

    def OnPressEnter(self, event):
        self.labelVariable.set(self.entryVariable.get() + " (You pressed ENTER)")
        self.entry.focus_set()
        self.entry.selection_range(0, Tkinter.END)


def main():
    app = my_app(None)
    app.title('my application')
    app.mainloop()


if __name__ == '__main__':
    main()



