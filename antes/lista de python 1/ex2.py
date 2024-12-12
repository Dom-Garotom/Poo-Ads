numUser = int(input("escreva um número:"))
fatorial = 1


for x in range(numUser):
    fatorial += fatorial * (x) ;     

print(fatorial)