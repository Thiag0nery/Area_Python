def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return  number * 3 + 1
numero = int(input("Digite um numero"))

while True:
    print(collatz(numero))
    numero = collatz(numero);

    if collatz(numero) == 1:
        print(collatz(numero))
        break