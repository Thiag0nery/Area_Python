lista = []

while True:
    nome = input("A lista tem " +  str(len(lista)) +" itens. Digite um nome para incluir ")
    if nome == "":
        break
    else:
        lista.append(nome)
        print("Você incluiu " + nome + " a sua lista")
print(lista)