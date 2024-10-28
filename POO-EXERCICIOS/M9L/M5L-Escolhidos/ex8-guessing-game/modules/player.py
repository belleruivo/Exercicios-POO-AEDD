class Player:
    def __init__(self, name):
        self.name = name
        self.guesses = 0

    def get_name(self):
        return self.name

    def increment_guesses(self):
        self.guesses += 1
