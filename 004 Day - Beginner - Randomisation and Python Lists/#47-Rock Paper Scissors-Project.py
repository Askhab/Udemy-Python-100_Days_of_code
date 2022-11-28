from random import randint

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

# Write your code below this line 👇
whole = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(whole[player_choice])

computer_choice = randint(0, len(whole) - 1)
print(whole[computer_choice])

if player_choice == 0 and computer_choice == 1 or player_choice == 1 and computer_choice == 2 or player_choice == 2 and computer_choice == 0:
    print("You lose.")
elif player_choice == 0 and computer_choice == 2 or player_choice == 1 and computer_choice == 0 or player_choice == 2 and computer_choice == 1:
    print("You win.")
else:
    print("Round draw.")
