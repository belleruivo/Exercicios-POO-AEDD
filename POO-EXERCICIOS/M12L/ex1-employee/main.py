from employee import *
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
            print(f"Erro. Por favor, escolha 1 ou 2.\n")


    nome = input("\nDigite o nome: ")
    matricula = input("Digite a matrícula: ")


    while True:
        try:
            salario = float(input("Digite o salário: R$"))
            break
        except ValueError:
            print("Insira somente valores numéricos\n")


    if opcao == 1:
        while True:
            turno = input("Digite o turno (dia/noite): ").lower()
            if turno in ["dia", "noite"]:
                break
            print("Turno inválido! Digite 'dia' ou 'noite'.\n")
        
        if turno == "noite":
            while True:
                try:
                    adicional_noturno = float(input("Digite o adicional noturno: R$")) 
                    break 
                except ValueError:
                    print("Certifique-se de inserir somente caracteres numéricos\n")  
        
        else:
            adicional_noturno = 0
                    
        assistente = AdministrativeAssistant(nome, matricula, salario, turno, adicional_noturno)  
    
        
    else:
        while True:
            try:
                bonus = float(input("Insira o bonús salarial: "))
                break
            except ValueError:
                print("Certifique-se de inserir um caractere numérico válido.\n")
                
        assistente = TecnicalAssistant(nome, matricula, salario, bonus)

    print("\nDados do Funcionário:")
    print(assistente)
    print("-="*20)
    
main()