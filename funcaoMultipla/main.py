def multiplicar(numero):
    return numero ** 2
def triplicar(numero):
    return numero ** 3
def quaduplicar(numero):
    return numero ** 4

def entrada(funcao1, funcao2, funcao3, numero):
    return funcao1(numero), funcao2(numero), funcao3(numero)

print(entrada(multiplicar, triplicar, quaduplicar, numero=5))