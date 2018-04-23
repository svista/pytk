#!/usr/bin/python3

# http://sebsauvage.net/python/gui/
# http://www.tkdocs.com/tutorial/tree.html
# http://effbot.org/tkinterbook/

import tkinter
from tkinter import ttk


class UI_frm_node():
    def __init__(self, parent):
        self.parent = parent
        self.initialize()

    def initialize(self):
        pass


class UI_LabTool(tkinter.Tk):
    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)
        self.title("Lab Tool")
        self.geometry('600x400')
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.frm_nodes = ttk.LabelFrame(self, text='Node')
        self.frm_task = ttk.LabelFrame(self, text='Task')
        self.frm_status = ttk.LabelFrame(self, text='Log')

        self.frm_nodes.grid(column=0, row=0, sticky=tkinter.NSEW)
        self.frm_task.grid(column=0, row=1, sticky=tkinter.NSEW)
        self.frm_status.grid(column=0, row=2, sticky=tkinter.NSEW)

        self.lbl_ip = ttk.Label(self.frm_nodes, text="IP")
        self.enty_ip = ttk.Entry(self.frm_nodes)
        self.lbl_ip.grid(row = 0, column = 0, sticky = tkinter.W)
        self.enty_ip.grid(row = 1, column = 0)

        self.lbl_base = ttk.Label(self.frm_nodes, text="Base Folder")
        self.enty_base = ttk.Entry(self.frm_nodes)
        self.lbl_base.grid(row = 0, column = 1, sticky = tkinter.W)
        self.enty_base.grid(row = 1, column = 1)

        self.lbl_user = ttk.Label(self.frm_nodes, text="User")
        self.enty_user = ttk.Entry(self.frm_nodes)
        self.lbl_user.grid(row = 0, column = 2, sticky = tkinter.W)
        self.enty_user.grid(row = 1, column = 2)

        self.lbl_pass = ttk.Label(self.frm_nodes, text="Password")
        self.enty_pass = ttk.Entry(self.frm_nodes)
        self.lbl_pass.grid(row = 0, column = 3, sticky = tkinter.W)
        self.enty_pass.grid(row = 1, column = 3)

        self.btn_add = ttk.Button(self.frm_nodes, text='Add node', command = self.node_insert)
        self.btn_remove = ttk.Button(self.frm_nodes, text='Remove node')
        self.btn_edit = ttk.Button(self.frm_nodes, text='Edit node')
        self.btn_add.grid(column=0, row=0, sticky=tkinter.NSEW)
        self.btn_edit.grid(column=1, row=0, sticky=tkinter.NSEW)
        self.btn_remove.grid(column=3, row=0, sticky=tkinter.NSEW)

        self.tree_node = ttk.Treeview(self.frm_nodes, columns=('IP', 'Base Folder', 'User', 'Password'))
        self.tree_node.heading('#0', text='IP')
        self.tree_node.heading('#1', text='Base Folder')
        self.tree_node.heading('#2', text='User')
        self.tree_node.heading('#3', text='Password')
        self.tree_node.column('#0', stretch=tkinter.YES)
        self.tree_node.column('#1', stretch=tkinter.YES)
        self.tree_node.column('#2', stretch=tkinter.YES)
        self.tree_node.column('#3', stretch=tkinter.YES)
        self.tree_node.grid(column=0, row=3, columnspan=4, sticky=tkinter.NSEW)

        self.frm_nodes.columnconfigure('all', weight=1)

        self.task_stopall = ttk.Button(self.frm_task, text='Stop All Processes')
        self.task_copy = ttk.Button(self.frm_task, text='Copy')
        self.task_stopall.grid(column=0, row=0, sticky=tkinter.NSEW)
        self.task_copy.grid(column=0, row=1, sticky=tkinter.NSEW)
        self.frm_task.columnconfigure('all', weight=1)

        self.log = tkinter.Text(self.frm_status)
        self.log.grid(column=0, row=0, sticky=tkinter.NSEW)

        self.columnconfigure('all', weight=1)
        self.rowconfigure('all', weight=1)
        pass

    def node_insert(self):
        self.tree_node.insert('', 'end', text=self.enty_ip.get(), value=(self.enty_base.get(), self.enty_user.get(), self.enty_pass.get()))
        pass

if __name__ == '__main__':
    app = UI_LabTool(None)
    app.mainloop()
