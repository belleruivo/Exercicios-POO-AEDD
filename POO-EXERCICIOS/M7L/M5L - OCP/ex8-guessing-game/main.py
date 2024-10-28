'''
Refazer as listas M3L e M5L, aplicando o Princípio Aberto-Fechado e mostrar as diferenças
de seu código, antes e depois.
'''

from ExtendedGuessingGame import ExtendedGuessingGame
from GuessingGame import GuessingGame 

def main():
    while True:
        game = ExtendedGuessingGame.novo_jogo()  # instância do jogo
        while True:
            player_input = input("Digite seu palpite (entre 0 e 100): ") 
            player_guess = GuessingGame.validar_palpite(player_input)
            if player_guess is None:
                continue 
            result = game.guess(player_guess)  
            print(result) 
            if "Parabéns! Você adivinhou o número." in result:
                break  
        play_again = input("Você quer jogar novamente? (s/n): ").lower()
        if play_again != 's':
            print("Obrigado por jogar!")
            break 
        
if __name__ == "__main__":
    main()