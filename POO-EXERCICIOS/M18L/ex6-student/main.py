from student_factory import StudentFactory

def adicionar_estudante(estudantes):
    nome = input("Digite o nome do estudante: ")
    idade = int(input("Digite a idade do estudante: "))
    curso_nome = input("Digite o nome do curso: ")
    print("Tipos de estudante: 1. Graduação 2. Especialização 3. Mestrado 4. Doutorado")
    tipo = int(input("Selecione o tipo de estudante (1-4): "))
    
    if tipo == 1:
        clube = input("Digite o clube do estudante: ")
        estudante = StudentFactory.create_student(tipo, nome, idade, curso_nome, clube)
    else:
        estudante = StudentFactory.create_student(tipo, nome, idade, curso_nome)
    
    estudantes.append(estudante)
    print(f'Estudante {nome} adicionado com sucesso!')

def listar_estudantes(estudantes):
    if not estudantes:
        print("Nenhum estudante registrado.")
        return
    
    for aluno in estudantes:
        print(f'Nome: {aluno.nome}, Idade: {aluno.idade}, Curso: {aluno.curso.nome}, Tipo: {aluno.get_student_type()}')
        papeis = aluno.obter_papeis()
        if "lider" in papeis:
            print(f'Líder: {papeis["lider"]}')
        if "clube" in papeis:
            print(f'Clube: {papeis["clube"]}')

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
Composição de Classes: Criamos classes componentes (PerfilAcademico, PapelLider, ParticipacaoClube) que são usadas dentro de Student para compor suas funcionalidades.

Classes Concretas: As classes de estudantes (Graduacao, Especializacao, etc.) usam essas classes componentes.

Segregação de Interface: Criamos interfaces específicas para funcionalidades adicionais (LiderInterface e ClubeInterface).

Subclasse Virtual: Registramos Graduacao como subclasse virtual das interfaces.

Princípio da Inversão da Dependência: Usamos uma fábrica (StudentFactory) para instanciar estudantes, desacoplando a lógica de criação da lógica de uso.

Sistema Interativo: Sistema para adicionar e listar estudantes com seus cursos e papéis extras foi mantido.
'''