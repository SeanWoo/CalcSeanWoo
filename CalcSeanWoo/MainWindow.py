from Application import *
from Calculate import parse

class MainWindow(Application):
    def __init__(self, **args):
        super().__init__()
        super().InitializeComponent()

        self.b1.configure(command=lambda: self.butt_MouseClick("1"))
        self.b2.configure(command=lambda: self.butt_MouseClick("2"))
        self.b3.configure(command=lambda: self.butt_MouseClick("3"))
        self.b4.configure(command=lambda: self.butt_MouseClick("4"))
        self.b5.configure(command=lambda: self.butt_MouseClick("5"))
        self.b6.configure(command=lambda: self.butt_MouseClick("6"))
        self.b7.configure(command=lambda: self.butt_MouseClick("7"))
        self.b8.configure(command=lambda: self.butt_MouseClick("8"))
        self.b9.configure(command=lambda: self.butt_MouseClick("9"))
        self.b0.configure(command=lambda: self.butt_MouseClick("0"))
        self.add.configure(command=lambda: self.butt_MouseClick(" + "))
        self.sub.configure(command=lambda: self.butt_MouseClick(" - "))
        self.mul.configure(command=lambda: self.butt_MouseClick(" * "))
        self.div.configure(command=lambda: self.butt_MouseClick(" / "))
        self.tch.configure(command=lambda: self.butt_MouseClick("."))
        self.openBracket.configure(command=lambda: self.butt_MouseClick("("))
        self.closeBracket.configure(command=lambda: self.butt_MouseClick(")"))
        self.mod.configure(command=lambda: self.butt_MouseClick("^"))
        self.delete.configure(command=self.delete_MouseClick)
        self.answer.configure(command=self.answer_MouseClick)


        super().EndInit()

    def butt_MouseClick(self, arg):
        self.entry.insert(len(self.entry.get()), arg)

    def delete_MouseClick(self):
        self.entry.delete(len(self.entry.get())-1, len(self.entry.get()))

    def answer_MouseClick(self):
        result = str(parse(self.entry.get()))
        self.entry.delete(0, len(self.entry.get()))
        self.entry.insert(0, result)

