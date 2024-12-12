wordUser = input("Escreva um palavra: ")
vogais = ["a" , "e" , "i" , "o" , "u"]
recorrencias = 0


for i in wordUser:
    if ( i in vogais):
        recorrencias += 1

print("Número de recorrencias das vogáis na frase é: " + str(recorrencias))

