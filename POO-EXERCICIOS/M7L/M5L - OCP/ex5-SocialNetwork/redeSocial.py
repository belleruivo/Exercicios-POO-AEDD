from usuario import UsuarioBase

class SocialNetwork:
    def __init__(self):
        self.usuarios = []

    def adicionar_usuario(self, nome):
        email = self.validar_email()
        if not email:
            return None

        usuario = UsuarioBase(nome, email)
        self.usuarios.append(usuario)
        print(f"Usuário {nome} ({email}) foi adicionado à rede.")
        return usuario
    
    def buscar_usuario_por_nome(self, nome_procurado):
        usuarios_encontrados = [usuario for usuario in self.usuarios if usuario.nome.lower() == nome_procurado.lower()]
        
        if not usuarios_encontrados:
            print("Usuário não encontrado.")
            return None

        if len(usuarios_encontrados) == 1:
            usuario = usuarios_encontrados[0]
            print(f"Usuário encontrado: {usuario.nome} ({usuario.email})")
            return usuario
        else:
            print(f"Vários usuários encontrados com o nome '{nome_procurado}':")
            for i, usuario in enumerate(usuarios_encontrados, start=1):
                print(f"{i}. {usuario.nome} ({usuario.email})")

            try:
                num_selecao = int(input("Selecione o número do usuário que você estava procurando: ")) - 1
                if 0 <= num_selecao < len(usuarios_encontrados):
                    usuario_selecionado = usuarios_encontrados[num_selecao]
                    print(f"Usuário selecionado: {usuario_selecionado.nome} ({usuario_selecionado.email})")
                    return usuario_selecionado
                else:
                    print("Número inválido.")
            except ValueError:
                print("Entrada inválida. Por favor, insira um número.")
        return None

    def validar_email(self):
        while True:
            email = input("Email do usuário: ")
            if '@' not in email:
                print("Email inválido. O email deve conter '@'. Tente novamente.")
                continue
            if any(usuario.email == email for usuario in self.usuarios):
                print(f"Já existe um usuário cadastrado com o email {email}.\n")
                continue
            return email

    def buscar_usuario_por_numero(self, numero):
        if 0 <= numero < len(self.usuarios):
            return self.usuarios[numero]
        print("Número de usuário inválido.")
        return None

    def listar_usuarios(self):
        if not self.usuarios:
            print("Nenhum usuário cadastrado.")
            return
        print("Usuários cadastrados:")
        for i, usuario in enumerate(self.usuarios, start=1):
            print(f"{i}. {usuario.nome} ({usuario.email})")

    def listar_posts(self, usuario):
        if not usuario.posts:
            return  
        print(f"Posts de {usuario.nome}:")
        for i, post in enumerate(usuario.posts, start=1):
            print(f"{i}. {post.conteudo}")