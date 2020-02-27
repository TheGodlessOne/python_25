from tkinter import *

class Calc:
    def __init__(self, master):
        self.x = StringVar
        self.y = StringVar
        self.func = {"+": None, "-": None, "*": None, "/": None, "=": None}
        self.num = {str(i+1): None for i in range(9)}
        self.entry = Entry(width = 10, justify=RIGHT)
        self.entry.grid(row = 0, column = 0, columnspan = 4, sticky = W+E)
        it=0
        for i in self.func.keys():
            it += 1
            f = Button(master, text = "{}".format(i))
            self.func[i] = f
            self.func[i].grid(row = it, column = 4)
        for i in self.num.keys():
            n = Button(master, text = "{}".format(int(i)))
            self.num[i] = n
            self.num[i].grid(row = 4-(int(i)-1)//3, column = (int(i)-1)%3)
            self.num[i].bind('<Button-1>', lambda event=int(i), num=i: self.number_action(event, num))
        self.num.update({'0': None})
        self.num['0'] = Button(master, text = "{}".format(0))
        self.num['0'].grid(row = 5, column = 0)
        self.entry.delete(0, END)
        self.entry.icursor(0)

    def number_action(self, event, num):
        self.entry.insert(END, num)


root = Tk()
calc = Calc(root)
root.mainloop()
