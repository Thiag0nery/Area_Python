import json
arquivo = "C:\\Users\\Thiago\\Desktop\\SENAI - Atividades\\"
arquivo += "arquivo.txt"

pessoa = {
    'nome': 'Luiz Otávio 2',
    'sobrenome': 'Miranda',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
       {'rua': 'R2', 'numeroS': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}
with open("arquivo.json", 'w') as caminho:
   json.dump(pessoa, caminho, indent=2)
with open("arquivo.json", 'r', encoding='utf8') as caminho:
    pessoa = json.load(caminho)
