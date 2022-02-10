# Choose who pays the bill
import random

dinner_party = input("Who is currently here? Use comma to separate the names. \n")

names_party = dinner_party.split(",")

# USING RANDINT
# number_party = len(names_party)
# payer_party = names_party[random.randint(0, number_party-1)]

#Randomly pick an item from a list
payer_party = random.choice(names_party)

print(f"{payer_party} is the one paying tongiht!")
