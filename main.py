from class_Game import Game
from class_Player import Player
from class_Sound import Sound

def main():
    game = Game()
    game.run()
    p = Player("Ivan", 25, 180, 75)
    print(p)

    sound = Sound()

if __name__ == "__main__":
    main()
