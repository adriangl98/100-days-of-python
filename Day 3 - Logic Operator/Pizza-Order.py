print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, L: ")
bill = int(0)

#Set price depending on size
if size == "S":
    bill = 15
if size == "M":
    bill = 20
if size == "L":
    bill = 25   


add_pepperoni = input("Do you want pepperoni? Y/N: ")

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
 
extra_cheese = input("Do you want extra cheese? Y/N: ")

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}")

