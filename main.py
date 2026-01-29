from class_Game import Game
from class_Player import Player

def main():
    game = Game()
    game.run()
    p = Player("Ivan", 25, 180, 75)
    print(p)


if __name__ == "__main__":
    main()
