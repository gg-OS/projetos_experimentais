import math


def binario(x):
    num_bin = ''
    while x >= 1:
        resto = x % 2
        num_bin = str(resto) + num_bin
        x = math.floor(x / 2)
    num_bin = str(x) + num_bin
    return num_bin


def octal(x):
    num_bin = ''
    while x >= 1:
        resto = x % 8
        num_bin = str(resto) + num_bin
        x = math.floor(x / 8)
    num_bin = str(x) + num_bin
    num_bin = num_bin[1:]
    return num_bin


def hexadecimal(x):
    num_bin = ''
    while x >= 1:
        resto = x % 16
        if resto == 10:
            num = 'A'
        elif resto == 11:
            num = 'B'
        elif resto == 12:
            num = 'C'
        elif resto == 13:
            num = 'D'
        elif resto == 14:
            num = 'E'
        elif resto == 15:
            num = 'F'
        else:
            num = str(resto)
        num_bin = num + num_bin
        x = math.floor(x / 16)
    return num_bin


print('Seja bem vindo(a) ao conversor de bases ggOS®')
print()
print('Digite "encerrar" para encerrar o programa')
print()
while True:
    numero = input('Insira o número que deseja converter: ')
    if numero.title() == 'Encerrar':
        break
    if not numero.isnumeric():
        print()
        print('Dados inválidos')
        print()
        continue
    else:
        numero = int(numero)
        base = input('Insira a base para a qual deseja converter '
                     '(b = Binário / o = Octal / h = Hexadecimal): ')
        print()
        if base.upper() == 'B':
            print(f'{numero} = {binario(numero)} em binário')
        elif base.upper() == 'O':
            print(f'{numero} = {octal(numero)} em octal')
        elif base.upper() == 'H':
            print(f'{numero} = {hexadecimal(numero)} em hexadecimal')
        else:
            print('Base inválida')
            print()
            continue
        print()

print()
print('powered by ggOS®')
