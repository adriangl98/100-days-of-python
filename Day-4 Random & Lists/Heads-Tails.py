import random

choice = input("Choose Heads or Tails?")
winner = random.randrange(1,3)


if winner == 1:
    winner = "Heads"
else:
    winner = "Tails"

if choice == winner:
    print(f"{winner}! You Win")
else:
    print(f"{winner}! You lose.")