class Player:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def __str__(self):
        return f"Player: {self.name}, Age: {self.age}, Height: {self.height}, Weight: {self.weight}"

