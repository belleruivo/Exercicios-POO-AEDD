from graduacao import Graduacao
from especializacao import Especializacao
from mestrado import Mestrado
from doutorado import Doutorado

def adicionar_estudante(estudantes):
    nome = input("Digite o nome do estudante: ")
    idade = int(input("Digite a idade do estudante: "))
    print("Tipos de estudante: 1. Graduação 2. Especialização 3. Mestrado 4. Doutorado")
    tipo = int(input("Selecione o tipo de estudante (1-4): "))
    
    if tipo == 1:
        clube = input("Digite o clube do estudante: ")
        estudante = Graduacao(nome, idade, clube)
    elif tipo == 2:
        estudante = Especializacao(nome, idade)
    elif tipo == 3:
        estudante = Mestrado(nome, idade)
    elif tipo == 4:
        estudante = Doutorado(nome, idade)
    else:
        print("Tipo inválido. Estudante não adicionado.")
        return
    
    estudantes.append(estudante)
    print(f'Estudante {nome} adicionado com sucesso!')

def listar_estudantes(estudantes):
    if not estudantes:
        print("Nenhum estudante registrado.")
        return
    
    for aluno in estudantes:
        print(f'Nome: {aluno.nome}, Idade: {aluno.idade}, Tipo: {aluno.get_student_type()}')
        if isinstance(aluno, Graduacao):
            print(f'Líder: {aluno.is_lider()}, Clube: {aluno.get_clube()}')

def main():
    estudantes = []
    
    while True:
        print("\nSistema de Gestão Acadêmica")
        print("1. Adicionar Estudante")
        print("2. Listar Estudantes")
        print("3. Sair")
        
        opcao = int(input("Selecione uma opção (1-3): "))
        
        if opcao == 1:
            adicionar_estudante(estudantes)
        elif opcao == 2:
            listar_estudantes(estudantes)
        elif opcao == 3:
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
