def soma(number1, number2):
    resultado = number1 + number2
    return print(resultado)

def subtracao(number1, number2):
    resultado = number1 - number2
    return print(resultado)

def multiplicacao(number1, number2):
    resultado = number1 * number2
    return print(resultado)

def divisao(number1, number2):
    resultado = number1 / number2
    return print(resultado)

while True:
    try:
        number_1 = float(input("Digite um numero: "))
        number_2 = float(input("Digite outro numero: "))
        escolha = input("Escolha a operação: + | - | * | /")

        if escolha.startswith("+"):
            soma(number_1,number_2)

        elif escolha.startswith("-"):
            subtracao(number_1,number_2)

        elif escolha.startswith("*"):
            multiplicacao(number_1,number_2)

        elif escolha.startswith("/"):
            divisao(number_1,number_2)
        else:
            print("Digite um valor valido")
    except:
        print("Algo deu errado")

    repeticao = input("Deseja sair? Sim ou s").upper().startswith("S")
    if repeticao:
        break