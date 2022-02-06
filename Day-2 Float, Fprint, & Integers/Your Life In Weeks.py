age_string = input("What is your age? ")

age = int(age_string)

age_remain = 90 - age

month_remain = age * 12

weeks_remain = age * 52

days_remain = age_remain * 365 

print(f"You have {days_remain} days, {weeks_remain} weeks, and {month_remain} months left")