import time


def tempo_reverso():
    if temporizador >= 60:
        tempo[0] = round(temporizador / 60)
        tempo[1] = temporizador % 60
    else:
        tempo[1] = temporizador
    while tempo[0] != 0 or tempo[1] != 0 or tempo[2] != 0:
        if tempo[1] == 0 and tempo[2] == 0:
            if tempo[0] > 0:
                tempo[0] -= 1
            tempo[1] = 59
            tempo[2] = 60
        elif tempo[2] == 00:
            tempo[1] -= 1
            tempo[2] = 60
        tempo[2] -= 1
        print(f'{tempo[0]}:{tempo[1]}:{tempo[2]}')
        time.sleep(1)


funcao = ''
cronometro = ''
tempo = [00, 00, 00]
while funcao != '0':
    funcao = input('1 - Cronômetro\n'
                   '2 - Temporizador\n'
                   '3 - Estudar (Pomodoro)\n'
                   '0 - Desligar\n'
                   'Insira a função desejada: ')
    if funcao == '1':
        print('Insira "0" para encerrar o cronômetro.')
        while cronometro != '0':
            tempo[2] += 1
            if tempo[2] == 60:
                tempo[1] += 1
                tempo[2] = 00
            print(f'{tempo[0]}:{tempo[1]}:{tempo[2]}')
            time.sleep(1)
    elif funcao == '2':
        temporizador = input('Insira a quantidade de minutos que deseja temporizar: ')
        temporizador = int(temporizador)
        tempo_reverso()
    elif funcao == '3':
        print('1 - 50 minutos de trabalho e 10 de descanso\n'
              '2 - 45 minutos de trabalho e 15 de descanso\n'
              '3 - 40 minutos de trabalho e 20 de descanso\n'
              '4 - 30 minutos de trabalho e 30 de descanso\n')
        parametro = input('Insira o parâmetro desejado: ')
        if parametro == '1':
            atividade = input('Digite "start" para começar: ')
            while atividade.lower() == 'start':
                temporizador = 50
                tempo_reverso()
                print('------------------------- TEMPO DE DESCANSO -------------------------')
                temporizador = 10
                tempo_reverso()
                atividade = input('Digite "start" para iniciar mais um ciclo: ')
        elif parametro == '2':
            atividade = input('Digite "start" para começar: ')
            while atividade.lower() == 'start':
                temporizador = 45
                tempo_reverso()
                print('------------------------- TEMPO DE DESCANSO -------------------------')
                temporizador = 15
                tempo_reverso()
                atividade = input('Digite "start" para iniciar mais um ciclo: ')
        elif parametro == '3':
            atividade = input('Digite "start" para começar: ')
            while atividade.lower() == 'start':
                temporizador = 40
                tempo_reverso()
                print('------------------------- TEMPO DE DESCANSO -------------------------')
                temporizador = 20
                tempo_reverso()
                atividade = input('Digite "start" para iniciar mais um ciclo: ')
        elif parametro == '4':
            print('Para de ser preguiçoso, escolha outra opção. >:(')
            continue
        else:
            print('Parâmetro inválido, insira um número de 1 a 4.')
            continue
    else:
        print('Função inválida, insira um número de 1 a 3.')
        continue
