numUser = int(input("escreva um número: "))
aux = 0
for i in range(numUser):
    if ( i % 2 == 0):
        aux += 1

if ( aux <= 2 ):
    print("O número : " + str(numUser) + " é primo.\n")
elif (numUser == 2):
    print("O número : " + str(numUser) + "é primo. \n")
else:
    print("O número : " + str(numUser) + " não é primo. \n")
