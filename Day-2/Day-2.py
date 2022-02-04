print("Welcome to the Tip Calculator.")
bill = float(input("What was the total bill? $"))
party_size = int(input("How many people to split the bill? "))
tip_size = int(input("What percentage would you like to give? 10, 12, or 15? "))

# Let's compute the bill

bill_tip = (bill + (bill*(tip_size/100))) / party_size #bill + tip total amount / party size
total = str(bill_tip) #Make bill_tip string to print 

print("Each person should pay: $" + total)