from jogo_adivinhacao import JogoAdivinhacao

def main():
    jogador_nome = input("Digite o nome do jogador: ")
    jogo = JogoAdivinhacao(jogador_nome)  # Inicializa o jogo com o nome do jogador

    while True:
        player_input = input("Digite seu palpite (entre 1 e 100) ou 'h' para ver o histórico: ")

        if player_input.lower() == 'h':
            print(jogo.exibir_historico())  # Mostra o histórico de palpites do jogador
            continue

        try:
            palpite = int(player_input)
            resultado = jogo.jogar(palpite)  # Verifica o palpite
            print(resultado)
            if "Parabéns" in resultado:
                break  # Termina o jogo se o jogador adivinhar corretamente
        except ValueError:
            print("Por favor, insira um número válido.")

if __name__ == "__main__":
    main()
