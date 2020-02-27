from tkinter import *

class Calc:
    def __init__(self, master):
        self.x = ''
        self.expression = ''
        self.func = ('+', '-', '*', '/', '=')
        # self.num = (str(i+1) for i in range(9))
        self.entry = Entry(width = 10, justify=RIGHT)
        self.entry.grid(row = 0, column = 0, columnspan = 4, sticky = W+E)
        
        for n in range(10):
            self.add_button(master, str(n))
        
        for f in self.func: 
            self.add_button(master, f)

        self.entry.delete(0, END)
        self.entry.icursor(0)
        
    def add_button(self, master, label): 
        b = Button(master, text = '{}'.format(label))
        if label.isnumeric() is True: 
            b.bind('<Button-1>', 
                        lambda event=int(label), num=label: self.number_action(event, num)
                        )
            if label == '0': 
                b.grid(row = 5, column = 0)
            else: 
                b.grid(row = 4-(int(label)-1)//3, column = (int(label)-1)%3)
        else: 
            if label == '=': 
                b.bind('<Button-1>', self.equal)
            else: 
                b.bind('<Button-1>', 
                            lambda event=label, func=label: self.func_action(event, func)
                            )
            b.grid(row = self.func.index(label)+1, column = 4)


    def number_action(self, event, num):
        self.entry.insert(END, num)

    def func_action(self, event, func): 
        self.x = self.entry.get()
        self.expression += self.x
        self.expression += func
        self.x = ''
        self.entry.delete(0, END)
    
    def equal(self, event): 
        self.x = self.entry.get()
        self.expression += self.x
        self.entry.delete(0, END)
        self.entry.insert(END, eval(self.expression))


root = Tk()
calc = Calc(root)
root.mainloop()
