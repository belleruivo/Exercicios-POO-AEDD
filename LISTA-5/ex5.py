'''5. Crie uma classe chamada SocialNetwork que represente uma rede social online. Essa
classe deve ter funcionalidades para adicionar amigos, publicar mensagens,
comentar em posts e buscar por usuários.'''

class User:
    def __init__(self, username):
        self.username = username
        self.friends = set()
        self.posts = []
        
def add_friend(self, user):
    if user != self:
        self.friends.add(user)
        self.friends.add(self)
        
def publish_post(self, message):
    post = Post(self, message)
    self.posts.append(post)
    return post
    
class Post:
    def __init__(self, user, message):
        self.user = user
        self.message = message
        self.comments = []
        
    def add_comment(self, user, comment):
        self.comments.append((user, comment))
        
class SocialNetwork:
    def __init__(self):
        self.users = {}
        
    def ass_user(self, username):
        if username not in self.users:
            self.users[username]= User(username)
            return True
        return False
    
    def add_friend(self, username1, username2):
        user1 = self.users.get(username1)
        user2 = self.users.get(username2)
        if user1 and user2:
            user1.add_friend(user2) 
            
    def publish_message(self, username, message):
        user = self.users.get(username)
        if user:
            return user.publish_post(message)      
        
    def comment_on_post(self, username, post, comment):
        user = self.users.get(username)
        if user and post in user.posts:
            post.add_comment(user, comment)
            
    def find_user(self, username):
        return self.users.get(username)  

def main():
    network = SocialNetwork()
    
    
    print("Adicionando usuários...")
    network.add_user("alice")
    network.add_user("bob")
    print("Usuários adicionados: Alice e Bob.")
    
   
    print("Adicionando Bob como amigo de Alice...")
    network.add_friend("alice", "bob")
    print("Amizade estabelecida entre Alice e Bob.")
    
   
    print("Alice publica uma mensagem...")
    post = network.publish_message("alice", "Olá, mundo!")
    print(f"Alice publicou: {post.message}")
    
    
    print("Bob comenta no post de Alice...")
    network.comment_on_post("bob", post, "Oi, Alice!")
    print("Comentário adicionado ao post.")
    
    user = network.find_user("alice")
    if user:
        print(f"Usuário encontrado: {user.username}, Amigos: {[friend.username for friend in user.friends]}, Postagens: {len(user.posts)}")
    else:
        print("Usuário não encontrado.")

main()