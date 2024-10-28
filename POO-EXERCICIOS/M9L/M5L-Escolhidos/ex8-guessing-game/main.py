'''Escolha pelo menos 5 exercícios das listas M3L e M5L (5 de cada) para expandir o projeto do
exercício, incluindo novas classes relacionadas, conforme a sua criatividade, demonstrando
a injeção de dependência.'''

from modules import GameSession, Player

def main():
    name = input("Digite o seu nome: ")
    player = Player(name)
    session = GameSession(player)
    session.play()

if __name__ == "__main__":
    main()


# Análise da Associação Bilateral
# A associação bilateral é observada principalmente entre as classes GameSession e Player, e indiretamente entre Player e GuessingGame. Vamos detalhar:

# GameSession:

# A classe GameSession tem um atributo player, que é uma instância da classe Player. Isso estabelece uma associação onde cada sessão de jogo está vinculada a um jogador específico.
# self.game = GuessingGame(): Uma nova instância de GuessingGame é criada para cada sessão, permitindo que cada jogador tenha seu próprio jogo.
# Player:

# A classe Player contém métodos que retornam informações sobre o jogador, como get_name() e increment_guesses(). Embora o Player não tenha uma referência direta a GameSession ou GuessingGame, ele interage com eles através da sessão do jogo, uma vez que o GameSession faz uso dos métodos do Player.
# GuessingGame:

# A classe GuessingGame contém a lógica do jogo. A GameSession invoca métodos dessa classe, como guess() e validar_palpite(), para interagir com o jogo em si. Isso não constitui uma associação bilateral, mas sim uma relação de uso ou dependência.
# Considerações sobre a Associação Bilateral
# Aqui está o resumo das associações:

# Entre GameSession e Player: Cada instância de GameSession tem um Player, permitindo que a sessão saiba quem está jogando.
# Entre Player e GuessingGame: Embora não haja uma referência direta, o Player está indiretamente associado ao GuessingGame por meio da lógica de jogo implementada em GameSession.