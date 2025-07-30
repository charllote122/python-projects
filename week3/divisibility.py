def divisible_by_ten(num):
    if num % 10 == 0:
        return True
    else:
        return False


number = int(input("Enter a number: "))
print("Is the number divisible by 10:",divisible_by_ten(number))