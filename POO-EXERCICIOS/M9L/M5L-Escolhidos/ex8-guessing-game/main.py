'''Escolha pelo menos 5 exercícios das listas M3L e M5L (5 de cada) para expandir o projeto do
exercício, incluindo novas classes relacionadas, conforme a sua criatividade, demonstrando
a injeção de dependência.'''

from modules import GameSession, Player

def main():
    while True:
        name = input("Digite o seu nome: ")
        player = Player(name)
        session = GameSession(player)
        session.play()

if __name__ == "__main__":
    main()