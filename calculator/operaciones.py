from tkinter import StringVar
from calculator import validations

class Operaciones():

    # Nota:
    # 1) Se usa una variable "num" debido a que así se va acumulando los números que va ingresando el 
    #    usuario hasta que este pulse un botón de operación, con esto se logra poder validar de forma más
    #    fácil el número ingresado, evitando que hayan ceros a la izquierda.
    # 2) Se usa una variable expr_math para almacenar la expresion matemática a calcular, la cual esta
    #    compuesta por el contenido de la variable num y de la variable operator. La diferencia que tiene
    #    el contenido de la variable expr_math con respecto a screenText es que en expr_math ciertas
    #    operaciones se cambian para que se puedan evaluar como por ejemplo para la potencia en vez de
    #    que sea ^2 como nos muestra la calculadora en expr_math se lo guarda como **2.

    def __init__(self):

        self.screenText = StringVar() # Contendrá la expresión matemática que se va a mostrar
        self.expr_math = "" # Guardará la expresión matemática que se va a calcular
        self.expr_result = StringVar() # Guardará el resultado a mostrar al usuario
        self.num = "" # Guardará el número que se está digitando
        self.operator = "" # Guardará el operador de la operación pulsada por el usuario
        self.result = "" # Servirá para mantener el resultado en memoria

    # Función que es llamada cuando se pulsa un boton de la calculadora
    def push_button(self, button):
        
        # Se llama a la función correspondiente para validar el inreso de un número
        # Una vez validado se devuelve el número pulsado, la expresion a mostrar y la
        # expresión matemática a evaluar
        values = validations.validate_numberEntry(button, self.screenText.get(), self.num, self.expr_math)

        self.num = values[0]
        self.screenText.set(values[1])
        self.expr_math = values[2]

    # Función que es llamda cuando se pulsa el signo "=" en la calculadora
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

    # Función que es llamada cuando se pulsa un botón para realizar una operación
    def push_operation(self, button):

        self.operator = button
        values = validations.validate_operationEntry(self.operator, self.screenText.get(), self.expr_math)
        self.screenText.set(values[0])
        self.expr_math = values[1]
        self.num = ""

    # Función que es llamada cuando se pulsa el botón "AC" de la calculadora
    # Se encarga de limpiar la pantalla de la calculadora
    def clear_all(self):

        self.screenText.set("")
        self.expr_result.set("")
        self.expr_math = ""
        self.num = ""
    
    # Función que es llamada cuando se pulsa el botón "(" ó ")"
    def push_parentesis(self, button):

        values = validations.validate_parenthesisEntry(button, self.screenText.get(), self.expr_math)
        self.screenText.set(values[0])
        self.expr_math = values[1]

    # Función que es llamada cuando se pulsa el botón "DEL" de la calculadora
    # Se encarga de eliminar el último carácter que se ingreso
    def delete(self):

        texto = self.screenText.get()
        last_character = texto[len(texto) - 1 : len(texto)]
        texto = texto[0 : len(texto) - 1]

        self.screenText.set(texto)

        values = validations.validate_characterDelete(last_character, self.expr_math, self.num)
        self.expr_math = values[0]
        self.num = values[1]

    # Función que es llamada cuando se pulsa los botones "^2" ó "EXP"
    def potencia(self, button):

        values = validations.validate_powEntry(button, self.screenText.get(), self.expr_math)
        self.screenText.set(values[0])
        self.expr_math = values[1]
        self.num = ""

    # Función que es llamada cuando se pulsa el botón "ANS"
    # Se encarga de obtener el último resultado que se obtuvo
    def get_resultado(self):
        
        self.screenText.set(self.screenText.get() + str(self.result))
        self.expr_math += str(self.result)

    # Función que es llamada cuando se pulsa el botoón "π"
    def insertPI(self, button):

        values = validations.validate_numberPIEntry(button, self.screenText.get(), self.expr_math)
        self.screenText.set(values[0])
        self.expr_math = values[1]
        self.num = ""