import sys
from animate_text import animate_text
from is_op import is_op
from is_num import is_num
from convert_to_num import convert_to_num


def writing_to_massive(stek, element):  # Process one element and update stack
    if is_num(element):
        stek.append(convert_to_num(element))
        return stek
    elif is_op(element):
        if len(stek) < 2:
            error_msg = "❌ Error: Not enough digits for operation"
            animate_text(error_msg, 0.03, "typing")
            sys.exit(0)
        el2 = stek.pop()  # Right operand
        el1 = stek.pop()  # Left operand
        
        if element == '+':
            stek.append(el1 + el2)
        elif element == '-':
            stek.append(el1 - el2)
        elif element == '*':
            stek.append(el1 * el2)
        elif element == '/' and el2 != 0:
            stek.append(el1 / el2)
        elif element == '//' and el2 != 0 and el2 == int(el2) and el1 == int(el1):
            stek.append(el1 // el2)
        elif element == '**':
            stek.append(el1 ** el2)
        elif element == '%' and el2 != 0 and el2 == int(el2) and el1 == int(el1):
            stek.append(el1 % el2)
        elif el2 == 0:
            error_msg = "❌ Error: Division by zero!"
            animate_text(error_msg, 0.05, "typing")
            sys.exit(0)
        elif el2 != int(el2) or el1 != int(el1):
            error_msg = "❌ Error: Invalid operands for integer division"
            animate_text(error_msg, 0.05, "typing")
            sys.exit(0)
        return stek
    else:
        error_msg = f"❌ Error: I don`t know what to do with the '{element}'"
        animate_text(error_msg, 0.03, "typing")
        sys.exit(0)
