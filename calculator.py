from tkinter import *

class Calc:
    def __init__(self, master):
        for row_index in range(5):
            Grid.rowconfigure(master, row_index, weight=1)
        for col_index in range(10):
            Grid.columnconfigure(master, col_index, weight=1)
        self.x = ''
        self.expression = ''
        self.func = ('+', '-', '*', '/', '=', 'C')
        self.buttons = {}

        self.label = Label()
        self.label.grid(row = 0, column = 0, columnspan = 4, sticky = N+S+W+E)

        self.entry = Entry(width = 10, text=0, justify=RIGHT)
        self.entry.grid(row = 1, column = 0, columnspan = 4, sticky = N+S+W+E)
        
        for n in range(10):
            self.add_button(master, str(n))
            self.buttons.update({str(n): self.add_button(master, str(n))})
        
        for f in self.func: 
            self.add_button(master, f)
            self.buttons.update({f: self.add_button(master,f)})

        print(self.buttons)

        self.entry.delete(0, END)
        self.entry.icursor(0)
        
    def add_button(self, master, label): 
        b = Button(master, text = '{}'.format(label))
        if label.isnumeric() is True: 
            b.bind('<Button-1>', 
                        lambda event=int(label), num=label: self.number_action(event, num)
                        )
            if label == '0': 
                b.grid(row = 6, column = 0, sticky = N+S+W+E)
            else: 
                b.grid(row = 5-(int(label)-1)//3, column = (int(label)-1)%3, sticky = N+S+W+E)
        else: 
            if label == '=': 
                b.bind('<Button-1>', self.equal)
                b.grid(row = 6, column = 2, columnspan=2, sticky = N+S+W+E)
            elif label == 'C': 
                b.bind('<Button-1>', self.clear)
                b.grid(row = 2, column = 0, columnspan=2, sticky = N+S+W+E)
            else: 
                b.bind('<Button-1>', 
                            lambda event=label, func=label: self.func_action(event, func)
                            )
                b.grid(row = self.func.index(label)+2, column = 3, sticky = N+S+W+E)
        return b

    def number_action(self, event, num):
        self.entry.insert(END, num)

    def func_action(self, event, func): 
        self.label['text'] = self.expression
        self.x = self.entry.get()
        self.expression += self.x
        self.expression += func
        self.x = ''
        self.label['text'] = self.expression
        self.entry.delete(0, END)
    
    def equal(self, event): 
        self.x = self.entry.get()
        self.expression += self.x
        self.entry.delete(0, END)
        self.label['text'] = self.expression + '=' + str(eval(self.expression))
        self.entry.insert(END, eval(self.expression))
        self.expression = ''
        self.clear(event)

    def clear(self, event): 
        if self.buttons['C']['text'] == 'CE':
            self.entry.delete(0, END)
        elif self.buttons['C']['text'] == 'C': 
            self.label['text'] = ''
            self.expression = ''
            self.entry.delete(0, END)


root = Tk()
calc = Calc(root)
root.mainloop()
