def large_power(base, exponent):
    result = base ** exponent
    if result > 5000:
        return True
    else:
        return False
 
base=int(input("Enter the base: "))
exponent=int(input("Enter the exponent: "))

print("Is the result of large_power greater than 5000:", large_power(base, exponent))