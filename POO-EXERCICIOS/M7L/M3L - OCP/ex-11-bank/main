# Implemente a classe Bank considerando os métodos listados abaixo e acrescentando 
# métodos que considerar conveniente

from banco import Banco
from poupanca import Poupanca
from verificacao import Verificacao

def main():
    banco = Banco()

    conta_poupanca = Poupanca("Lívia", "1234", 1000, 0.05)
    conta_corrente = Verificacao("Martha", "5678", 2000)

    banco.adicionar(conta_poupanca)
    banco.adicionar(conta_corrente)

    print("Contas no banco:")
    print(banco)

    print(f"\nTotal de juros calculados: R${banco.calcularJuros():.2f}")

main()
