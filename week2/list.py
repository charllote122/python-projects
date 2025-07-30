numbers=input("Enter integers separated by spaces: ").split()
int_list = [int(num) for num in numbers]
print("Sum of the integers:", sum(int_list))