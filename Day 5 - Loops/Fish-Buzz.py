evens_sum = 0
for number in range (1,101):
    #Only follows one if statement, if first one is true, ommits the resto of the code
    if number % 5 == 0 and number % 3 == 0:
       print("FizzBuzz")
    elif number % 3 == 0:
       print("Fizz")
    elif number % 5 == 0:
       print("Buzz")
    else:
        print(number)
  