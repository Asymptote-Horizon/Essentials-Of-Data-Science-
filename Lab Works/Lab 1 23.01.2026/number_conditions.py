import math

n = int(input("Enter a number: "))
digits = len(str(abs(n)))

if digits == 1:
    print(n * n)
elif digits == 2:
    print(math.sqrt(n))
elif digits == 3:
    print(n ** (1/3))
