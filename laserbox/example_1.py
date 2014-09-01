# ! /usr/bin/env python
# -*- coding: utf-8 -*-
#

import Tkinter
import argparse


def my_hover(event):
    # print args
    id, = event.widget.find_withtag('current')
    tags = event.widget.gettags('current')
    print 'tags of selected ='
    print tags
    # if 'text' in tags:  # the current item is the text in the box
    # id = self.canvas.find_withtag(self.canvas.itemcget(id, 'text'))
    # return id


def doe_het_echte_werk(canvas=None, x=10, y=10, h=3):
    if canvas:
        # canvas.create_polygon([0, 0, 0, 10, 20, 30, 40, 50, 0, 0], outline='red', fill='green')

        scalefactor = 10
        spacing = 5

        front = [0, 0, x * scalefactor, y * scalefactor]  # x by y
        back = [0, 0, x * scalefactor, y * scalefactor]  # x by y
        left = [0, 0, h * scalefactor, y * scalefactor]  #
        right = [0, 0, h * scalefactor, y * scalefactor]  #
        top = [0, 0, x * scalefactor, h * scalefactor]  #
        bot = [0, 0, x * scalefactor, h * scalefactor]  #

        offset = 0
        parameters = {'outline': 'red', 'fill': 'blue', 'activefill': 'gray'}
        front_rect = canvas.create_rectangle(front, tag='FRONT', **parameters)
        print front_rect
        canvas.move(front_rect, spacing, spacing)

        mybox = canvas.bbox(front_rect)
        back_rect = canvas.create_rectangle(back, tag='BACK', **parameters)
        canvas.move(back_rect, mybox[2] + spacing, spacing)

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
        self.canvas1.config(background="black")
        self.canvas1.grid(row=2, column=0, columnspan=2, sticky='NSEW')
        self.grid_rowconfigure(2, weight=1)

        doe_het_echte_werk(canvas=self.canvas1, x=10, y=20, h=2.5)

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



