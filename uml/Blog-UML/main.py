from datetime import datetime
from postagem import Postagem
from blog import Blog
from user import User

def menu():
    print("\n=== Sistema de Blog ===")
    print("1. Adicionar Postagem")
    print("2. Publicar Postagem")
    print("3. Listar Todas as Postagens")
    print("4. Listar Postagens Publicadas")
    print("5. Sair")
    return input("Escolha uma opção: ")


def login():
    nome = input("Informe seu nome \n")
    email = input("Informe seu email \n")
    senha = input("Informe sua senha \n")
    userSystem = User(nome , email , senha)

    return userSystem

def system () :
    while True:
        opcao = menu()

        match opcao:
            case "1":
                titulo = input("Digite o título da postagem: ")
                ano = int(input("Digite o ano de publicação: "))
                mes = int(input("Digite o mês de publicação: "))
                dia = int(input("Digite o dia de publicação: "))

                nova_postagem = Postagem(titulo, ano, mes, dia)
                meu_blog.adicionarPostagem(nova_postagem)
                print("Postagem adicionada com sucesso!")

            case "2":
                if not meu_blog.postagens:
                    print("Nenhuma postagem para publicar.")
                    continue

                print("Postagens disponíveis para publicação:")
                for i, postagem in enumerate(meu_blog.postagens):
                    print(f"{i + 1}. {postagem._titulo}")

                escolha = int(input("Escolha o número da postagem para publicar: "))
                if 1 <= escolha <= len(meu_blog.postagens):
                    meu_blog.publicarPostagem(meu_blog.postagens[escolha - 1])
                    print("Postagem publicada com sucesso!")
                else:
                    print("Opção inválida.")

            case "3":
                print("\n--- Todas as Postagens ---")
                meu_blog.listarTodasAsPostagens()

            case "4":
                print("\n--- Postagens Publicadas ---")
                meu_blog.listarPostagensPublicadas()

            case "5":
                print("Saindo do sistema...")
                break

            case _:
                print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    meu_blog = Blog()
    
    userLogged = login()  

    while not userLogged:
        print("Usuario não está logado") 
        userLogged = login()

    system()
    