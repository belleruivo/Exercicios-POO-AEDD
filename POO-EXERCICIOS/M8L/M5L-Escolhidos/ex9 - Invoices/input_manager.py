class InputManager:
    @staticmethod
    def obter_entrada(mensagem, tipo=float):
        while True:
            try:
                if tipo == int:
                    return int(input(mensagem))
                else:
                    return float(input(mensagem))
            except ValueError:
                print("Entrada inválida. Por favor, insira um valor numérico.\n")
