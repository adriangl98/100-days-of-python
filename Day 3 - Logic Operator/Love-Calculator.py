name1 = input("What is your name?\n").lower()
name2 = input("What is their name?\n").lower()

#Counting number of letters that appear in both names (lovers)
lovers = name1 + name2

t = lovers.count("t")
r = lovers.count("r")
u = lovers.count("u")
e = lovers.count("e")

true = t + r + u + e

l = lovers.count("l")
o = lovers.count("o")
v = lovers.count("v")
e = lovers.count("e")

love = l + o + v + e
#Adding count of letters
love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together")
else:
    print(f"Your score is {love_score}")
