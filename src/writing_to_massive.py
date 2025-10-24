from src.animate_text import animate_text
from src.is_op import is_op
from src.is_num import is_num
from src.convert_to_num import convert_to_num


def writing_to_massive(stek, element):  # Process one element and update stack
    if is_num(element):
        stek.append(convert_to_num(element))
        return stek
    elif is_op(element):
        if len(stek) < 2:
            return ["❌ Error: Not enough digits"]
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
        elif el2 == 0 and (element == '//' or element == "/"):
            return ["❌ Error: Division by zero!"]
        elif element == '//' and el2 != 0 and el2 == int(el2) and el1 == int(el1):
            stek.append(el1 // el2)
        elif element == '**':
            stek.append(el1 ** el2)
        elif element == '%' and el2 != 0 and el2 == int(el2) and el1 == int(el1):
            stek.append(el1 % el2)
        elif el2 != int(el2) or el1 != int(el1):
            return ["❌ Error: Invalid operands for integer division"]
        return stek
    else:
        return [f"❌ Error: I don`t know what to do with the '{element}'"]