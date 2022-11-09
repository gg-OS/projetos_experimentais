import random
print('Bem vindo ao gerador de senhas ggOS!')
fraca = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x',
         'y', 'w', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
media = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x',
         'y', 'w', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
         'J', 'K', 'L', 'M', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'W', 'Z']
forte = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x',
         'y', 'w', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
         'J', 'K', 'L', 'M', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'W', 'Z', '!', '@', '#', '$', '%', '&',
         '*', '(', ')', '?', '-', '+', '>', '<', '~', ']', '[']
senha = ''
forca = input('Você quer uma senha\n'
              '1 - Fraca\n'
              '2 - Mediana\n'
              '3 - Forte\n'          
              'Insira a opção desejada: ')
tamanho = input('Insira o tamanho desejado da senha: ')
tamanho = int(tamanho)
if forca.title() == 'Fraca':
    for i in range(tamanho):
        senha += fraca[random.randint(0, len(fraca))]
    print(f'Senha = {senha}')
elif forca.title() == 'Mediana':
    for i in range(tamanho):
        senha += media[random.randint(0, len(media))]
    print(f'Senha = {senha}')
elif forca.title() == 'Forte':
    for i in range(tamanho):
        senha += forte[random.randint(0, len(forte))]
    print(f'Senha = {senha}')
else:
    print('Tipo inválido.')
    print('Execute novamente o programa.')
print()
print('powered by ggOS®')
