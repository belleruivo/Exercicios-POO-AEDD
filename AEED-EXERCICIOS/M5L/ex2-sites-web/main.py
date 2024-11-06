from linked_list import LinkedList

def main():
    # cria a lista ligada para armazenar sites e links
    sites_list = LinkedList()
    
    # inserindo alguns sites na lista
    sites_list.insert("Google", "https://www.google.com")
    sites_list.insert("YouTube", "https://www.youtube.com")
    sites_list.insert("GitHub", "https://www.github.com")
    
    print("Lista de sites antes da busca:")
    sites_list.display()

    # interação com o usuário para buscar um site
    site_name = input("\nDigite o nome do site que deseja buscar: ")
    link = sites_list.search_and_move_to_front(site_name)

    if link:
        print(f"O link para '{site_name}' é: {link}")
    else:
        print(f"O site '{site_name}' não foi encontrado.")

    print("\nLista de sites após a busca:")
    sites_list.display()  # mostra a lista após a busca

if __name__ == "__main__":
    main()  # executa a função principal
