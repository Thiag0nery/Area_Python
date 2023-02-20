nome = input("Qual é o seu nome? ")
idade = input("Qual a sua idade? ")

if nome and idade:
    if nome in "":
        print("O seu nome tem espaços")
    else:
        print("O seu nome não contem espaços ")

    print(f'O seu nome invertidop é: {nome[::-1]}')
    print(f' O seu nome possui  {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é: {nome[-1]}')
else:
    if bool(nome) == False:
        print("O dado nome esta faltando informações")
    elif bool(idade) == False:
        print("O dado idade esta faltando informações")
