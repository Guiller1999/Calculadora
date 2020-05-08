from tkinter import StringVar
from calculator import validations

class Operaciones():

    def __init__(self):

        self.screenText = StringVar()
        self.expr_math = ""
        self.expr_result = StringVar()
        self.num = ""
        self.operator = ""
        self.result = ""


    def push_button(self, button):
        
        values = validations.validate_numberEntry(button, self.screenText.get(), self.num, self.expr_math)

        self.num = values[0]
        self.screenText.set(values[1])
        self.expr_math = values[2]

    def resultado(self):
        
        try:
            self.result = str(eval(self.expr_math))
            self.expr_result.set(self.result)
        except SyntaxError:
            self.screenText.set("Syntaxis Error")
        except ZeroDivisionError:
            self.screenText.set("Math Error")
        except TypeError:
            self.screenText.set("Type Error")
        except SyntaxWarning:
            self.screenText.set("Syntaxis warning")

        self.operator = ""

    def push_operation(self, button):

        self.operator = button
        values = validations.validate_operationEntry(self.operator, self.screenText.get(), self.expr_math)
        self.screenText.set(values[0])
        self.expr_math = values[1]
        self.num = ""

    
    def clear_all(self):

        self.screenText.set("")
        self.expr_result.set("")
        self.expr_math = ""
        self.num = ""
    
    def push_parentesis(self, button):

        values = validations.validate_parenthesisEntry(button, self.screenText.get(), self.expr_math)
        self.screenText.set(values[0])
        self.expr_math = values[1]

    def delete(self):

        texto = self.screenText.get()
        last_character = texto[len(texto) - 1 : len(texto)]
        texto = texto[0 : len(texto) - 1]

        self.screenText.set(texto)

        values = validations.validate_characterDelete(last_character, self.expr_math, self.num)
        self.expr_math = values[0]
        self.num = values[1]

    def potencia(self, button):

        values = validations.validate_powEntry(button, self.screenText.get(), self.expr_math)
        self.screenText.set(values[0])
        self.expr_math = values[1]
        self.num = ""

    def get_resultado(self):
        
        self.screenText.set(self.screenText.get() + str(self.result))
        self.expr_math += str(self.result)

    
    def insertPI(self, button):

        values = validations.validate_numberPIEntry(button, self.screenText.get(), self.expr_math)
        self.screenText.set(values[0])
        self.expr_math = values[1]
        self.num = ""