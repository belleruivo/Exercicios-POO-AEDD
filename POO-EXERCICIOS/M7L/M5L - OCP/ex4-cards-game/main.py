from SimpleCardsGame import SimpleCardsGame

def main():
    jogadores = []  # inicializa uma lista vazia para armazenar os nomes dos jogadores

    # loop para coletar os nomes de dois jogadores
    for i in range(2):
        while True:
            # solicita o nome do jogador i+1
            nome_jogador = input(f"Nome do jogador {i + 1}: ").strip()
            if nome_jogador:
                # se o nome não estiver vazio, adiciona à lista de jogadores e sai do loop interno
                jogadores.append(nome_jogador)
                break
            else:
                # se o nome estiver vazio, solicita novamente
                print("O nome do jogador não pode estar em branco. Por favor, insira um nome válido.")

    # cria uma instância de SimpleCardsGame com a lista de jogadores
    jogo = SimpleCardsGame(jogadores)
    # distribui as cartas para os jogadores
    jogo.distribuir_cartas()

    # loop para jogar rodadas do jogo
    while True:
        # joga uma rodada do jogo
        jogo.jogar_rodada()
        # pergunta ao usuário se deseja jogar outra rodada
        if input("Deseja jogar outra rodada? (s/n) ").lower() != 's':
            break  # sai do loop se a resposta não for 's'

if __name__ == "__main__":
    # chama a função main se o script for executado diretamente
    main()