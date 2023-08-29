from time import sleep
print('')


nome = str(input('digite seu nome : ')).strip()

print('-=' * 15)
print('''Ola {}
Seja bem-vindo a loja do Brayan '''.format(nome))
print('-=' * 15)
sleep(1)

print('''Ola {} Vou te Passar Algumas Informações:
- Pagamento a vista em Dinheiro ou Cheque (10% de descontos)
- Pagamento a vista no Cartão (5% De desconto)
- Pagamento em ate 2x no Cartão (Preço Normal)
- pagamento em 3x ou mais no Cartão (20% de juros)'''.format(nome))
print('-=' * 15)
sleep(1)

produto = float(input('Digite o Valor do Produto: '))
print('-=' * 15)
print('''[1] Para Forma de Pagamento a Vista Dinheiro ou Cheque
[2] Para Forma de Pagamento a Vista no Cartão
[3] Para Forma de Pagamento em até 2x no Cartão
[4] Para Forma de Pagamento em 3x ou mais no Cartão''')
print('-=' * 15)
sleep(1)
pagamento = int(input('Qual seria a forma de pagamento: '))
print('-=' * 15)
desconto = produto -(produto *0.1)
desconto1 = produto -(produto *0.05)
juros =  (produto * 0.2) + produto

if pagamento == 1:
    print('O valor a ser pago R${:.2f}'.format(desconto))

elif pagamento == 2:
    print('O valor a ser pago R${:.2f}'.format(desconto1))

elif pagamento == 3:
    print('O valor a ser pago R${:.2f}'.format(produto))

elif pagamento == 4:
    print('O valor a ser pago R${:.2f}'.format(juros))

else:
    print('Erro!! Por Favor Digite um Valor Entre 1 e 4!!')

