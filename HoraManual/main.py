while True:
    try:
        dataUsuario = int(input("Quais são as horas? "))

        if dataUsuario >= 0 and dataUsuario < 12:
            print("Bom dia")

        elif dataUsuario >= 12 and dataUsuario < 18:
            print("Boa tarde")
        else:
            print("Boa a noite!")
        escolhaUsuario = input("Gostaria de rodar o programa novamene? ")

        if escolhaUsuario[0].upper() == "N":
            break


    except:
        print("Opa! aconteceu algo")