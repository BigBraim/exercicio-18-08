from time import sleep
print('')

name = str(input('Digite seu nome: '))

print('-='*19)
print('''Olá {}
Seja Bem-Vindo ao banco do Brayan'''.format(name))
print('-='*19)

sleep(1)

print('''Nosso banco trabalha apenas com empréstimos
- Nós cobramos 10% de juros nos empréstimo
- Se o valor da prestação do empréstimo for maior que 30% do seu salário o empréstimo será NEGADO!''')
print('-='*11)

sleep(1)

casa = float(input('Valor da casa R$ '))
salario = float(input('Qual o seu salário? '))
anos = int(input('Quantos anos de financiamento? '))
minimo = salario * 30 / 100

parcela = casa / (anos * 12)
parcela1 = (casa / (anos * 12))*0.1
parcela2= (casa / (anos * 12))*0.1 + parcela
print('-='*11)
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos))

print('''- O total de parcelas será de {}
- O valor da prestação sem juros será de R${:.2f}
- O valor da prestação com juros será de R${:.2f} (Com R${:.2f} de juros adicional)'''.format(anos*12, parcela, parcela2, parcela1))

if parcela <= minimo:
    print('-='*11)
    print('Empréstimo LIBERADO!')
else:
    print('-='*11)
    print('Empréstimo NEGADO!')