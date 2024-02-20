from tkinter import *
import pickle

class listWindowClass:
    def __init__(self, master):
        self.master = master
        self.listWindow = Toplevel(self.master.root)
        self.listWindow.title("List of Contributions")
        self.listWindow.geometry("500x500")

# Hard kodet member list "temporary"

        members = [
            'Hans Hansen',
            'Klaus Klausen',
            'Ole Olsen',
            'Bent Bentsen',
            'Peter Petersen',
            'Anders Andersen',
            'Jens Jensen',
            'Ib Ibsen'
        ]

        Label(self.listWindow, text="List of Members").pack()

        for member in members:
            Label(self.listWindow, text=member).pack()
