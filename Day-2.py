print("Welcome to the Tip Calculator.")
bill = input("What was the total bill? $")
party_size = input("How many people to split the bill? ")
tip_size = input("What percentage would you like to give? 10, 12, or 15? ")

# Let's compute the bill

bill_tip = bill + (bill*(tip_size/100)) #bill + tip total amount