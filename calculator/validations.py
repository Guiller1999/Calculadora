
# Función que es llamada cuando se pulsa un número
# Se encarga de validar que la expresión para poder ingresar con exito un número y no haya prblemas
# a la hora de evaluar la expresión
def validate_numberEntry(button, screenText, num, expr_math):

    last_num = screenText
    last_num = last_num[len(last_num) - 1 : len(last_num)]

    # Se encarga de validar si el botón pulsado es un número o punto decimal
    if len(num) >= 0 and num != "0" and last_num != ")" and last_num != "π":
        screenText += button
        num += button
        expr_math += button
    elif len(num) == 1 and last_num == "0" and button.isdigit(): # Valida que no hayan ceros inecesarios a la
        text = screenText                                        # izquierda del número ingresado
        text = text[0 : len(text) - 1]
        num = num[0 : len(num) - 1] + button
        expr_math = expr_math[0 : len(expr_math) - 1] + button
        screenText = text + button
    elif last_num == ")" or last_num == "π" and button.isdigit(): # Si el caracter anterior es un ")"
        screenText += "x" + button                                # o "π", se agregue a la expresion el signo
        expr_math += "*" + button                                 # de multiplicación

    return [num, screenText, expr_math]


# Valida el correcto ingreso de los operadores
def validate_operationEntry(operation, screenText, expr_math):

    operators = ["+", "-", "x", "/"]
    last_character = screenText
    last_character = last_character[len(last_character) -1 : len(last_character)]

    # Valida que no se permita ingresar consecutivamente operadores como por ej: ++
    if last_character not in operators:

        # Si el operador a ingresar es la multiplicación se cambia el signo por "*" para que no cause
        # problemas la expresion matemática a calcular
        if operation == "*":
            screenText += "x"
            expr_math += "*"
        else:
            screenText += operation
            expr_math += operation

    return [screenText, expr_math]


# Valida el correcto ingreso de la potencia y se encarga de cambiar el signo de la potencia para 
# que se calcule correctamente la expresión matemática
def validate_powEntry(button, screenText, expr_math):
    
    if button == "^2":
        expr_math += "**2"
    else:
        expr_math += "**("
    
    screenText += button

    return [screenText, expr_math]


# Valida el correcto ingreso de los parentesis
def validate_parenthesisEntry(button, screenText, expr_math):

    last_character = screenText
    last_character = last_character[len(last_character) -1 : len(last_character)]

    if button =="(" and last_character.isdigit():

        screenText += "x" + button
        expr_math += "*("
    else:
        screenText += button
        expr_math += button

    return [screenText, expr_math]


# Valida que se borre correctamente el último caracter de la expresión matemática
# para que no haya errores a la hora de calcular la expresión
def validate_characterDelete(character, expr_math, num):
    
    if character.isdigit():
        expr_math = expr_math[0 : len(expr_math) - 1]
        num = num[0 : len(num) - 1]
    else:
        if character == "^":
            expr_math = expr_math[0 : len(expr_math) - 2]
        elif character == "π":
            expr_math = expr_math[0 : len(expr_math) - 9]
        else:
            expr_math = expr_math[0 : len(expr_math) - 1]
       
    return [expr_math, num]


# Valida el correcto ingreso del número PI
def validate_numberPIEntry(button, screenText, expr_math):

    last_character = expr_math
    last_character = last_character[len(last_character) - 1 : len(last_character)]

    if last_character.isdigit() or last_character == ")":
        screenText += "x" + button
        expr_math += "*3.1415926"
    else:
        screenText += button
        expr_math += "3.1415926"
    
    return [screenText, expr_math]