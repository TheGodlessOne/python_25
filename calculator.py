from tkinter import *

class Calc:
    def __init__(self, master):
        self.func = {"+": None, "-": None, "*": None, "/": None}
        self.num = {str(i): None for i in range(10)}
        self.entry = Entry(width = 10)
        self.entry.grid(row = 0, column = 0, columnspan = 4, sticky = W+E)
        for i in self.func.keys():
            f = Button(master, text = "{}".format(i))
            self.func[i] = f
            self.func[i].grid(row = 0, column = 4)
        for i in self.num.keys():
            n = Button(master, text = "{}".format(int(i)+1))
            self.num[i] = n
            self.num[i].grid(row = 4-int(i)//3, column = int(i)%3)
        self.eq = Button(master, text = "=")
        self.eq.grid(row = 5, column = 0, sticky = W+E)

root = Tk()
calc = Calc(root)
root.mainloop()
