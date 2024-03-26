from random import randint
from time import sleep
import os

def msg_error(msg):
    print(f"\033[31mERROR!\033[m {msg}")

#perguntando a dificuldade 
while True:
    print("[1] - 10 tentativas ")
    print("[2] - 15 tentativas ")
    print("[3] - 20 tentativas ")
    esc = int(input("escolha uma dificuldade: "))
    if esc < 1 or esc > 3:
        msg_error("numero inválido! ")
        continue
    break

plBomb = 0
if esc == 1: plBomb = 10
if esc == 2: plBomb = 15
if esc == 3: plBomb = 20

numBomb = rand = c = jogada = 0
c2 = 1
matriz = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # matriz correspondente 
matrizPrint = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ]
while numBomb < 5:
    try:
        rand = randint(0,26)
        if matriz[rand] == 0:
            matriz[rand] = 1
            numBomb += 1
    except IndexError:
        continue
print(matriz)
while plBomb > 0 and numBomb > 0:
    c2 = 1
    print(f'\033[32mNumero de tentativas: {plBomb}, Barcos restantes: {numBomb}\033[m]')
    print('     1A     2A     3A     4A     5A  ')
    print(f'{c2}B ',end='')
    for i in matrizPrint:
        c += 1
        if c != 5:
            print(f' [ {i.center(2)}] ',end='')
        else:
            c2 += 1
            print(f' [ {i.center(2)}] ')
            if c2 < 6:
              print(f'{c2}B ', end='')
            c = 0
    while True:
        try:
            numA  = int(input('Posição A:'))
        except (ValueError,TypeError):
            print('ERROR! Digite um numero inteiro na ',end='')
            continue
        except (KeyboardInterrupt):
            print('ERROR! Programa interrompido!')
        if numA > 5 or numA < 1:
            print('ERROR! O numero deve estar entre 1 e 5, ', end='')
        else:
            break
    while True:
        try:
            numB  = int(input('Posição B:'))
        except (ValueError,TypeError):
            print('ERROR! Digite um numero inteiro na ',end='')
            continue
        except (KeyboardInterrupt):
            print('ERROR! Programa interrompido!')
        if numB > 5 or numB < 1:
            print('ERROR! O numero deve estar entre 1 e 5, ', end='')
        else:
            break

    jogada = ((numB-1) * 5) + (numA-1)
    if matriz[jogada] == 0:
        if matrizPrint[jogada] == 'X ':
            print('Jogada ja feita')
        else:
            matrizPrint[jogada] = '\033[31mX \033[m'
            plBomb -= 1

    elif matriz[jogada] == 1:
        if matrizPrint[jogada] == '+ ':
            print('Jogada ja feita')
        else:
            matrizPrint[jogada] = '\033[32m+ \033[m'
            numBomb -= 1
            plBomb -= 1
if plBomb == 0 and numBomb > 0:
    print('''
    ----------------------
    VOCÊ PERDEU A PARTIDA!
    ----------------------
    ''')
elif numBomb == 0:
    print('''
        ----------------------
        VOCÊ GANHOU A PARTIDA!
        ----------------------
        ''')
opiniao = input("você gostou do jogo? ")
del opiniao # ninguem liga pra tua opiniao 
