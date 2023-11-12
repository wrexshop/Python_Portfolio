# Day 5 Coding Challenge

import random

# 0 = ROCK
# 1 = PAPER
# 2 = SCISSORS

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

art = [rock, paper, scissors]
options = ["Rock", "Paper", "Scissors"]
isValid = False

while isValid == False:
    player_roll = int(input("What do you choose? 0 for Rock, 1 for Paper, 2 for Scissors. "))
    if player_roll >= 0 and player_roll <=2:
        isValid = True
    else:
        print("Error: Invalid Selection")

computer_roll = random.randint(0,2)

print(f"You selected {options[player_roll]}")
print(f"{art[player_roll]}\n")
print(f"Computer selected {options[computer_roll]}")
print(f"{art[computer_roll]}\n")

if player_roll == computer_roll:
    print("Draw!")
# ROCK
elif player_roll == 0:
    if computer_roll == 1:
        print("You Lose!")
    elif computer_roll == 2:
        print("You Win!")
# PAPER
elif player_roll == 1:
    if computer_roll == 0:
        print("You WIN!")
    elif computer_roll == 2:
        print("You Lose!")
# SCISSORS
elif player_roll == 2:
    if computer_roll == 0:
        print("You Lose!")
    elif computer_roll == 1:
        print("You Win!")
