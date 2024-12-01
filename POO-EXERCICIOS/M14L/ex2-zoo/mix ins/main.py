'''
Implemente um sistema de Zoológico com sua classificação (mamífero, ave, réptil, etc.), evidenciando a classe Animal como uma classe abstrata. Por exemplo, considere a estrutura abaixo:
'''

from mamifero import Mamifero
from ave import Ave
from reptil import Reptil

def adicionar_animal(animais):
    nome = input("Digite o nome do animal: ")
    idade = int(input("Digite a idade do animal: "))
    print("Classificações de animal: 1. Mamífero 2. Ave 3. Réptil")
    tipo = int(input("Selecione a classificação do animal (1-3): "))
    
    if tipo == 1:
        animal = Mamifero(nome, idade)
    elif tipo == 2:
        animal = Ave(nome, idade)
    elif tipo == 3:
        animal = Reptil(nome, idade)
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
        print(f'Nome: {animal.nome}, Idade: {animal.idade}, Classificação: {animal.get_classificacao()}, Som: {animal.emitir_som()}')
        if isinstance(animal, Ave):
            print(animal.voar())
        if isinstance(animal, Reptil):
            print(animal.nadar())

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
Versão com Mix-Ins: Implementamos funcionalidades Voar e Nadar usando classes Mix-Ins.

Versão com Interfaces: Implementamos as mesmas funcionalidades usando interfaces.
'''