from ch7_logo import logo,stages
from ch7_word import word_list
import random 
print(logo)
print("===============================================")
print(stages[6])

# 단어준비
word = random.choice(word_list)
word_to_list = list(word)
word_blank = []
life = 6

for _ in range(len(word_to_list)):
   word_blank.append('_')

def start_game():
    print("The word is : "+word)
    print("===============================================")
    print("Guess the word: ", ''.join(word_blank))
    print("===============================================")
    while True:
        guess = input("Enter your guess: ").lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in word_to_list:
                for i in range(len(word_to_list)):
                    if word_to_list[i] == guess:
                        word_blank[i] = guess
            else:
                print(f"{guess} is not in the word.")
                # 목숨 한개 차감하고 다시 그리기
                you_loss_life()
            print("===============================================")
            print("Guess the word: ", ''.join(word_blank))
            if '_' not in word_blank:
                print("Congratulations! You've guessed the word.")
                break
        else:
            print("Please enter a single alphabet.")


def you_loss_life():
    global life
    life -= 1
    print(stages[life])
    if life <= 0:
        print("The word is : "+word)
        print("Game Over!ㅜㅜ")
        exit()

start_game()