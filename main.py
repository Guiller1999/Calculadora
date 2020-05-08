from calculator.calculatorInterface import Calculator
from tkinter import Tk

root = Tk()
root.iconbitmap("Img\\icono.ico")
fr_pr = Calculator(master = root)
fr_pr.pack(fill = "both", expand = True)

root.title("Calculadora")
root.mainloop()