import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_image = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors.\n"))


computer_choice = random.randint(0,2)

# User Wins Scenarios
if user_choice == 0 and computer_choice == 2 or user_choice == 1 and computer_choice == 0 or user_choice == 2 and computer_choice == 1:
    print("Your choice:\n") ; print(game_image[user_choice]) ; print("computer's choice:\n") ; print(game_image[computer_choice]) ; print("You win!")
# Same Choice Scenario
elif user_choice == computer_choice:
    print("Your choice:\n") ; print(game_image[user_choice]) ; print("computer's choice:\n") ; print(game_image[computer_choice]) ; print("Tie!")
# User Loses
else:
    print("Your choice:\n") ; print(game_image[user_choice]) ; print("computer's choice:\n") ; print(game_image[computer_choice]) ; print("You Lose!")



# 0 beats 2
# 1 beats 0
# 2 beats 1 

