'''
Implemente um sistema de Zoológico com sua classificação (mamífero, ave, réptil, etc.), evidenciando a classe Animal como uma classe abstrata. Por exemplo, considere a estrutura abaixo:
'''
from mamifero import Mamifero
from ave import Ave
from reptil import Reptil
from habitat import Habitat

def adicionar_animal(animais):
    nome = input("Digite o nome do animal: ")
    idade = int(input("Digite a idade do animal: "))
    habitat_tipo = input("Digite o tipo de habitat do animal: ")
    habitat = Habitat(habitat_tipo)
    print("Classificações de animal: 1. Mamífero 2. Ave 3. Réptil")
    tipo = int(input("Selecione a classificação do animal (1-3): "))
    
    if tipo == 1:
        animal = Mamifero(nome, idade, habitat)
    elif tipo == 2:
        animal = Ave(nome, idade, habitat)
    elif tipo == 3:
        animal = Reptil(nome, idade, habitat)
    else:
        print("Classificação inválida. Animal não adicionado.")
        return
    
    animais.append(animal)
    print(f'Animal {nome} adicionado com sucesso!')

def listar_animais(animais):
    if not animais:
        print("Nenhum animal registrado.")
        return
    
    for animal in animais:
        print(f'Nome: {animal.nome}, Idade: {animal.idade}, Classificação: {animal.get_classificacao()}, Som: {animal.emitir_som()}, Habitat: {animal.habitat.get_tipo()}')

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
Agregação de Classes: Criamos a classe Habitat que é agregada à classe Animal, representando o ambiente de cada animal.

Classes Concretas: As classes Ave, Mamifero, e Reptil agora possuem um habitat agregado.

Sistema Interativo: O main.py foi atualizado para incluir a entrada do habitat ao adicionar um novo animal e exibir o habitat ao listar os animais.
'''