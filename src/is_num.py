def is_num(token):  # Check if token can be converted to float
    try:
        float(token)
        return True
    except:
        return False