# Escreva um programa que peça uma data informando o dia, mês e ano e determine se ela
# é válida para uma análise.

dia = int(input('Digite o dia: '))
mes = int(input('Digite o mês: '))
ano = int(input('Digite o ano: '))

if mes == 2:
    if ano % 4 == 0 and (ano % 400 == 0 or ano % 100 != 0):
        dias_fevereiro = 29
    else:
        dias_fevereiro = 28
    if dia >= 1 and dia <= dias_fevereiro:
        print('Data válida')
    else:
        print('Data inválida')
elif mes in [1, 3, 5, 7, 8, 10, 12]:
    if dia >= 1 and dia <= 31:
        print('Data válida')
    else:
        print('Data inválida')
elif mes in [4, 6, 9, 11]:
    if dia >= 1 and dia <= 30:
        print('Data válida')
    else:
        print('Data inválida')
else:
    print('Data inválida')
