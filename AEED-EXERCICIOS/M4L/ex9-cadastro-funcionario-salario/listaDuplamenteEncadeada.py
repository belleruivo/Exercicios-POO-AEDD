class ListaDuplamenteEncadeada:
    def __init__(self):
        self.cabeca = None

    def inserir_ordenado(self, funcionario):
        if self.cabeca is None:
            self.cabeca = funcionario
        else:
            atual = self.cabeca
            while atual is not None and atual.salario < funcionario.salario:
                anterior = atual
                atual = atual.proximo

            if atual == self.cabeca:  # Inserção no início
                funcionario.proximo = self.cabeca
                self.cabeca.anterior = funcionario
                self.cabeca = funcionario
            else:
                funcionario.proximo = atual
                funcionario.anterior = anterior
                anterior.proximo = funcionario
                if atual is not None:
                    atual.anterior = funcionario

    def calcular_imposto(self):
        funcionarios = []
        atual = self.cabeca
        while atual is not None:
            if atual.salario <= 850:
                imposto = 0
            elif 850 < atual.salario <= 1200:
                imposto = 0.1 * atual.salario
            else:
                imposto = 0.2 * atual.salario
            
            valor_a_receber = atual.salario - imposto
            funcionarios.append((atual.nome, imposto, valor_a_receber))
            atual = atual.proximo
        return funcionarios

    def listar_por_letra(self, letra):
        atuais = []
        atual = self.cabeca
        while atual is not None:
            if atual.nome.lower().startswith(letra.lower()):
                atuais.append((atual.nome, atual.salario))
            atual = atual.proximo
        return atuais

    def listar_funcionarios(self, ordem='crescente'):
        funcionarios = []
        atual = self.cabeca
        while atual is not None:
            funcionarios.append((atual.nome, atual.salario))
            atual = atual.proximo

        if ordem == 'decrescente':
            funcionarios.reverse()
        return funcionarios