class MessageHandler:
    def obter_nome_jogador(self):
        """Solicita o nome do jogador."""
        return input("Digite o nome do jogador: ")

    def obter_dificuldade(self):
        """Solicita o nível de dificuldade até que uma entrada válida seja recebida."""
        while True:
            dificuldade = input("Escolha o nível de dificuldade (fácil, médio, difícil): ").lower()
            if dificuldade in ['fácil', 'médio', 'difícil']:
                return dificuldade
            else:
                print("Nível de dificuldade inválido. Tente novamente.")

    def mostrar_resultado(self, resultado):
        """Exibe o resultado do palpite."""
        print(resultado)

    def mostrar_pontuacao(self, pontuacao):
        """Exibe a pontuação do jogador."""
        print(pontuacao)
