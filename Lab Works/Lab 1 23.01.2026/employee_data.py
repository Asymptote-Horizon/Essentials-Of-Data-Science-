from datetime import date

def calculate_age(year):
    return date.today().year - year

def salary_to_dollar(rupees):
    return rupees / 83

year = int(input("Enter birth year: "))
salary = float(input("Enter salary in rupees: "))

print("Age:", calculate_age(year))
print("Salary in dollars:", salary_to_dollar(salary))
