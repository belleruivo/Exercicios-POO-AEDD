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


# explicacao:
# Identificação das Classes
# Dificuldade: Define o nível de dificuldade e o intervalo de números com base nesse nível.
# GuessingGame: Controla a lógica do jogo, incluindo a verificação dos palpites do jogador.
# History: Armazena o histórico dos palpites do jogador.
# MessageHandler: Gerencia as interações com o usuário, como obter o nome do jogador e a dificuldade.
# Player: Representa o jogador e coleta os palpites.
# ScoreTracker: Mantém e exibe a pontuação do jogador.
# Análise da Injeção de Dependência
# A injeção de dependência é uma técnica que ajuda a reduzir o acoplamento entre classes, facilitando testes e manutenção. No seu código, a injeção de dependência está sendo aplicada nas seguintes classes:

# GuessingGame: Recebe player, score_tracker e dificuldade no construtor. Isso é apropriado, pois permite que o jogo utilize instâncias de Player e ScoreTracker sem criar suas próprias instâncias internamente.

# Player: Recebe dificuldade para solicitar palpites de acordo com o nível de dificuldade. Isso também é uma boa prática, pois mantém a lógica de dificuldade separada.

# As classes Dificuldade, History, MessageHandler e ScoreTracker não utilizam injeção de dependência em seus construtores, o que é aceitável, pois elas não dependem de outras classes para funcionar corretamente.