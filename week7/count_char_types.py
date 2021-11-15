def count_char_type(str):
    alpha = 0
    digit = 0
    symbol = 0
    for c in str:
        if c.isalpha():
            alpha += 1
        elif c.isdigit():
            digit += 1
        elif c.isascii():
            symbol += 1

    return alpha, digit, symbol



print(count_char_type("W@#yn26at^&i9ve%^&&^^"))
