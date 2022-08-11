import Deck as d

def draw(player, deck):
    player.hit(deck)
    player.add_points()


def start_game():
    deck = d.Deck()
    deck.shufle()
    player_name = input("enter your name: ")
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
    return