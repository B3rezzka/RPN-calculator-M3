import sys
import time
from animate_text import animate_text
from writing_to_massive import writing_to_massive


def calc(expression):  # Calculate Reverse Polish Notation expression
    if expression == "" or expression == " ":
        error_msg = "❌ Error: Empty expression"
        animate_text(error_msg, 0.03, "typing")
        sys.exit(0)
    
    ln = expression  # Save original expression for output
    expression = expression.rstrip().split()
    stek = []  # Main stack for calculations
    stek_for_steks = []  # Stack for expressions in parentheses
    counting_parentheses = 0  # Parentheses counter
    
    # Animated welcome message
    animate_text("🔢 RPN Calculator Starting...", 0.05, "typing")
    time.sleep(0.5)
    for element in expression:
        if element != '(' and element != ')':
            stek = writing_to_massive(stek, element)
        elif element == '(':
            counting_parentheses += 1
            stek_for_steks.append(stek)  # Save current stack state
            stek = []  # Start new stack for parentheses content
        elif element == ')':
            counting_parentheses -= 1
            if counting_parentheses < 0:
                error_msg = "❌ Error: Incorrect parenthesis syntax"
                animate_text(error_msg, 0.03, "typing")
                sys.exit(0)  # Unmatched closing parenthesis
            if len(stek) == 1:
                result = stek.pop()  # Get result from parentheses
                stek = stek_for_steks.pop()  # Restore previous stack
                stek.append(result)  # Add parentheses result to stack
            else:
                error_msg = "❌ Error: Incorrect entry in parentheses"
                animate_text(error_msg, 0.03, "typing")
                sys.exit(0)
    
    if counting_parentheses != 0:  # Check if all parentheses are closed
        error_msg = "❌ Error: Some parentheses are not closed"
        animate_text(error_msg, 0.03, "typing")
        sys.exit(0)
    
    if len(stek) == 1: # Output - final result
        result_text = f"🎉 Final Result: [{ln}] = {stek[0]}"
        animate_text("Calculating...", 0.1, "random_chars")
        time.sleep(0.5)
        animate_text(result_text, 0.05, "typing")
        sys.exit(0)
    else:
        error_msg = "❌ Error: Not enough operators"
        animate_text(error_msg, 0.03, "typing")
        sys.exit(0)
