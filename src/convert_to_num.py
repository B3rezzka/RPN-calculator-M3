def convert_to_num(token):  # Convert string to int or float
    if '.' in token:
        return float(token)
    else:
        return int(token)