from CardsGame import CardsGame

class SimpleCardsGame(CardsGame):
    def jogar_rodada(self):
        cartas_jogadas = {}
        for jogador in self.jogadores:
            print(f"\n{jogador}, suas cartas: {[str(c) for c in self.maos[jogador]]}")
            carta = input(f"Escolha uma carta para jogar: ").lower()
            while carta not in [str(c).lower() for c in self.maos[jogador]]:
                print("Você não tem essa carta. Escolha uma carta válida.\n")
                carta = input(f"Escolha uma carta para jogar: ").lower()
            carta_selecionada = next(c for c in self.maos[jogador] if str(c).lower() == carta)
            self.maos[jogador].remove(carta_selecionada)
            cartas_jogadas[jogador] = carta_selecionada
            print(f"{jogador} jogou {carta_selecionada}.")

        vencedor = max(cartas_jogadas, key=lambda j: self.valor_carta(cartas_jogadas[j]))
        print(f"\nO vencedor da rodada é {vencedor} com {cartas_jogadas[vencedor]}!")
