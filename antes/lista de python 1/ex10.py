from random import randint
palpite = int(input("Qual o seu palpite de número entre 0 a 100: "))
number = randint(0 , 100)

while (palpite != number):
    palpite = int(input("Qual o seu palpite de número entre 0 a 100: "))

    if ( palpite < number):
        palpite = int(input("Que tal um númeor um pouco maior?\n:"))
    elif(palpite < number):
        palpite = int(input("Que tal um númeor um pouco menor?\n:"))

print("Parabens você acertou!!\nO númeor ocrreto era: " +str(number))