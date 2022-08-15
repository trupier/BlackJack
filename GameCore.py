import time

import Deck as d


def interface():
    print("Welcome to the BlackJack Python game!\nI hope you will have fun there!")
    print("1. Start Game\n2. Exit")


def draw(player, deck):
    player.hit(deck)
    player.add_points()


def create_deck():
    deck = d.Deck()
    return deck


def start_game(name, deck):
    """
    Function using to start game preparation.
    Give a player a name, Deal cards.
    :return:
    """
    deck.shufle()
    player_name = name
    krupier = d.Player('Croupier')
    p1 = d.Player(player_name)
    draw(p1, deck)
    draw(krupier, deck)
    draw(p1, deck)
    print(krupier.show_player())
    print(krupier.show_hand(), '2nd Card is hidden')
    draw(krupier, deck)
    print(p1.show_player())
    print(p1.show_hand())
    print("What's your next step?")
    next_step(p1, deck)
    if p1.show_points() == 21:
        print("You Win!")
        exit()
    else:
        croupier_turn(krupier, deck)
    if p1.show_points() > krupier.show_points() and p1.show_points() < 22:
        print("You Win!")
    else:
        print("Croupier Wins!")


def next_step(player, deck):
    didntpass = True
    while didntpass:
        if player.show_points() > 21:
            print("too much points. You lost")
            break
        try:
            step = input("type 'H' for hit or 'P' for pass")
            step = step.upper()
        except ValueError:
            print("incorrect Value!")
        else:
            if step == 'H':
                draw(player, deck)
                print(player.show_hand())
                print(player.show_points())
            elif step == 'P':
                didntpass = False


def croupier_turn(player, deck):
    print("Croupier shows his hand: ")
    print(player.show_hand())
    print(player.show_points())
    if player.show_points() < 17:
        while player.show_points() <= 17:
            print("Coupier hit the card")
            draw(player, deck)
            print(player.show_hand(), player.show_points())
            time.sleep(1)
    if player.show_points() >= 17:
        print(f"Coupier's hand is worth {player.show_points()} ")
