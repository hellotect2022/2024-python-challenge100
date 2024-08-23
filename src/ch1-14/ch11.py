import random
from logos.logo import logo_blackjack
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.

class GameState:
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    my_cards = []
    dealer_cards = []
    you_check = False
    dealer_check = False
    game_is_over = False

def init_game():
    if "Y" == input("Do you want to play a game of Blackjack? (y/n): ").upper():
        start_game()
def deal_cards():
    return random.choice(GameState.cards)

def start_game():
    print(logo_blackjack)
    # 처음 카드를 2장 뽑는다. 
    for _ in range(2):
        GameState.my_cards.append(deal_cards())
        GameState.dealer_cards.append(deal_cards())
    print(f"Your cards: {GameState.my_cards}, current score: {sum(GameState.my_cards)}")
    print(f"Computer's first card: {GameState.dealer_cards[0]}")
    new_session()


def new_session():
    while not GameState.game_is_over:
        if not GameState.you_check:
            # 내가 카드를 뽑을 지 말지 선택하는 로직 추가 
            try_game = input("Type 'y' to get another card, type 'n' to pass: ").upper()
            if try_game == 'Y': 
                GameState.my_cards.append(deal_cards())
                if sum(GameState.my_cards) >= 21 : 
                    GameState.you_check = True
                print(f"Your cards: {GameState.my_cards}, current score: {sum(GameState.my_cards)}")
            elif try_game == 'N': 
                GameState.you_check = True
            else :
                print("Invalid input. Please enter 'y' or 'n'.")
                new_session()
        
        if not GameState.dealer_check:
            dealer_time()

        if GameState.you_check and GameState.dealer_check:    
            GameState.game_is_over = True
    check_winner()

def dealer_time():
    if sum(GameState.dealer_cards) >= 17:
        GameState.dealer_check = True
        print("Dealer checks!!!")
    else :
        GameState.dealer_cards.append(deal_cards())

def check_winner():
    print(f"Your cards: {GameState.my_cards}, current score: {sum(GameState.my_cards)}")
    print(f"Computer cards: {GameState.dealer_cards}, current score: {sum(GameState.dealer_cards)}")
    if sum(GameState.my_cards) > 21:
            print("Busted! You lose!")
    elif sum(GameState.my_cards) == 21:
        print("Congratulations! You win!")
    elif sum(GameState.dealer_cards) > 21:
        print("Computer busted! You win!")
    elif sum(GameState.dealer_cards) > sum(GameState.my_cards):
        print("Computer wins!")
    elif sum(GameState.dealer_cards) < sum(GameState.my_cards):
        print("You win!")
    else:
        print("It's a tie!")


if __name__ == "__main__":
    init_game()


