#!/usr/bin/python3

# http://sebsauvage.net/python/gui/
# http://www.tkdocs.com/tutorial/tree.html

import tkinter
from tkinter import ttk


class UI_Page_operation(tkinter.Tk):
    def __init__(self, parent):
        # tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.page = ttk.Frame(self.parent, padding=(5))
        self.parent.add(self.page, text='Operation')
        self.page.columnconfigure(0, weight=1)
        self.page.rowconfigure(0, weight=1)

        self.conf_add = ttk.Button(self.page, text='Add a node')
        self.label = tkinter.Text(self.page, height=10)

        self.conf_add.grid(column=1, row=3)
        self.label.grid(column=0, row=0)
        pass


class UI_Page_configure(tkinter.Tk):
    def __init__(self, parent):
        # tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.page = ttk.Frame(self.parent, padding=(5))
        
        self.parent.add(self.page, text='Configure')
        self.page.columnconfigure(0, weight=1)
        self.page.rowconfigure(0, weight=1)

        self.conf_table = ttk.Treeview(self.page)
        self.conf_table.insert('', 'end', 'widgets', text='Widget Tour')

        self.conf_add = ttk.Button(self.page, text='Add a node')
        self.conf_remove = ttk.Button(self.page, text='Remove a node')
        self.conf_clean = ttk.Button(self.page, text='Clean all node')

        self.conf_table.grid(column=0, row=0, columnspan=3)
        self.conf_add.grid(column=1, row=3)
        self.conf_remove.grid(column=2, row=3)
        self.conf_clean.grid(column=3, row=3)
        pass


class UI_LabTool(tkinter.Tk):
    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.nb = ttk.Notebook(self)
        self.page_oper = UI_Page_operation(self.nb)
        self.page_conf = UI_Page_configure(self.nb)
        self.nb.pack(expand=1, fill="both")
        pass


if __name__ == '__main__':
    app = UI_LabTool(None)
    app.title("Lab Tool")
    app.mainloop()
