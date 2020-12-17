from tkinter import *
from Window import Window

class Application:
    def __init__(self):
        self._window = None

    def InitializeComponent(self):
        font = ('Helvetica', '14')

        self._window = Window()
        self._window.setSize(460, 450)
        self._window.allowResize(False)

        self.root = self._window
        self.root.configure(bg="black")

        self.root.rowconfigure(0, weight=2)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)
        self.root.rowconfigure(3, weight=1)
        self.root.rowconfigure(4, weight=1)
        self.root.rowconfigure(5, weight=1)
        self.root.columnconfigure(0, weight=1)   
        self.root.columnconfigure(1, weight=1)   
        self.root.columnconfigure(2, weight=1)   
        self.root.columnconfigure(2, weight=1)   

        self.entry = Entry(self.root, font=font, bg="#88F")
        self.entry.grid(column=0, row=0, columnspan=6, sticky='news')

        self.delete = Button(self.root, text="C", bg='#08F', font=font, width=4, height=2)
        self.delete.grid(column=0, row=1, sticky='news')

        self.openBracket = Button(self.root, text="(", bg='#08F', font=font, width=4, height=2)
        self.openBracket.grid(column=1, row=1, sticky='news')

        self.closeBracket = Button(self.root, text=")", bg='#08F', font=font, width=4, height=2)
        self.closeBracket.grid(column=2, row=1, sticky='news')

        self.mod = Button(self.root, text="^", bg='#08F', font=font, width=4, height=2)
        self.mod.grid(column=3, row=1, sticky='news')

        self.b1 = Button(self.root, text="1", bg='#48F', font=font, width=6, height=3)
        self.b1.grid(column=0, row=2, sticky='news')

        self.b2 = Button(self.root, text="2", bg='#48F', font=font, width=6, height=3)
        self.b2.grid(column=1, row=2, sticky='news')

        self.b3 = Button(self.root, text="3", bg='#48F', font=font, width=6, height=3)
        self.b3.grid(column=2, row=2, sticky='news')

        self.b4 = Button(self.root, text="4", bg='#48F', font=font, width=6, height=3)
        self.b4.grid(column=0, row=3, sticky='news')

        self.b5 = Button(self.root, text="5", bg='#48F', font=font, width=6, height=3)
        self.b5.grid(column=1, row=3, sticky='news')

        self.b6 = Button(self.root, text="6", bg='#48F', font=font, width=6, height=3)
        self.b6.grid(column=2, row=3, sticky='news')

        self.b7 = Button(self.root, text="7", bg='#48F', font=font, width=6, height=3)
        self.b7.grid(column=0, row=4, sticky='news')

        self.b8 = Button(self.root, text="8", bg='#48F', font=font, width=6, height=3)
        self.b8.grid(column=1, row=4, sticky='news')

        self.b9 = Button(self.root, text="9", bg='#48F', font=font, width=6, height=3)
        self.b9.grid(column=2, row=4, sticky='news')

        self.b0 = Button(self.root, text="0", bg='#48F', font=font, width=6, height=3)
        self.b0.grid(column=1, row=5, sticky='news')
        
        self.add = Button(self.root, text="+", bg='#08F', font=font, width=4, height=2)
        self.add.grid(column=3, row=2, sticky='news')

        self.sub = Button(self.root, text="-", bg='#08F', font=font, width=4, height=2)
        self.sub.grid(column=3, row=3, sticky='news')

        self.mul = Button(self.root, text="×", bg='#08F', font=font, width=4, height=2)
        self.mul.grid(column=3, row=4, sticky='news')

        self.div = Button(self.root, text="÷", bg='#08F', font=font, width=4, height=2)
        self.div.grid(column=3, row=5, sticky='news')

        self.answer = Button(self.root, text="=", bg='#08F', font=font, width=4, height=2)
        self.answer.grid(column=2, row=5, sticky='news')

        self.tch = Button(self.root, text=".", bg='#08F', font=font, width=4, height=2)
        self.tch.grid(column=0, row=5, sticky='news')

    def EndInit(self):
        self._window.show()
        
