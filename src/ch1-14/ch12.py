import random

def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    num = random.randint(1, 100)
    trial_count = 0
    game_is_over = False

    difficult = input("Choose a difficulty. Type 'easy' of 'hard' : ").lower()
    if "easy" == difficult:
        trial_count = 10
    elif "hard" == difficult:
        trial_count = 5
    else:
        print("Invalid difficulty. Let's start with the easy difficulty.")
        trial_count = 10
    
    while not game_is_over:
        print(f"You have {trial_count} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if num > guess:
            print("Too low")
            print("Guess again.")
        elif num < guess:
            print("Too high")
            print("Guess again.")
        else:
            print(f"Congratulations! You guessed the number {num} in {trial_count} attempts.")
            game_is_over = True
        trial_count -= 1
        if trial_count == 0:
            game_is_over = True
            print(f"Sorry, you didn't guess the number {num} in {trial_count} attempts.")


if __name__ == "__main__":
    start_game()