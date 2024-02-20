from tkinter import *
from tkinter import messagebox

class payWindowClass:
    def __init__(self, master):
        self.master = master
        self.payWindow = Toplevel(self.master.root)
        self.payWindow.title("Pay Window")
        self.payWindow.geometry("200x200")

        Label(self.payWindow, text="Indbetal").pack()

        self.input_name = Entry(self.payWindow)
        self.input_name.pack()

        self.input_amount = Entry(self.payWindow)
        self.input_amount.pack()

        self.status_label = Label(self.payWindow)
        self.status_label.pack()

        self.button = Button(self.payWindow, text="Betal", command=self.registrer_betaling)
        self.button.pack()

    def registrer_betaling(self):
        member = self.input_name.get()
        amount = float(self.input_amount.get())
        if member in self.master.fodboldtur:
            self.master.fodboldtur[member] += amount
        else:
            self.master.fodboldtur[member] = amount
        self.input_name.delete(0, END)
        self.input_amount.delete(0, END)
        self.status_label.config(text="Betalingsregistrering fuldført.")
        self.master.gemFilen()
        self.master.update_ui()
