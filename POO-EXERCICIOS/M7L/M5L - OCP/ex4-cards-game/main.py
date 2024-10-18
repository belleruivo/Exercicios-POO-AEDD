from SimpleCardsGame import SimpleCardsGame

def main():
    jogadores = []
    for i in range(2):
        while True:
            nome_jogador = input(f"Nome do jogador {i + 1}: ").strip()
            if nome_jogador:
                jogadores.append(nome_jogador)
                break
            else:
                print("O nome do jogador não pode estar em branco. Por favor, insira um nome válido.")

    jogo = SimpleCardsGame(jogadores)
    jogo.distribuir_cartas()

    while True:
        jogo.jogar_rodada()
        if input("Deseja jogar outra rodada? (s/n) ").lower() != 's':
            break

if __name__ == "__main__":
    main()
