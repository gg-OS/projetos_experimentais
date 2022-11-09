def dados():
    num1 = input('Insira o primeiro elemento: ')
    num2 = input('Insira o segundo elemento: ')
    num1 = float(num1)
    num2 = float(num2)
    return num1, num2


def fatorial(n):
    fat = 1
    for i in range(n):
        fat *= n - i
    return fat


print('Bem-vindo(a) a calculadora ggOS')
operacao = ''
while operacao.title() != 'Sair':
    operacao = input('Menu de operações\n'
                     '--------------------'
                     '1 - Soma\n'
                     '2 - Subtração\n'
                     '3 - Multiplicação\n'
                     '4 - Divisão\n'
                     '5 - Potenciação\n'
                     '6 - Radiciação\n'
                     '7 - Fatorial\n'
                     'Sair - Encerrar o programa\n'
                     '--------------------\n'
                     'Insira a operação desejada: ')
    if operacao == '1':
        x, y = dados()
        resultado = lambda n1, n2: x + y
        print(f'{x} + {y} = {resultado(x,y)}')
    elif operacao == '2':
        x, y = dados()
        resultado = lambda n1, n2: x - y
        print(f'{x} - {y} = {resultado(x,y)}')
    elif operacao == '3':
        x, y = dados()
        resultado = lambda n1, n2: x * y
        print(f'{x} * {y} = {resultado(x, y)}')
    elif operacao == '4':
        x, y = dados()
        if y != 0:
            resultado = lambda n1, n2: x / y
            print(f'{x} / {y} = {resultado(x, y)}')
        else:
            print('Divisão por zero não existe!')
            continue
    elif operacao == '5':
        x, y = dados()
        resultado = lambda n1, n2: x ** y
        print(f'{x} ^ {y} = {resultado(x, y)}')
    elif operacao == '6':
        x, y = dados()
        resultado = lambda n1, n2: x ** (1 / y)
        print(f'{x} sqrt {y} = {resultado(x, y)}')
    elif operacao == '7':
        x = input('Insira o numero que deseja fazer fatorial: ')
        if x.isnumeric():
            x = int(x)
            resultado = fatorial(x)
            print(f'{x}! = {resultado}')
        else:
            print('Dados inválidos.')
            continue
    elif operacao.title() == 'Sair':
        print('\nVocê encerrou o programa.')
    else:
        print('Operação inválida!')
print()
print('powered by ggOS')
