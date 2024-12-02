from graduacao import Graduacao
from especializacao import Especializacao
from mestrado import Mestrado
from doutorado import Doutorado
from curso import Curso
from endereco import Endereco

def adicionar_estudante(estudantes):
    nome = input("Digite o nome do estudante: ").capitalize()
    idade = int(input("Digite a idade do estudante: "))
    curso_nome = input("Digite o nome do curso: ")
    curso = Curso(curso_nome)
    rua = input("Digite o nome da rua: ").title()
    numero = input("Digite o número: ")
    cidade = input("Digite a cidade: ").capitalize()
    estado = input("Digite o estado: ").capitalize()
    cep = input("Digite o CEP: ")
    endereco = Endereco(rua, numero, cidade, estado, cep)
    
    print("Tipos de estudante: 1. Graduação 2. Especialização 3. Mestrado 4. Doutorado")
    tipo = int(input("Selecione o tipo de estudante (1-4): "))
    
    if tipo == 1:
        estudante = Graduacao(nome, idade, curso, endereco)
    elif tipo == 2:
        estudante = Especializacao(nome, idade, curso, endereco)
    elif tipo == 3:
        estudante = Mestrado(nome, idade, curso, endereco)
    elif tipo == 4:
        estudante = Doutorado(nome, idade, curso, endereco)
    else:
        print("Tipo inválido. Estudante não adicionado.")
        return
    
    while True:
        opcao_nota = input("Deseja adicionar uma nota ao histórico do estudante? (s/n): ")
        if opcao_nota.lower() == 's':
            while True:
                nota = float(input("Digite a nota (0-10): "))
                if 0 <= nota <= 10:
                    estudante.historico.adicionar_nota(nota)
                    break
                else:
                    print("Nota inválida. Digite uma nota entre 0 e 10.")
        else:
            break

    estudantes.append(estudante)
    print(f'Estudante {nome} adicionado com sucesso!')

def listar_estudantes(estudantes):
    if not estudantes:
        print("Nenhum estudante registrado.")
        return
    
    for aluno in estudantes:
        print(f'Nome: {aluno.nome}, Idade: {aluno.idade}, Tipo: {aluno.get_student_type()}, Curso: {aluno.get_curso()}, Endereço: {aluno.get_endereco()}, Média do Histórico: {aluno.get_historico():.2f}')

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

'''
Composição de Classes: Criamos classes componentes (Curso, Historico, Endereco) que são usadas dentro de Student para compor suas funcionalidades.

Classes Concretas: As classes de estudantes (Graduacao, Especializacao, Mestrado, Doutorado) usam essas classes componentes.

Sistema Interativo: O main.py foi atualizado para incluir a entrada de curso, endereço, e histórico ao adicionar um novo estudante e exibir essas informações ao listar os estudantes.
'''