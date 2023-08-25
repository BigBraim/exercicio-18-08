from datetime import date
from time import sleep
print('')
print('-='*15)
print('     ALISTAMENTO MILITAR')
print('-='*15)
print('by: Brayan')
print('')
sleep(2)

hoje = date.today().year
nasc = int(input('Digite APENAS seu ano de nascimento: '))
idade = hoje - nasc

print('')
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, hoje))

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    print('Ainda falta {} ano(s) para o alistamento'.format(18 - idade))
    print('Seu alistamento será em {}.'.format(hoje + (18 - idade)))
elif idade > 18:
    print('Você já deveria ter se alistado há {} ano(s)'.format(idade - 18))
    print('Seu alistamento foi em {}.'.format(hoje - (idade - 18)))
