class Banco:
    def __init__(self):
        self.contas = []

    def adicionar(self, conta):
        self.contas.append(conta)

    def remover(self, nome, pin):
        for conta in self.contas:
            if conta.getNome() == nome and conta.getPin() == pin:
                self.contas.remove(conta)
                return None
        return None

    def obter(self, nome, pin):
        for conta in self.contas:
            if conta.getNome() == nome and conta.getPin() == pin:
                return conta
        return None

    def calcularJuros(self):
        total_juros = 0
        for conta in self.contas:
            total_juros += conta.calcularJuros()
        return total_juros

    def __str__(self):
        return '\n'.join(str(conta) for conta in self.contas)