from __future__ import print_function


print("Welcome to Treasure Island. \nYour Mission is to find the treasure.")
road_decision = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\"\n")

if road_decision == "left": 
    swim_decision = input("You come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across\n")
    if swim_decision == "wait":
        doors_decision = input("You arrive at the island unharmed. There is a hosue wiht 3 doors. One red, one yellow, and one blue. Which color do you choose?\n")
        if doors_decision == "yellow":
            print("You find a treasure filled with bounty. YOU WIN")
        elif doors_decision == "red":
            print("A ninja jumps out out of the door and stabs youn in the heart. YOU DIED")
        else:
            print("A whale pops out of the door and crushes your whole body. YOU DIED")
    else:
        print("You tried to swim across but got exhausted and drawned. YOU DIED")
else:
    print("You walk the road and step on a poisonous flower and die of a heart attack")
