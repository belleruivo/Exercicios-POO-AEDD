from GuessingGame import GuessingGame

class ExtendedGuessingGame(GuessingGame): 
    def __init__(self): 
        super().__init__() # permite chamar o init da classe pai
        self.attempts = 0

    def guess(self, player_guess): # já reutiliza a logica da classe base e a estende
        self.attempts += 1
        
        result = super().guess(player_guess)
        
        if result == "Parabéns! Você adivinhou o número.":
            result += f" Você levou {self.attempts} tentativas."
        return result