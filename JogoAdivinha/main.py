import random

lista = ["FLOR","TIGRE","BARCO","PIMENTA","VESPA","SAPO","GATO"]
numeroAleatorio = random.randint(0,3)
palavraSecreta = lista[numeroAleatorio]
palavra = ""
contagem = 0
print(f'A palavra secreta tem: {len(palavraSecreta)} letras')
while True:
    digitado = input("Escolha UMA letra: \n", ).upper()

    if digitado[0] in palavraSecreta:
        palavra += f"{digitado[0]}"

    print("Resultado: ",  end="")
    for i in palavraSecreta:
        if i in palavra:
            print(f"{palavra}", end="")
        else:
            print("*", end="")

    resposta = input(f"\n Qual é a palavra secreta? Chance de {contagem} a 2\n").upper()
    if resposta == palavraSecreta:
        print("Voce ganhou!")
        break
    else:
        contagem += 1
        print(f"Você errou!")
    if contagem >= 2:
        print("Voce perdeu! Pelo numero de chance ")
        break