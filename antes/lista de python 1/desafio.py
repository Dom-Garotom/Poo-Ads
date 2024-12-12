alunos = [
    {"nome": "João Silva", "nota1": 3.5, "nota2": 5.0, "nota3": 9.2},
    {"nome": "Maria Oliveira", "nota1": 5.5, "nota2": 8.0, "nota3": 6.9},
    {"nome": "Pedro Santos", "nota1": 9.0, "nota2": 9.8, "nota3": 7.5},
    {"nome": "Ana Costa", "nota1": 6.5, "nota2": 4.3, "nota3": 8.4},
    {"nome": "Lucas Almeida", "nota1": 8.2, "nota2": 9.1, "nota3": 7.8},
    {"nome": "Paula Souza", "nota1": 7.0, "nota2": 3.5, "nota3": 5.0},
    {"nome": "Rafael Pereira", "nota1": 6.8, "nota2": 7.9, "nota3": 8.6},
    {"nome": "Beatriz Lima", "nota1": 9.1, "nota2": 8.4, "nota3": 9.0},
    {"nome": "Carlos Silva", "nota1": 7.6, "nota2": 8.2, "nota3": 7.5},
    {"nome": "Fernanda Rocha", "nota1": 9.0, "nota2": 10.0, "nota3": 9.8}
]


def adicionarAluno () :
    name = input("Nome do aluno: ")
    notaOne = float(input("Nota n°1 do" +name+ " :"))
    notaTwo = float(input("Nota n°2 do" +name+ " :"))
    notaThree = float(input("Nota n°3 do " +name+ " :"))

    alunos.append({
        "nome": name,
        "nota1": notaOne, 
        "nota2": notaTwo, 
        "nota3": notaThree
    })

def gerarRelatorio():
    print("\n\nRelátorio da turma")
    print("{:<15} {:<6} {:<6} {:<6} {:<6} {:<6}".format("Nome" , "N1",  "N2"  , "N3" , "Media" , "Situação") + "\n")
    mediaGeral = 0.0


    for aluno in alunos:
        media = (aluno["nota1"] + aluno["nota2"] + aluno["nota3"] ) / 3
        media = round(media , 2)
        print("{:<15} {:<6} {:<6} {:<6} {:<6} {:<6}".format(
            aluno["nome"] , str(aluno["nota1"])  , str(aluno["nota2"] ), 
            str(aluno["nota3"])  , str(media) , ("Aprovado" if media >= 7 else "Reprovado") 
        ))

        mediaGeral += media
    
    mediaGeral = round( mediaGeral / len(alunos) , 2)

    print("\nMedia Geral da Turma : " , mediaGeral, "\n")
    

def system () :
    key = False

    while ( key != True ):
        print("O que você gostaria de fazer?\n"
            + "1 - Adicionar um Aluno novo:\n"
            + "2 - Gerar o relatorio da turma:\n" 
            + "3 - sair\n" 
        )

        action = input()

        if (action):
            match action:
                case "1":
                    adicionarAluno()
                case "2":
                    gerarRelatorio()
                case "3":
                    key = True
                case _:
                    print("Escreva um valor válido")
system()

