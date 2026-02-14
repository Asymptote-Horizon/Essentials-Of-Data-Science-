from datetime import datetime

def age_calc(birthdate):
    birth_year = int(birthdate.split('-')[-1])
    current_year = datetime.now().year
    return current_year- birth_year

def convert_salary_to_usd (salary_in_INR):
    conv_factor = 0.0125
    # return salary_in_INR / int(conv_factor)
    return salary_in_INR * conv_factor
birthdate = input("Input Your date of birth in DD-MM-YYYY: ")
salary_in_INR = float(input("Enter Salary in INR: "))
age = age_calc(birthdate)
salary_in_usd = convert_salary_to_usd(salary_in_INR)
print("Age is: " + str(age) )
print ("Salary in USD: " + f"{salary_in_usd:.2f}")