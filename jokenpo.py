import random
from time import sleep
print('')


itens = ('Pedra','Papel','Tesoura')

adversario = random.randint(0,2)

print('''Suas opções :
[0] PEDRA
[1] PAPEL
[2] TESOURA''')

jogador = int(input('Qual e a sua jogada ? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)

print('-=' * 11)
print(f'Computador jogou: {itens[adversario]}')
print(f'Jogador jogou: {itens[jogador]}')
print('-=' * 11)

if adversario == 0:

    if jogador == 0:
        print('EMPATOU')

    elif jogador == 1:
        print('VOCÊ GANHOU')

    elif jogador == 2:
        print('COMPUTADOR GANHOU')

    else:
        print('JOGADA INVÁlIDA')

elif adversario == 1:

    if jogador == 0:
        print('COMPUTADOR GANHOU')

    elif jogador == 1:
        print('EMPATOU')

    elif jogador == 2:
        print('VOCÊ GANHOU')
    else:
        print('JOGADA INVÁlIDA')

elif adversario == 2:

    if jogador == 0:
        print('VOCÊ GANHOU')

    elif jogador == 1:
        print('COMPUTADOR GANHOU')

    elif jogador == 2:
        print('EMPATOU')
    else:
        print('JOGADA INVÁlIDA')