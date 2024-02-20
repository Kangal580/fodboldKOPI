from tkinter import *
from tkinter import messagebox  # Import messagebox module for error popup

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
        # Opretter etiketter for hver medlem i medlemslisten
        Label(self.listWindow, text="List of Members").pack()

        for member in members:
            Label(self.listWindow, text=member).pack()

        # Viser en fejlmeddelelse i en popup box
        self.show_error_popup("Whoops! Denne del er stadig under kodning, benyt venligst modsatte fortov")

    def show_error_popup(self, message):
        messagebox.showerror("Error", message)

if __name__ == "__main__":
    root = Tk()
    app = listWindowClass(root)
    root.mainloop()
