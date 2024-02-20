import pickle
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from listWindow import listWindowClass
from payWindow import payWindowClass
from worstWindow import worstWindowClass

class mainWindow:
    def __init__(self):
        self.total = 0
        self.target = 31500 #TODONE Skiftede fra 1 til 31500
        self.root = Tk()

        self.filename = 'betalinger.pk'
        self.fodboldtur = {}
        try:
            infile = open(self.filename, 'rb')
            self.fodboldtur = pickle.load(infile)
            infile.close()
            #Todo Nogen oversættelses tingeling
            #TODONE Ændrede messagebox.showerror titlen og beskeden til dansk
        except FileNotFoundError: #FILEN FINDES IKKE.
            ##TODO: Åbn filen??
            ##TODONE: Giv en advarsel
            messagebox.showerror(parent=self.root, title="Fejl", message="Filen blev ikke fundet!")

        self.update_ui() #TODONE Tilføjede en metodekald til update_ui for at opdatere totalværdien

        velkomst = Label(self.root, text="Velkommen til fodboldtur GUI")
        velkomst.pack(pady=10)

        self.progressLabelText = StringVar()
        self.progressLabelText.set(f"Indsamlet: {self.total} af {self.target} kroner:")
        self.progressLabel = Label(self.root, textvariable=self.progressLabelText)
        self.progressLabel.pack()
        self.progress = Progressbar(self.root, orient=HORIZONTAL, length=250, mode='determinate')
        self.progress['value'] = self.total / self.target * 100
        self.progress.pack(padx=20)

        listButton = Button(self.root, text="Liste over indbetalinger", command=lambda: listWindowClass(self))
        listButton.pack(padx=20, pady=10, side=LEFT)

        payButton = Button(self.root, text="Indbetal", command=lambda: payWindowClass(self))
        payButton.pack(padx=20, pady=10, side=LEFT)

        worstButton = Button(self.root, text="Worst 3", command=lambda: worstWindowClass(self, self.fodboldtur))
        worstButton.pack(padx=20, pady=10, side=LEFT)

        mainloop()

    def update_ui(self): #TODONE Tilføjede en metode til at opdatere brugergrænsefladen (UI)
        self.total = sum(self.fodboldtur.values())

    def gemFilen(self):
        outfile = open(self.filename, 'wb')
        pickle.dump(self.fodboldtur, outfile)
        outfile.close()

if __name__ == '__main__':
    main = mainWindow()
