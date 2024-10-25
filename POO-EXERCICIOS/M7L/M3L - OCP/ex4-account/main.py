'''
Refazer as listas M3L e M5L, aplicando o Princípio Aberto-Fechado e mostrar as diferenças
de seu código, antes e depois.
'''

from account import Account
from console_display import ConsoleDisplay
from displayable_account import DisplayableAccount

def main():
    account = Account("João Silva", 1000.0)

    # Passa a estratégia de exibição para a classe DisplayableAccount.
    displayable_account = DisplayableAccount(account, ConsoleDisplay())
    displayable_account.display()

if __name__ == "__main__":
    main()

# Análise do Código
# Classe DisplayStrategy (Estratégia de Exibição):

# Esta classe é uma classe abstrata que define um método display() que deve ser implementado por qualquer classe que herde dela.
# Isso permite que você adicione novas estratégias de exibição no futuro, simplesmente criando novas classes que estendam DisplayStrategy e implementem o método display(). Você não precisa modificar a classe DisplayStrategy ou DisplayableAccount.
# Classe ConsoleDisplay:

# Esta é uma implementação concreta da DisplayStrategy, que exibe os detalhes da conta no console.
# Se você quiser adicionar outro método de exibição (por exemplo, uma exibição em formato de arquivo ou em uma interface gráfica), você poderia criar outra classe que também herda de DisplayStrategy, sem precisar mudar a classe ConsoleDisplay.
# Classe DisplayableAccount:

# Esta classe aceita uma instância de Account e uma estratégia de exibição (que é uma implementação de DisplayStrategy).
# O método display() delega a tarefa de exibir a conta à estratégia de exibição fornecida. Isso significa que você pode alterar a forma como a conta é exibida sem alterar a implementação de DisplayableAccount.
# Extensibilidade:

# Se você precisar de um novo tipo de exibição, basta criar uma nova classe que estenda DisplayStrategy. Por exemplo, você poderia criar uma classe FileDisplay que grava os detalhes da conta em um arquivo. Isso não requer nenhuma modificação nas classes existentes, o que respeita o princípio.