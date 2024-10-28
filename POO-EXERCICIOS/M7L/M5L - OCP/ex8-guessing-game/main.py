'''
Refazer as listas M3L e M5L, aplicando o Princípio Aberto-Fechado e mostrar as diferenças
de seu código, antes e depois.
'''

from ExtendedGuessingGame import ExtendedGuessingGame
from GuessingGame import GuessingGame 

def main():
    game = ExtendedGuessingGame.novo_jogo()  # instância do jogo
    while True:
        player_input = input("Digite seu palpite (entre 0 e 100): ") 
        player_guess = GuessingGame.validar_palpite(player_input)
        if player_guess is None:
            continue
        result = game.guess(player_guess)  # Verifica o palpite
        print(result) 
        if "Parabéns! Você adivinhou o número." in result:
            break  

if __name__ == "__main__":
    main()  
