evens_sum = 0
for number in range (1,101):
    if number % 2 == 0:
        evens_sum += number
    
print(f"The sum of even numbers between 1-100 is: {evens_sum}")