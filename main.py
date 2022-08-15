# need to create a user text-interface
# add other games like poker with multiplayer game
import time
import GameCore as GmCr


def start():
    GmCr.interface()
    try:
        choice = int(input("Your choice: "))
    except ValueError:
        print("Enter a number!!")
        input("Press ENTER to return...")
        print("Restarting game")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print("..")
        time.sleep(1)
        print("...")
        time.sleep(1)
        start()
    if choice == 1:
        deck = GmCr.create_deck()
        name = input("Enter Your Name: ")
        GmCr.start_game(name, deck)
    elif choice == 2:
        exit()


if __name__ == '__main__':
    start()