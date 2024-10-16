'''5. Crie uma classe chamada SocialNetwork que represente uma rede social online. Essa
classe deve ter funcionalidades para adicionar amigos, publicar mensagens,
comentar em posts e buscar por usuários.'''

from redeSocial import SocialNetwork
from post import *

def menu():
    rede = SocialNetwork()
    print("-=" * 30)
    while True:
        print("MENU:")
        print("1. Adicionar Usuário")
        print("2. Adicionar Amigo")
        print("3. Publicar Post")
        print("4. Comentar em Post")
        print("5. Buscar Usuário")
        print("6. Sair\n")

        escolha = input("Escolha uma opção: ")
        print()

        if escolha == '1':
            nome = input("Nome do usuário: ")
            rede.adicionar_usuario(nome)

        elif escolha == '2':
            rede.listar_usuarios()  # Exibir lista de usuários
            try:
                num1 = int(input("Número do usuário que vai adicionar um amigo: ")) - 1
                num2 = int(input("Número do amigo a ser adicionado: ")) - 1
                usuario1 = rede.buscar_usuario_por_numero(num1)
                usuario2 = rede.buscar_usuario_por_numero(num2)
                if usuario1 and usuario2:
                    usuario1.adicionar_amigo(usuario2)
            except ValueError:
                print("Entrada inválida. Por favor, insira números.")

        elif escolha == '3':
            rede.listar_usuarios()  # Exibir lista de usuários
            try:
                num = int(input("Número do usuário que vai publicar: ")) - 1
                usuario = rede.buscar_usuario_por_numero(num)
                if usuario:
                    print("\nEscolha o tipo de post:")
                    print("1. Texto")
                    print("2. Imagem")
                    print("3. Vídeo")
                    tipo_post = input("Digite o número do tipo de post: ")
                    conteudo = input("Escreva o conteúdo do post: ")

                    if tipo_post in ['2', '3']:
                        midia = input("Insira a URL da mídia (imagem ou vídeo): ")
                        post = PostFactory.criar_post(tipo_post, conteudo, usuario, midia)
                    else:
                        post = PostFactory.criar_post(tipo_post, conteudo, usuario)

                    usuario.publicar_post(post)

            except ValueError:
                print("Entrada inválida. Por favor, insira um número.")

        elif escolha == '4':
            rede.listar_usuarios()  # Exibir lista de usuários
            try:
                num = int(input("Número do usuário que vai comentar: ")) - 1
                usuario = rede.buscar_usuario_por_numero(num)
                if usuario:
                    amigos_com_posts = [amigo for amigo in usuario.amigos if amigo.posts]

                    if not amigos_com_posts:
                        print("Nenhum amigo tem posts para comentar.")
                        continue

                    # Exibir lista de amigos com posts
                    print("Amigos com posts:")
                    for i, amigo in enumerate(amigos_com_posts, start=1):
                        print(f"{i}. {amigo.nome}")

                    try:
                        num_autor = int(input("Número do autor do post que você deseja comentar: ")) - 1
                        if 0 <= num_autor < len(amigos_com_posts):
                            usuario_autor = amigos_com_posts[num_autor]
                            rede.listar_posts(usuario_autor)  # Exibir os posts do autor selecionado

                            if usuario_autor.posts:
                                num_post = int(input("Número do post para comentar: ")) - 1
                                if 0 <= num_post < len(usuario_autor.posts):
                                    comentario = input("Escreva seu comentário: ")
                                    usuario.comentar_post(usuario_autor.posts[num_post], comentario)
                                else:
                                    print("Número de post inválido.")
                            else:
                                print(f"{usuario_autor.nome} não tem posts.")
                        else:
                            print("Número de autor inválido.")
                    except ValueError:
                        print("Entrada inválida. Por favor, insira um número.")
            except ValueError:
                print("Entrada inválida. Por favor, insira um número.")

        elif escolha == '5':
            nome_procurado = input("Nome do usuário a ser buscado: ")
            rede.buscar_usuario_por_nome(nome_procurado)

        elif escolha == '6':
            break

        print("-=" * 30)


menu()
