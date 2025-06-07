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
game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for Scissors: \n".lower()))
# Note: it's worth checking if the user has made a valid choice before the next line of code.
# If the user typed somthing other than 0, 1 or 2 the next line will give you an error.
# You could for example write:
if 0 <= user_choice < 3:
    print(game_images[user_choice])
    computer_choice = random.randint(0, 2)
    print(f"Computer chose: {game_images[computer_choice]}")

    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose!")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice > user_choice:
        print("You lose!")
    elif computer_choice == user_choice:
        print("It's a draw!")
else:
    print("You typed an invalid number. You lose!")
