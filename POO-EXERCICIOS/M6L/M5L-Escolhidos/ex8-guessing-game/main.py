'''Escolha pelo menos 5 exercícios das listas M3L e M5L (5 de cada) para expandir o projeto do
exercício, incluindo novas classes relacionadas, conforme a sua criatividade, aplicando a
associação de classes.

Uma boa maneira de criar esse exercício é seguindo o seguinte roteiro: descreva em no
máximo 200 palavras o que é um objeto específico e o que ele faz. Liste os substantivos e
verbos separadamente. Cada substantivo corresponde a um objeto que precisará ser
construído para implementar um sistema. Selecione 5 dos objetos que você listou e, para
cada um, liste vários atributos e comportamentos. Perceba também as associações e
implemente-as. Descreva brevemente como esses objetos interagem entre si e com outros
objetos na sua descrição. Estes passos que você seguiu são típicos do projeto orientado a
objetos.'''

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
