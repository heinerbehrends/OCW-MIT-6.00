def simpleExp(number, exponent):
    if exponent == 0:
        return 1
    else:
        return number * (simpleExp(number, exponent - 1))

print simpleExp(2,3)
