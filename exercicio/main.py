nome = input("Nome")
letra = 0
nomeNome = ''
while letra < len(nome):
    nomeVindo = nome[letra]
    nomeNome += f'*{nomeVindo}'
    letra += 1

print(nomeNome)