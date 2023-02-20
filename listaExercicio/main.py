Lista = []
while True:
    try:
        opcao = input("Digite uma opção: [i]nsire | [d]eletar | [l]ista | [e]xit \n")

        if opcao.startswith("i"):
            item = input("Digite um valor para incluir na lista")
            Lista.append(item)

        elif opcao.startswith("d"):
            try:
                deletar = int(input("Qual valor você quer deletar? \n"))
                del Lista[deletar]
            except ValueError:
                print("Valor não existe na lista")

        elif opcao.startswith("l"):
            if len(Lista) == 0:
                print("Sem nada na lista")
            else:
                for numero in range(len(Lista)):
                    print(f" {numero} -- {Lista[numero]}")
        elif opcao.startswith("e"):
            for numero in range(len(Lista)):
                print(f" {numero} -- {Lista[numero]}")
            break
        else:
            print("Digite uma opção!")

    except:
        print("Algo deu errado")