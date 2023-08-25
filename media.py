from time import sleep
print('')
print('-='*23)
print('     SEJA BEM VINDO AO SISTEMA DE MÉDIA')
print('-='*23)
print('by: Brayan')
print('')
sleep(2)

n1 = float(input("Nota do 1º Bimestre: "))
n2 = float(input("Nota do 2º Bimestre: "))
n3 = float(input("Nota do 3º Bimestre: "))
n4 = float(input("Nota do 4º Bimestre: "))

media = (n1 + n2 + n3 + n4)/4

if media > 7.5:
    print("Aprovado =D sua média é: {:.1f}".format(media))

elif 6 <= media <= 7.5:
     print("Você está de recuperação!! Tire uma média maior que 7.5 para passar de ano. Sua média é: {:.1f}".format(media))

else:
     print("Reprovado!! sua média é: {:.1f}".format(media))