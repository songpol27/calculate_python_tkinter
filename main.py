import tkinter as tk
from tkinter import ttk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        self.expression = ""
        self.input_text = tk.StringVar()
        self.angle_mode = 'Deg'

        self.input_frame = tk.Frame(self.root, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=1)
        self.input_frame.pack(side=tk.TOP)
        
        self.input_field = tk.Entry(self.input_frame, font=('arial', 18, 'bold'), textvariable=self.input_text, width=50, bg="#eee", bd=0, justify=tk.RIGHT)
        self.input_field.grid(row=0, column=0)
        self.input_field.pack(ipady=10)
        
        self.buttons_frame = tk.Frame(self.root, width=312, height=272.5, bg="grey")
        self.buttons_frame.pack()
        
        self.create_buttons()

    def create_buttons(self):
        buttons = [
            ('Rad', 1, 0), ('Deg', 1, 1), ('x!', 1, 2), ('(', 1, 3),(')', 1, 4),('%', 1, 5),('AC', 1, 6),
            ('Inv', 2, 0), ('Sin', 2, 1), ('ln', 2, 2), ('7', 2, 3),('8', 2, 4),('9', 2, 5),('/', 2, 6),
            ('Pi', 3, 0), ('Cos', 3, 1), ('log', 3, 2), ('4', 3, 3),('5', 3, 4),('6', 3, 5),('x', 3, 6),
            ('e', 4, 0), ('Tan', 4, 1), ('root', 4, 2), ('1', 4, 3),('2', 4, 4),('3', 4, 5),('-', 4, 6),
            ('Ans', 5, 0), ('EXP', 5, 1), ('x^y', 5, 2), ('0', 5, 3),('.', 5, 4),('=', 5, 5),('+', 5, 6),
        ]
        
        for (text, row, col) in buttons:
            self.create_button(text, row, col)
    
    def create_button(self, text, row, col):
        if text == '=':
            btn = tk.Button(self.buttons_frame, text=text, fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=self.calculate)
        elif text == 'AC':
            btn = tk.Button(self.buttons_frame, text=text, fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=self.clear)
        elif text in ('Sin', 'Cos', 'Tan', 'ln', 'log', 'root', 'Pi', 'e', 'x!', 'EXP', 'x^y'):
            btn = tk.Button(self.buttons_frame, text=text, fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda t=text: self.advanced_function(t))
        elif text in ('Deg', 'Rad', 'Inv'):
            btn = tk.Button(self.buttons_frame, text=text, fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda t=text: self.mode_function(t))
        else:
            btn = tk.Button(self.buttons_frame, text=text, fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda t=text: self.click(t))
        btn.grid(row=row, column=col, padx=1, pady=1)

    def click(self, item):
        self.expression += str(item)
        self.input_text.set(self.expression)

    def clear(self):
        self.expression = ""
        self.input_text.set("")

    def calculate(self):
        try:
            self.expression = self.expression.replace('x', '*').replace('÷', '/')
            result = str(eval(self.expression))
            self.input_text.set(result)
            self.expression = result
        except Exception as e:
            self.input_text.set("Error")
            self.expression = ""

    def advanced_function(self, func):
        try:
            if func == 'Sin':
                self.expression = str(math.sin(math.radians(float(self.expression))) if self.angle_mode == 'Deg' else math.sin(float(self.expression)))
            elif func == 'Cos':
                self.expression = str(math.cos(math.radians(float(self.expression))) if self.angle_mode == 'Deg' else math.cos(float(self.expression)))
            elif func == 'Tan':
                self.expression = str(math.tan(math.radians(float(self.expression))) if self.angle_mode == 'Deg' else math.tan(float(self.expression)))
            elif func == 'ln':
                self.expression = str(math.log(float(self.expression)))
            elif func == 'log':
                self.expression = str(math.log10(float(self.expression)))
            elif func == 'root':
                self.expression = str(math.sqrt(float(self.expression)))
            elif func == 'Pi':
                self.expression += str(math.pi)
            elif func == 'e':
                self.expression += str(math.e)
            elif func == 'x!':
                self.expression = str(math.factorial(int(self.expression)))
            elif func == 'EXP':
                self.expression += 'e'
            elif func == 'x^y':
                self.expression += '**'
            self.input_text.set(self.expression)
        except Exception as e:
            self.input_text.set("Error")
            self.expression = ""

    def mode_function(self, func):
        if func == 'Deg':
            self.angle_mode = 'Deg'
        elif func == 'Rad':
            self.angle_mode = 'Rad'
        elif func == 'Inv':
            pass  # Implement inverse function handling if necessary

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
