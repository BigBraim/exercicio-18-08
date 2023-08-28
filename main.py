print('')
print ('Escolha entre "Empréstimo", "Conversor", "Alistamento", "Média", e "Pagamento"')
print('')
print ('Empréstimo: 1')
print ('Conversor: 2')
print ('Alistamento: 3')
print ('Média: 4')
print ('Pagamento: 5')
print('')

nome = int(input('Escolha entre 1, 2, 3, 4, e 5: '))

match nome:
    case 1:
        import emprestimo

    case 2:
        import convesor

    case 3:
        import alistamento

    case 4:
        import media

    case 5:
        import pagamento

    case _:
        ValueError
        print('ERRO: Digite apenas NÚMEROS entre 1 e 2! ')