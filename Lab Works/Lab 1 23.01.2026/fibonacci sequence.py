def fibonacci(n):
    # Base cases for recursion
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Take user input (replaces scanf functionality)
try:
    num = int(input("Enter the position in the Fibonacci sequence: "))
    
    if num < 0:
        print("Please enter a non-negative integer.")
    else:
        # Get and display the result
        print(f"The {num}th Fibonacci number is: {fibonacci(num)}")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
