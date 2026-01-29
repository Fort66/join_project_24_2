from class_Game import Game
from class_Player import Player
from class_UI import UI

def main():
    game = Game()
    game.run()
    p = Player("Ivan", 25, 180, 75)
    print(p)

    ui = UI()

if __name__ == "__main__":
    main()
