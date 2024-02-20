from tkinter import *

class worstWindowClass:
    def __init__(self, master, fodboldtur):
        self.master = master
        self.fodboldtur = fodboldtur

        self.worstWindow = Toplevel(self.master.root)
        self.worstWindow.title("De 3 med mest gæld")
        self.worstWindow.geometry("300x100")

        Label(self.worstWindow, text="Top 3 medlemmer, der mangler mest at betale:").pack()

        sorted_debtors = sorted(fodboldtur, key=lambda x: 4500 - fodboldtur[x], reverse=True)
        for i, member in enumerate(sorted_debtors[:3], 1):
            remaining_balance = 4500 - fodboldtur[member]
            Label(self.worstWindow, text=f"{i}. {member}: Mangler {remaining_balance} kr").pack()
