from game import GuessingGame
from player import Player
from score_tracker import ScoreTracker
from difficulty import Dificuldade
from message_handler import MessageHandler

def main():
    message_handler = MessageHandler()
    nome_jogador = message_handler.obter_nome_jogador()
    
    score_tracker = ScoreTracker()  # Mantém a pontuação entre os jogos

    while True:
        nivel_dificuldade = message_handler.obter_dificuldade()
        dificuldade = Dificuldade(nivel_dificuldade)
        
        # A injeção de dependências ocorre aqui
        player = Player(nome_jogador, dificuldade)
        game = GuessingGame(player, score_tracker, dificuldade)

        while True:
            player_input = player.dar_palpite()
            player_guess = game.validar_palpite(player_input)
            if player_guess is None:
                continue

            result = game.guess(player_guess)
            message_handler.mostrar_resultado(result)

            if result == "Parabéns! Você adivinhou o número.":
                message_handler.mostrar_pontuacao(score_tracker.exibir_pontuacao())
                break  # Sai do loop do jogo

        # Pergunta se o jogador quer jogar novamente
        jogar_novamente = input("Você deseja jogar novamente? (s/n): ").lower()
        if jogar_novamente != 's':
            print("Obrigado por jogar! Sua pontuação final foi:", score_tracker.exibir_pontuacao())
            break  # Sai do loop principal



if __name__ == "__main__":
    main()
