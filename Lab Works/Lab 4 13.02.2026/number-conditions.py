import math
number = int(input("Enter Your number:"))

#if number is two digits
if 0 <= number <=9:
    print("square of the number is: " + number ** 2)

elif(10 <= number <= 99):
    print(f"Square root of the number is: " + f"{math.sqrt(number):.2f}")

elif(100 <= number <= 999):
    print(f"Cube root of the number is: " + f"{math.cbrt(number):.2f}")


else:
    print("Other")