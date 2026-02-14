@echo off

REM ===== Momentum =====
echo m = float(input("Enter mass in kg: "))> momentum.py
echo v = float(input("Enter velocity in m/s: "))>> momentum.py
echo momentum = m * v>> momentum.py
echo print("Momentum:", momentum)>> momentum.py

REM ===== Number Conditions =====
echo import math> number_conditions.py
echo.>> number_conditions.py
echo n = int(input("Enter a number: "))>> number_conditions.py
echo digits = len(str(abs(n)))>> number_conditions.py
echo.>> number_conditions.py
echo if digits == 1:>> number_conditions.py
echo     print(n * n)>> number_conditions.py
echo elif digits == 2:>> number_conditions.py
echo     print(math.sqrt(n))>> number_conditions.py
echo elif digits == 3:>> number_conditions.py
echo     print(n ** (1/3))>> number_conditions.py

REM ===== Employee Data =====
echo from datetime import date> employee_data.py
echo.>> employee_data.py
echo def calculate_age(year):>> employee_data.py
echo     return date.today().year - year>> employee_data.py
echo.>> employee_data.py
echo def salary_to_dollar(rupees):>> employee_data.py
echo     return rupees / 83>> employee_data.py
echo.>> employee_data.py
echo year = int(input("Enter birth year: "))>> employee_data.py
echo salary = float(input("Enter salary in rupees: "))>> employee_data.py
echo.>> employee_data.py
echo print("Age:", calculate_age(year))>> employee_data.py
echo print("Salary in dollars:", salary_to_dollar(salary))>> employee_data.py

REM ===== Reverse Number =====
echo n = input("Enter number: ")> reverse_number.py
echo print("Reverse:", n[::-1])>> reverse_number.py

REM ===== Student Result =====
echo marks = []> student_result.py
echo for i in range(5):>> student_result.py
echo     marks.append(int(input(f"Enter marks of subject {i+1}: ")))>> student_result.py
echo.>> student_result.py
echo if all(m >= 40 for m in marks):>> student_result.py
echo     total = sum(marks)>> student_result.py
echo     percent = total / 5>> student_result.py
echo.>> student_result.py
echo     if percent ^> 75:>> student_result.py
echo         grade = "Distinction">> student_result.py
echo     elif percent ^>= 60:>> student_result.py
echo         grade = "First Division">> student_result.py
echo     elif percent ^>= 50:>> student_result.py
echo         grade = "Second Division">> student_result.py
echo     elif percent ^>= 40:>> student_result.py
echo         grade = "Third Division">> student_result.py
echo.>> student_result.py
echo     print("Passed")>> student_result.py
echo     print("Percentage:", percent)>> student_result.py
echo     print("Grade:", grade)>> student_result.py
echo else:>> student_result.py
echo     print("Failed")>> student_result.py

REM ===== Fibonacci =====
echo def fib(n):> fibonacci_recursive.py
echo     if n <= 1:>> fibonacci_recursive.py
echo         return n>> fibonacci_recursive.py
echo     return fib(n-1) + fib(n-2)>> fibonacci_recursive.py
echo.>> fibonacci_recursive.py
echo n = int(input("Enter number of terms: "))>> fibonacci_recursive.py
echo for i in range(n):>> fibonacci_recursive.py
echo     print(fib(i), end=" ")>> fibonacci_recursive.py

REM ===== Patterns =====
echo for i in range(1, 6):> patterns.py
echo     print("*" * i)>> patterns.py
echo.>> patterns.py
echo print()>> patterns.py
echo.>> patterns.py
echo for i in range(5, 0, -1):>> patterns.py
echo     print("*" * i)>> patterns.py
echo.>> patterns.py
echo print()>> patterns.py
echo.>> patterns.py
echo for i in range(1, 6):>> patterns.py
echo     print(" " * (5 - i) + "* " * i)>> patterns.py

echo.
echo All Python files created successfully!
pause
