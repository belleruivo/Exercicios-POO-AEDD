from player import Player
from game_session import GameSession

def main():
    name = input("Digite o seu nome: ")
    player = Player(name)
    session = GameSession(player)
    session.play()

if __name__ == "__main__":
    main()
