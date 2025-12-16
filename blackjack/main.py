import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def score(hand):
    final_score = sum(hand)

    if final_score == 21 and len(hand) == 2:
        return 0

    while final_score > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
        final_score = sum(hand)

    return final_score

def draw_card(hand):
    hand.append(random.choice(cards))

def draw_another_cards(hand):
    while True:
        choice_draw = input("Vuoi pescare un'altra carta? premi 'y' o 'n'\n").lower()
        if choice_draw == "y":
            draw_card(hand)
            print(f"Le tue carte sono: {hand} e il punteggio è {score(hand)}")
            return False
        elif choice_draw == "n":
            return True


def winner_rules(player_score, computer_score):
    if player_score == computer_score:
        print("Pareggio.🤝")
    elif computer_score == 0:
        print("Hai perso: il computer ha Blackjack.🥲")
    elif player_score == 0:
        print("Hai vinto: Blackjack!😁")
    elif player_score > 21:
        print("Hai perso: sballato.🥲")
    elif computer_score > 21:
        print("Hai vinto: il computer ha sballato.😁")
    elif player_score > computer_score:
        print("Hai vinto.😁")
    else:
        print("Hai perso.🥲")

def play_blackjack():
    player_cards = []
    computer_cards = []

    draw_card(player_cards)
    draw_card(player_cards)
    draw_card(computer_cards)
    draw_card(computer_cards)

    print(f"Le tue carte sono: {player_cards} e il punteggio è {score(player_cards)}")
    print(f"La carta del computer è: {computer_cards[0]}")

    game_over = False

    while not game_over:
        player_score = score(player_cards)
        computer_score = score(computer_cards)


        if player_score == 0 or computer_score == 0 or player_score > 21:
            game_over = True
        else:
            game_over = draw_another_cards(player_cards)

    player_score = score(player_cards)
    computer_score = score(computer_cards)

    if player_score <= 21 and player_score != 0:
        while computer_score != 0 and computer_score < 17:
            draw_card(computer_cards)
            computer_score = score(computer_cards)


    print(f"\nCarte finali player: {player_cards} -> {player_score if player_score != 0 else 21}")
    print(f"Carte finali computer: {computer_cards} -> {computer_score if computer_score != 0 else 21}")

    winner_rules(player_score, computer_score)

def start():
    restart = True
    while restart:
        print(art.logo)

        choice = input("Vuoi giocare a blackjack? premi 'y' o 'n'\n").lower()
        if choice != "y":
            restart = False
            continue

        play_blackjack()

        again = input("Vuoi fare un'altra partita? (y/n)\n").lower()
        if again == "y":
            restart = True
            print("\n" * 20)
            continue


start()
