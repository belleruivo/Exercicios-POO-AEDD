from animal_factory import AnimalFactory

def adicionar_animal(animais):
    nome = input("Digite o nome do animal: ")
    idade = int(input("Digite a idade do animal: "))
    print("Classificações de animal: 1. Mamífero 2. Ave 3. Réptil")
    tipo = int(input("Selecione a classificação do animal (1-3): "))
    
    try:
        animal = AnimalFactory.create_animal(tipo, nome, idade)
        animais.append(animal)
        print(f'Animal {nome} adicionado com sucesso!')
    except ValueError as e:
        print(e)

def listar_animais(animais):
    if not animais:
        print("Nenhum animal registrado.")
        return
    
    for animal in animais:
        print(f'Nome: {animal.nome}, Idade: {animal.idade}, Classificação: {animal.get_classificacao()}, Som: {animal.emitir_som()}')

def main():
    animais = []
    
    while True:
        print("\nSistema de Gestão do Zoológico")
        print("1. Adicionar Animal")
        print("2. Listar Animais")
        print("3. Sair")
        
        opcao = int(input("Selecione uma opção (1-3): "))
        
        if opcao == 1:
            adicionar_animal(animais)
        elif opcao == 2:
            listar_animais(animais)
        elif opcao == 3:
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()

'''
Princípio da Inversão da Dependência: Criamos uma fábrica (AnimalFactory) para instanciar os objetos Animal, desacoplando a lógica de criação da lógica de uso.

Classes Concretas: As classes Ave, Mamifero e Reptil continuam implementando a abstração Animal.

Sistema Interativo: O main.py usa a fábrica para adicionar e listar animais no zoológico.
'''