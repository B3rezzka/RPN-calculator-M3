from src.calc import calc


def test_positive_addition():
    assert calc("5 2 +") == "🎉 Final Result: [5 2 +] = 7"

def test_positive_subtraction():
    assert calc("10 3 -") == "🎉 Final Result: [10 3 -] = 7"

def test_positive_multiplication():
    assert calc("4 6 *") == "🎉 Final Result: [4 6 *] = 24"

def test_positive_division():
    assert calc("15 3 /") == "🎉 Final Result: [15 3 /] = 5.0" 

def test_positive_multiple_operations():
    assert calc("2 3 4 * +") == "🎉 Final Result: [2 3 4 * +] = 14"

def test_positive_division_by_float():
    # 9 / 2.0 -> 4.5
    assert calc("9 2.0 /") == "🎉 Final Result: [9 2.0 /] = 4.5"

def test_positive_zero_multiplication():
    assert calc("100 0 *") == "🎉 Final Result: [100 0 *] = 0"

def test_with_parentheses_1():
    assert calc("( 1 2 + ) 3 *") == "🎉 Final Result: [( 1 2 + ) 3 *] = 9"

def test_with_parentheses_2():
    assert calc("( 10 5 - ) 3 *") == "🎉 Final Result: [( 10 5 - ) 3 *] = 15"

def test_single_number():
    assert calc("5") == "🎉 Final Result: [5] = 5"