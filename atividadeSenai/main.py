Quant_pessoas = int(input("Quantas pessoas vão ficar com você no mesmo quarto? "))
Cadastro = []
if Quant_pessoas >  0:
    for index in range(Quant_pessoas):
        Cadastro_nome = input("Digite seu nome: ")
        Cadastro_CPF =int(input("Digite seu CPF "))
        Cadastro += [[Cadastro_CPF , Cadastro_nome]]
    print("----Hospedes------")
    for pessoas in Cadastro:
        print(pessoas)
else:
    print("Digite a quantidades de pessoas por favor")