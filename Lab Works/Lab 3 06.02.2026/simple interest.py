# Program to calculate Simple Interest

P = float(input("Enter Principal amount: "))
R = float(input("Enter Rate of interest: "))
T = float(input("Enter Time: "))

SI = (P * R * T) / 100
total = P + SI

print("Simple Interest is:", SI)
print("Total Amount is:", total)
