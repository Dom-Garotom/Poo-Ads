lista = []
result = 0

while (True) :
    lista.append(input("escreva um número terminado por um zero: "))
    end = input("Terminou? s/n \n")
    if end == "s":
        break


for i in lista:
    result += int(i)



print(result)