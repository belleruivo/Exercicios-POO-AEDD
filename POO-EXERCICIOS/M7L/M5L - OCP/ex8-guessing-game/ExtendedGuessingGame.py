from GuessingGame import GuessingGame

class ExtendedGuessingGame(GuessingGame):
    def __init__(self):
        # Chama o construtor da classe base GuessingGame
        super().__init__()
        # Inicializa o contador de tentativas
        self.attempts = 0

    def guess(self, player_guess):
        # Incrementa o contador de tentativas a cada palpite
        self.attempts += 1
        
        # Chama o método guess da classe base e armazena o resultado
        result = super().guess(player_guess)
        
        # Verifica se o palpite foi correto
        if result == "Parabéns! Você adivinhou o número.":
            # Adiciona o número de tentativas ao resultado
            result += f" Você levou {self.attempts} tentativas."
        
        # Retorna o resultado
        return result
    
    # A classe ExtendedGuessingGame herda de GuessingGame e adiciona uma nova funcionalidade: um contador de tentativas. Ao implementar o método guess, ela não apenas reutiliza a lógica da classe base, mas também a estende para incluir informações sobre o número de tentativas.
    # ExtendedGuessingGame utiliza super().guess(player_guess) para chamar o método da classe base. Isso permite que você adicione a contagem de tentativas sem alterar a lógica de adivinhação já definida na classe GuessingGame.
    # Se, por exemplo, você quisesse adicionar uma nova funcionalidade que registrasse a data e hora em que o jogador começou a jogar ou a dificuldade do jogo (números maiores ou menores), você poderia criar novas subclasses que estendessem ExtendedGuessingGame sem precisar modificar o código existente.