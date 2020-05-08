from tkinter import Tk, Frame, Label, Button, StringVar, PhotoImage
from calculator.operaciones import Operaciones

class Calculator(Frame):

    def __init__(self, master = None):

        super().__init__(master)
        self._operaciones = Operaciones()
        self.expr_math = self._operaciones.screenText
        self.expr_result = self._operaciones.expr_result
        self.crear_widgets()
        self.configureExpansion(2, 1, 1, 1)
        

    def crear_widgets(self):

        self.__fr_north = Frame(self, bg = "White")
        self.__fr_south = Frame(self, bg = "#57CA85")
        self.__fr_north.grid(row = 0, column = 0, sticky = "nswe")
        self.__fr_south.grid(row = 1, column = 0, sticky = "nswe")
        self.configureExpansion(1, 1, 1, 1, widget = self.__fr_north)
        self.configureExpansion(4, 4, 1, 1, widget = self.__fr_south)

        #--------------------- Creando y configurando widget Label -----------------------
        # Estos dos label servirán como pantalla para la calculadora
        # El primer label muestra la expresión matemática que se está realizando
        self.__lblExpresion = Label(self.__fr_north, justify = "right", textvariable = self.expr_math)
        self.__lblExpresion.config(
            bg = "White", 
            bd = 2, 
            relief = "flat", 
            font = ("Helvetica", 20, "italic bold")
        )
        self.__lblExpresion.grid(row = 0, column = 0, sticky = "e", ipadx = 10)

        # Este label se encarga de mostrar el resultado de la expresión matemática mostrada en el primer
        # label
        self.__lbl_resultado = Label(
            self.__fr_north, 
            justify = "left", 
            state = "normal", 
            width = 10, 
            textvariable = self.expr_result)
        self.__lbl_resultado.config(
            bg = "White", 
            bd = 2, 
            relief = "flat", 
            font = ("Helvetica", 18, "italic bold"))
        self.__lbl_resultado.grid(row = 1, column = 0, sticky = "nswe", ipadx = 10)

        # Botones de la calculadora
        #---------------------------- Fila 1 ---------------------------------
        self.setButton("EXP", 5, 2, 0, 0, expansion = "nswe", event = lambda:self._operaciones.potencia("^("))
        self.setButton("^2", 5, 2, 0, 1, expansion = "nswe", event = lambda:self._operaciones.potencia("^2"))
        self.setButton("ANS", 5, 2, 0, 2, expansion = "nswe", event = self._operaciones.get_resultado)
        self.setButton("π", 5, 2, 0, 3, expansion = "nswe", event = lambda:self._operaciones.insertPI("π"))

        #---------------------------- Fila 2 ---------------------------------
        self.setButton("(", 5, 2, 1, 0, expansion = "nswe", event = lambda:self._operaciones.push_parentesis("("))
        self.setButton(")", 5, 2, 1, 1, expansion = "nswe", event = lambda:self._operaciones.push_parentesis(")"))
        self.setButton("DEL", 5, 2, 1, 2, expansion = "nswe", event = self._operaciones.delete)
        self.setButton("AC", 5, 2, 1, 3, expansion = "nswe", event = self._operaciones.clear_all)

        #---------------------------- Fila 3 ---------------------------------
        self.setButton("7", 5, 2, 2, 0, expansion = "nswe", event = lambda:self._operaciones.push_button("7"))
        self.setButton("8", 5, 2, 2, 1, expansion = "nswe", event = lambda:self._operaciones.push_button("8"))
        self.setButton("9", 5, 2, 2, 2, expansion = "nswe", event = lambda:self._operaciones.push_button("9"))
        self.setButton("/", 5, 2, 2, 3, expansion = "nswe", event = lambda:self._operaciones.push_operation("/"))

        #---------------------------- Fila 4 ---------------------------------
        self.setButton("4", 5, 2, 3, 0, expansion = "nswe", event = lambda:self._operaciones.push_button("4"))
        self.setButton("5", 5, 2, 3, 1, expansion = "nswe", event = lambda:self._operaciones.push_button("5"))
        self.setButton("6", 5, 2, 3, 2, expansion = "nswe", event = lambda:self._operaciones.push_button("6"))
        self.setButton("x", 5, 2, 3, 3, expansion = "nswe", event = lambda:self._operaciones.push_operation("*"))

        #---------------------------- Fila 5 ---------------------------------
        self.setButton("1", 5, 2, 4, 0, expansion = "nswe", event = lambda:self._operaciones.push_button("1"))
        self.setButton("2", 5, 2, 4, 1, expansion = "nswe", event = lambda:self._operaciones.push_button("2"))
        self.setButton("3", 5, 2, 4, 2, expansion = "nswe", event = lambda:self._operaciones.push_button("3"))
        self.setButton("-", 5, 2, 4, 3, expansion = "nswe", event = lambda:self._operaciones.push_operation("-"))

        #---------------------------- Fila 6 ---------------------------------
        self.setButton(".", 5, 2, 5, 0, expansion = "nswe", event = lambda:self._operaciones.push_button("."))
        self.setButton("0", 5, 2, 5, 1, expansion = "nswe", event = lambda:self._operaciones.push_button("0"))
        self.setButton("=", 5, 2, 5, 2, expansion = "nswe", event = self._operaciones.resultado)
        self.setButton("+", 5, 2, 5, 3, expansion = "nswe", event = lambda:self._operaciones.push_operation("+"))
            

    # Funcion que se encarga de crear y ubicar los botones de la calculadora
    def setButton(self, textButton, widthButton, heightButton, row, column, borderType = "flat", expansion = None, event = None):

        boton = Button(self.__fr_south, text = textButton, width = widthButton, height = heightButton, justify = "center")
        boton.grid(row = row, column = column, sticky = expansion, padx = 5, pady = 5)
        boton.config(
            relief = borderType, 
            font = ("Helvetica", 16, "bold italic"), 
            borderwidth = 2, 
            bg = "#42E695", 
            fg = "White", 
            command = event
        )


    # Funcion que se encarga de adaptar los widgets Frame a los cambios en la pantalla
    def configureExpansion(self, num_row, num_column, weight_row, weight_column, widget = None):

        # Este for se encarga de configurar cada fila del frame cuando se expande la pantalla
        for i in range(num_row):
            
            # Si el valor del widget es None significa que se va a configurar la expansion
            # del objeto de esta clase
            if widget == None: 
                self.rowconfigure(i, weight = weight_row)
            else:                                               # Caso contrario entonces se configura la 
                widget.rowconfigure(i, weight = weight_row)     # expansion del widget pasado como parametro
        
        # Este for se encarga de configurar cada columna del frame cuando se expande la pantalla
        for i in range(num_column):
            
            if widget == None:
                self.columnconfigure(i, weight = weight_column)
            else:
                widget.columnconfigure(i, weight = weight_row)