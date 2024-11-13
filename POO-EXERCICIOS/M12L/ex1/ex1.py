'''1. Implemente a classe Employee com nome, número de matrícula e salário.
a. Crie um método para exibir os dados.
b. Crie as classes AdministrativeAssistant e TecnicalAssistent, herdando de
Employee.
c. Sabendo que os assistentes técnicos possuem um bônus salarial e que os
assistentes administrativos possuem um turno (dia ou noite) e um adicional
noturno, sobrescreva o método que exibe os dados.'''


class Employee:
    def __init__(self, nome, matricula, salario):
        self.nome = nome
        self.matricula = matricula
        self.salario = salario


    def __str__(self):
        return f"Nome: {self.nome}, Matricula: {self.matricula}, Salário: {self.salario:.2f}"
   
class AdministrativeAssistant(Employee):
    def __init__(self, nome, matricula, salario, turno, adicional_noturno):
        super().__init__(nome, matricula, salario)
        self.turno = turno
        self.adicional_noturno = adicional_noturno


    def __str__(self):
        return (f"Nome: {self.nome}, Matricula: {self.matricula}, Salário: {self.salario} "
                f"Turno: {self.turno}, Adicional Noturno: {self.adicional_noturno:.2f}")

class TecnicalAssistent(Employee):
    def __init__(self, nome, matricula, salario, bonus_salarial):
        super().__init__(nome, matricula, salario)
        self.bonus_salarial = bonus_salarial


    def __str__(self):
        return (f"Nome: {self.nome}, Matricula: {self.matricula}, Salário: {self.salario}"
                f"Bônus Salarial: {self.bonus_salarial:.2f}")


def main():
    print("-="*20)
    print("Escolha o tipo de funcionário:")
    print("1 - Assistente Administrativo")
    print("2 - Assistente Técnico")

    while True:
        try:
            opcao = int(input("Escolha uma opção: "))
            if opcao not in [1, 2]:
                raise ValueError("Escolha uma opção válida.")
            break
        except ValueError:
            print(f"Erro. Por favor, escolha 1 ou 2.")


    nome = input("\nDigite o nome: ")
    matricula = input("Digite a matrícula: ")


    while True:
        try:
            salario = float(input("Digite o salário: R$"))
            break
        except ValueError:
            print("Insira somente valores numéricos")


    if opcao == 1:
        while True:
            turno = input("Digite o turno (dia/noite): ").lower()
            if turno in ["dia", "noite"]:
                break
            print("Turno inválido! Digite 'dia' ou 'noite'.\n")
        
        while True:
            try:
                adicional_noturno = float(input("Digite o adicional noturno: R$")) 
                break 
            except ValueError:
                print("Certifique-se de inserir somente caracteres nuéricos")  
                
        assistente = AdministrativeAssistant(nome, matricula, salario, turno, adicional_noturno)  
    
        
    else:
        while True:
            try:
                bonus = float(input("Insira o bonús salarial: "))
                break
            except ValueError:
                print("Certifique-se de inserir um caractere numérico válido.")
                
        assistente = TecnicalAssistent(nome, matricula, salario, bonus)

    print("\nDados do Funcionário")
    print(assistente)
    
main()