from CardsGame import CardsGame

class SimpleCardsGame(CardsGame):
    def jogar_rodada(self):
        # dicionário para armazenar as cartas jogadas por cada jogador
        cartas_jogadas = {}

        # loop para cada jogador na lista de jogadores
        for jogador in self.jogadores:
            # exibe as cartas do jogador
            print(f"\n{jogador}, suas cartas: {[str(c) for c in self.maos[jogador]]}")

            # solicita ao jogador que escolha uma carta para jogar
            carta = input(f"Escolha uma carta para jogar: ").lower()

            # enquanto a carta escolhida não estiver na mão do jogador, solicita novamente
            while carta not in [str(c).lower() for c in self.maos[jogador]]:
                print("Você não tem essa carta. Escolha uma carta válida.\n")
                carta = input(f"Escolha uma carta para jogar: ").lower()

            # encontra a carta selecionada na mão do jogador
            carta_selecionada = next(c for c in self.maos[jogador] if str(c).lower() == carta)

            # remove a carta selecionada da mão do jogador
            self.maos[jogador].remove(carta_selecionada)

            # armazena a carta jogada no dicionário cartas_jogadas
            cartas_jogadas[jogador] = carta_selecionada

            # exibe a carta jogada pelo jogador
            print(f"{jogador} jogou {carta_selecionada}.")

        # determina o vencedor da rodada com base no valor da carta jogada
        vencedor = max(cartas_jogadas, key=lambda j: self.valor_carta(cartas_jogadas[j]))

        # exibe o vencedor da rodada
        print(f"\nO vencedor da rodada é {vencedor} com {cartas_jogadas[vencedor]}!")