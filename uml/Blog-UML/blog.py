from postagem import Postagem
import datetime

class Blog:
    postagens : list[Postagem]

    def __init__(self):
        self.postagens = []

    def adicionarPostagem (self, postagem : Postagem):
        self.postagens.append(postagem);

    def publicarPostagem (self , postagem : Postagem ):
        for post in self.postagens :
            if (post._id == postagem._id):
                post._dataPublicacao = datetime.datetime.now()
                print(post._titulo + "\n" + post._texto)
                return

    def listarPostagensPublicadas (self):
        for post in self.postagens:
            now = datetime.datetime.now()
            diferenca = post._dataPublicacao - now

            if ( diferenca <= datetime.timedelta(0)):
                print("Titulo: " + post._titulo + "\nTexto: " + post._texto );

    def listarTodasAsPostagens (self):
        for post in self.postagens:
            print("Titulo: " + post._titulo + "\nTexto: " + post._texto );



