import random

class Card:

    mark = ['♥', '♠', '♣', '♦']
    numbers = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    @staticmethod
    def card_value(card):
        num = card[1:]
        if num in 'J':
            return 11
        elif num in 'Q':
            return 12
        elif num  in 'K':
            return 13
        elif num in 'A':
            return 1
        else:
            return int(num)

def draw_card(deck):
    rand_card = random.randint(0, len(deck) - 1)
    return deck.pop(rand_card)



deck = [mk + num for mk in Card.mark for num in Card.numbers]
random.shuffle(deck)

player_hand = [draw_card(deck) for _ in range(2)]
print(player_hand)

dealer_hand = [draw_card(deck) for _ in range(2)]
print(dealer_hand)

sharing_hand = [draw_card(deck) for _ in range(3)]
print(sharing_hand)

while True:
    choice = input("フォールド｜コール｜レイズ (f/c/r): ")
    if choice == 'f':
        print("ディーラーWin!!")
        break
    elif choice == 'c':
        sharing_hand.append(draw_card(deck))
        print(sharing_hand)
    elif choice == 'r':
        sharing_hand.append(draw_card(deck))
        print(sharing_hand)
    else:
        print("無効な入力です。'f' または 'c'または'r' を入力してください。")
        
    if len(sharing_hand) >= 5:
        break

player_hand.extend(sharing_hand)
dealer_hand.extend(sharing_hand)

checkhand_player = sorted(player_hand,key=lambda card: card[1])
print(checkhand_player)
checkhand_dealer = sorted(dealer_hand,key=lambda card: card[1])
print(checkhand_dealer)