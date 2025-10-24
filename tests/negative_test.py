from src.calc import calc


def test_incorrect_parenthesis_syntax1():
    assert calc(") ( 5 3 +") == "❌ Error: Incorrect parenthesis syntax"

def test_incorrect_parenthesis_syntax2():
    assert calc(") 5 3 + ( ) )") == "❌ Error: Incorrect parenthesis syntax"

def test_parentheses_not_closed1():
    assert calc("( 4 5 +") == "❌ Error: Some parentheses are not closed"

def test_parentheses_not_closed2():
    assert calc("( ( 4 5 + )") == "❌ Error: Some parentheses are not closed"

def test_incorrect_entry_parentheses1():
    assert calc("( )") == "❌ Error: Incorrect entry in parentheses"

def test_incorrect_entry_parentheses2():
    assert calc("( 5 5 )") == "❌ Error: Incorrect entry in parentheses"

def test_parantheses_are_not_closed1():
    assert calc("( 2 ( 5 4  + ) - ") == "❌ Error: Some parentheses are not closed"

def test_parantheses_are_not_closed1():
    assert calc("( 2 ( 5 4  + ) - ") == "❌ Error: Some parentheses are not closed"

def test_not_enough_operators1():
    assert calc("42 52 + 9") == "❌ Error: Not enough operators"

def test_not_enough_operators2():
    assert calc("1337 98 - 5 + 3") == "❌ Error: Not enough operators"

def test_empty_expression1():
    assert calc(" ") == "❌ Empty expression"

def test_empty_expression2():
    assert calc("") == "❌ Empty expression"

def test_empty_expression3():
    assert calc("       ") == "❌ Empty expression"

def test_division_by_zero1():
    assert calc("100 0 /") == "❌ Error: Division by zero!"

def test_division_by_zero2():
    assert calc("100 0 //") == "❌ Error: Division by zero!"

def test_invalid_operands_int1():
    assert calc("4.1 2 //") == "❌ Error: Invalid operands for integer division"

def test_invalid_operands_int2():
    assert calc("52.6 7 //") == "❌ Error: Invalid operands for integer division"

def test_unknown_element1():
    assert calc("r") == "❌ Error: I don`t know what to do with the 'r'"

def test_unknown_element2():
    assert calc("&&") == "❌ Error: I don`t know what to do with the '&&'"