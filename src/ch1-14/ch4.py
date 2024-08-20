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

choices = [rock,paper,scissors]

def play_game():
    computer_choice = randint(0,len(choices)-1)
    your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

    print(choices[computer_choice]+"\n")
    print("Computer chose: \n")
    print(choices[your_choice]+"\n")

    if computer_choice == your_choice:
        print("It's a tie!")
    elif ((computer_choice == 0 and your_choice == 2) or
          (computer_choice == 1 and your_choice == 0) or
          (computer_choice == 2 and your_choice == 1)):
        print("You lose!")
    else:
        print("You win!")

if __name__ == "__main__":
    play_game()