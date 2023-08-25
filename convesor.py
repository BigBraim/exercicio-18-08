from time import sleep
print('')
print('-='*11)
print('''Olá 
Seja Bem-Vindo ao conversor do Brayan''')
print('-='*11)

sleep(2)

n = int(input('Digite um número inteiro: '))

print('''Escolha uma opção
[ 1 ] conversor BINÁRIO
[ 2 ] conversor OCTAL
[ 3 ] conversor HEXADECIMAL''')

sleep(1)

escolha = int(input('Digite sua escolha: '))

if escolha == 1:
    print('O numero {} foi convertido para BINÁRIO é igual a {}'.format(n, bin(n)[2:]))
elif escolha == 2:
    print('O numero {} foi convertido para OCTAL é igual a {}'.format(n, oct(n)[2:]))
elif escolha == 3:
    print('O numero {} foi convertido para HEXADECIMAL é igual a {}'.format(n, hex(n)[2:]))
else:
    print('Escolha inválida. Tente Novamente.')