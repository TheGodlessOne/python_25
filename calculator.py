from tkinter import *

class Calc:
    def __init__(self, master):
        self.func = {"+": None, "-": None, "*": None, "/": None, "=": None}
        self.num = {str(i+1): None for i in range(9)}
        self.entry = Entry(width = 10)
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
        self.num.update({'0': None})
        self.num['0'] = Button(master, text = "{}".format(0))
        self.num['0'].grid(row = 5, column = 0)




for i in range(10):
    print('{0}//3 {1}, {0}%3 {2}'.format(i, i//3, i%3))

root = Tk()
calc = Calc(root)
root.mainloop()
