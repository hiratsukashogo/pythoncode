import random

class Card:
    
    numbers = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    mark = ['♥', '♠', '♣', '♦']
    
    @staticmethod
    def card_value(card):
        num = card[1:]
        if num in ['J', 'Q', 'K']:
            return 10
        elif num == 'A':
            return 11
        else:
            return int(num)

def adjust_for_ace(points, hand):
    aces = sum(1 for card in hand if card[1:] == 'A')
    while points + 10 <= 21 and aces > 0:
        points -= 10
        aces -= 1
    return points    

def draw_card(deck):
    rand_card = random.randint(0, len(deck) - 1)
    return deck.pop(rand_card)

def print_hand_and_points(name, hand):
    hand_str = ' '.join(hand)
    points = sum(Card.card_value(card) for card in hand)
    points = adjust_for_ace(points, hand)
    print(f"{name}の手札: {hand_str}")
    print(f"{name}の点数: {points}")
    return points

deck = [mk + num for mk in Card.mark for num in Card.numbers]
random.shuffle(deck)

player_hand = [draw_card(deck) for _ in range(2)]
print_hand_and_points("プレイヤー", player_hand)

while True:
    choice = input("カードを引きますか？ (y/n): ")
    if choice == 'y':
        player_hand.append(draw_card(deck))
        print_hand_and_points("プレイヤー", player_hand)
        if sum(Card.card_value(card) for card in player_hand) > 21:
            print("プレイヤーの点数が21を超えた。")
            break
    elif choice == 'n':
        print("プレイヤーは引かなかった")
        break
    else:
        print("無効な入力です。'y' または 'n' を入力してください。")


dealer_hand = [draw_card(deck) for _ in range(2)]
print_hand_and_points("ディーラー", dealer_hand)

while True:
    if sum(Card.card_value(card) for card in dealer_hand) < 16:
        print("ディーラーはカードを引いた")
        dealer_hand.append(draw_card(deck))
        print_hand_and_points("ディーラー", dealer_hand)
        if sum(Card.card_value(card) for card in dealer_hand) > 21:
            print("ディーラーの点数が21を超えた。")
            break
    else:
        print("ディーラーは引かなかった")
        break

if  sum(Card.card_value(card) for card in player_hand) <= 21 and sum(Card.card_value(card) for card in dealer_hand) <= 21:
    print("Judge!!")
    if sum(Card.card_value(card) for card in player_hand) < sum(Card.card_value(card) for card in dealer_hand):
        print("ディーラーWin!!!")
    elif sum(Card.card_value(card) for card in player_hand) > sum(Card.card_value(card) for card in dealer_hand):
        print("プレイヤーWin!!!")
    else:
        print("draw!!!")
elif sum(Card.card_value(card) for card in player_hand) <= 21 and sum(Card.card_value(card) for card in dealer_hand) > 21:
    print("プレイヤーWin!!!")
elif sum(Card.card_value(card) for card in player_hand) > 21 and sum(Card.card_value(card) for card in dealer_hand) <= 21:
    print("ディーラーWin!!!")
else:
    print("draw")