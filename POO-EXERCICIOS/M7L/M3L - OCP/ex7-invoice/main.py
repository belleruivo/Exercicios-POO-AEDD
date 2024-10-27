# Crie uma classe Fatura para que uma loja de suprimentos de informática possa
# utilizá-la para representar a fatura de um item vendido na loja. Uma Fatura deve
# incluir quatro variáveis de instância: o número da fatura (string), a descrição (string),
# a quantidade comprada de um item (int) e o preço por item (float). Sua classe deve ter
# um construtor que inicializa as quatro variáveis de instância.
# Forneça um método set e um get para cada variável de instância. Forneça também um método chamado que
# calcula o valor da fatura (multiplica preço por quantidade do item) e retorna o
# resultado. Se a quantidade de itens passada pelo usuário não for positiva, deve ser
# configurada como 0. Se o preço do item não for positivo, deve ser configurado como
# 0.0. Teste a classe implementada e seus métodos.

from fatura import Fatura 
from faturaComDesconto import FaturaComDesconto

print("-" * 30)
print("     LOJA DE INFORMÁTICA")
print("-" * 30)

def main():
    numFatura = input("Digite o número da fatura: ")
    descricao = input("Digite a descrição do item: ")
    quantidade = int(input("Digite a quantidade: "))
    precoItem = float(input("Digite o preço por item: R$"))

    tipo_fatura = input("Digite 'normal' para fatura normal ou 'desconto' para fatura com desconto: ").strip().lower()

    if tipo_fatura == 'desconto':
        desconto = float(input("Digite o desconto em percentual: "))
        fatura = FaturaComDesconto(numFatura, descricao, quantidade, precoItem, desconto)
    else:
        fatura = Fatura(numFatura, descricao, quantidade, precoItem)

    print("-" * 30)
    print("       FATURA")
    print("-" * 30)
    print(fatura)

    nova_quantidade = int(input("\nDigite uma nova quantidade (ou 0 para sair): "))
    if nova_quantidade > 0:
        fatura.quantidade = nova_quantidade 

    novo_preco = float(input("Digite um novo preço por item (ou 0 para sair): "))
    if novo_preco > 0:
        fatura.precoItem = novo_preco

    print("\nFatura ajustada:")
    print(fatura)

main()
