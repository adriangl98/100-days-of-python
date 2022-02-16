from ntpath import join
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# SETTING UP PASSWORD STRING
pwd = ''

#ADDING INPUTS OF LETTERS, SYMBOLS, NUMBERS TO STRING AT THE END
for letter in range(0,nr_letters):
    pwd += letters[random.randint(0,len(letters)-1)]
    print(pwd) 

for symbol in range(0,nr_symbols):
    pwd += symbols[random.randint(0,len(symbols)-1)]
    print(pwd)

for number in range(0,nr_numbers):
    pwd += numbers[random.randint(0,len(numbers)-1)]
    print(pwd)

pwd = list(pwd)
random.shuffle(pwd)
pwd = ''.join(pwd)

print("Your new password is: " + pwd)
# FROM LIST TO STRING (DIFFICULT)

# OWD =[]
# for letter in range(0,nr_letters):
#     pwd.append(letters[random.randint(0,len(letters)-1)])
#     print(pwd) 

# for symbol in range(0,nr_symbols):
#     pwd.append(symbols[random.randint(0,len(symbols)-1)])
#     print(pwd)

# for number in range(0,nr_numbers):
#     pwd.append(numbers[random.randint(0,len(numbers)-1)])
#     print(pwd)

# pwd = random.shuffle(pwd)

# print(pwd)