from src.animate_text import animate_text
from src.writing_to_massive import writing_to_massive
from src.is_op import is_op


def calc(expression):  # Calculate Reverse Polish Notation for real
    if len(expression.rstrip()) == 0:
        return "❌ Empty expression"
    
    ln = expression  # Save original expression for output
    expression = expression.rstrip().split()
    stek = []  # Main stack for calculations
    stek_for_steks = []  # Stack for expressions in parentheses
    counting_parentheses = 0  # Parentheses counter
    
    # Animated welcome message
    animate_text("🔢 RPN Calculator Starting...", 0.05, "typing")
    for element in expression:
        if element != '(' and element != ')':
            stek = writing_to_massive(stek, element)
            if stek[0] == "❌ Error: Not enough digits":
                return "❌ Error: Not enough digits"
            elif stek[0] == "❌ Error: Division by zero!":
                return "❌ Error: Division by zero!"
            elif stek[0] == "❌ Error: Invalid operands for integer division":
                return "❌ Error: Invalid operands for integer division"
            elif stek[0] == f"❌ Error: I don`t know what to do with the '{element}'":
                return f"❌ Error: I don`t know what to do with the '{element}'"
        elif element == '(':
            counting_parentheses += 1
            stek_for_steks.append(stek)  # Save current stack state
            stek = []  # Start new stack for parentheses content
        elif element == ')':
            counting_parentheses -= 1
            if counting_parentheses < 0:
                return "❌ Error: Incorrect parenthesis syntax"  # Unmatched closing parenthesis
            if len(stek) == 1:
                result = stek.pop()  # Get result from parentheses
                stek = stek_for_steks.pop()  # Restore previous stack
                stek.append(result)  # Add parentheses result to stack
            else:
                return "❌ Error: Incorrect entry in parentheses"
    
    if counting_parentheses != 0:  # Check if all parentheses are closed
        return "❌ Error: Some parentheses are not closed"
    if len(stek) == 1 and not is_op(stek): # Output - final result
        return f"🎉 Final Result: [{ln}] = {stek[0]}"
    elif len(stek) > 1:
        return "❌ Error: Not enough operators"
    else:
        exit(0)