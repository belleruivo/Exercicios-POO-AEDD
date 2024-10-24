class Person:
    def __init__(self, nome="", endereco="", cpf="", rg="", telefone=""):
        self.__nome = nome
        self.__endereco = endereco
        self.__cpf = cpf
        self.__rg = rg
        self.__telefone = telefone

    def get_nome(self):
        return self.__nome

    def get_endereco(self):
        return self.__endereco

    def get_cpf(self):
        return self.__cpf

    def get_rg(self):
        return self.__rg

    def get_telefone(self):
        return self.__telefone

    def set_nome(self, nome):
        if isinstance(nome, str) and nome:
            self.__nome = nome
        else:
            raise ValueError("Nome inválido")

    def set_endereco(self, endereco):
        if isinstance(endereco, str) and endereco:
            self.__endereco = endereco
        else:
            raise ValueError("Endereço inválido")

    def set_cpf(self, cpf):
        if isinstance(cpf, str) and len(cpf) == 11 and cpf.isdigit():
            self.__cpf = cpf
        else:
            raise ValueError("CPF inválido")

    def set_rg(self, rg):
        if isinstance(rg, str) and rg:
            self.__rg = rg
        else:
            raise ValueError("RG inválido")

    def set_telefone(self, telefone):
        if isinstance(telefone, str) and telefone.isdigit():
            self.__telefone = telefone
        else:
            raise ValueError("Telefone inválido")