cpf = "746.824.890-70"
cpf = cpf.replace(".","").replace("-","")
contador = 10
resultado = 0
for palavra in cpf[0:10]:
    soma = contador * int(palavra)
    contador -= 1
    resultado += soma

resultado = resultado * 10
resultado = 11 % resultado

if resultado > 9:
    print(resultado)
else:
    print(resultado)