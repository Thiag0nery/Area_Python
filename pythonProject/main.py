import random

numeroSecreto = random.randint(1, 30)

for number in range(1, 7):
    try:
        usuario = int(input("Escolha um numero! voce tem 6 chances e voce esta na chance: " + str(number)))

        if usuario > numeroSecreto:
             print("Muito alto")
        elif usuario < numeroSecreto:
            print("Muito baixo")
        else:
            break
    except ValueError:
        print("Valor incoerente")
#Fim do for
if usuario == numeroSecreto:
    print("Parabens voce conseguiu! O numero aleatorio era: ", numeroSecreto)
else:
    print("Voce perdeu! :(")