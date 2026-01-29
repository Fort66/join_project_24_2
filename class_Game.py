class Game:
    def __init__(self):
        self.loop = True

    def run(self):
        while self.loop:
            print("Game is running")
            self.loop = False