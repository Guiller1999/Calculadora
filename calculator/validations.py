
def validate_numberEntry(button, screenText, num, expr_math):

    last_num = screenText
    last_num = last_num[len(last_num) - 1 : len(last_num)]

    if len(num) >= 0 and num != "0" and last_num != ")" and last_num != "π":
        screenText += button
        num += button
        expr_math += button
    elif len(num) == 1 and last_num == "0" and button.isdigit():
        text = screenText
        text = text[0 : len(text) - 1]
        num = num[0 : len(num) - 1] + button
        expr_math = expr_math[0 : len(expr_math) - 1] + button
        screenText = text + button
    elif last_num == ")" or last_num == "π" and button.isdigit():
        screenText += "x" + button
        expr_math += "*" + button

    return [num, screenText, expr_math]


def validate_operationEntry(operation, screenText, expr_math):

    operators = ["+", "-", "x", "/"]
    last_character = screenText
    last_character = last_character[len(last_character) -1 : len(last_character)]

    if last_character not in operators:

        if operation == "*":
            screenText += "x"
            expr_math += "*"
        else:
            screenText += operation
            expr_math += operation

    return [screenText, expr_math]


def validate_powEntry(button, screenText, expr_math):
    
    if button == "^2":
        expr_math += "**2"
    else:
        expr_math += "**("
    
    screenText += button

    return [screenText, expr_math]


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
