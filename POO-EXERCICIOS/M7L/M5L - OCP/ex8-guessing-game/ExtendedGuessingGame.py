from GuessingGame import GuessingGame

class ExtendedGuessingGame(GuessingGame): #herda de guessing game e adc a nova funcionalidade q é o contador sem alterar a logica de adivinhacao da classe guessing game 
    def __init__(self):
        # chama o construtor da classe base GuessingGame
        super().__init__()
        # inicializa o contador de tentativas
        self.attempts = 0

    def guess(self, player_guess): #ja reutiliza a logica da classe base e a estende
        # incrementa o contador de tentativas a cada palpite
        self.attempts += 1
        
        # chama o método guess da classe base e armazena o resultado
        result = super().guess(player_guess)
        
        if result == "Parabéns! Você adivinhou o número.":
            result += f" Você levou {self.attempts} tentativas."
        return result
    
    # pra modificacoes seria so criar novas subclasses que estendessem ExtendedGuessingGame.