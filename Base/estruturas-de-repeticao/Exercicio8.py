# 8) Vamos entender a distribuição de idades de pensionistas de uma empresa de previdência.
# Escreva um programa que leia as idades de uma quantidade não informada de clientes e mostre a
# distribuição em intervalos de [0-25], [26-50], [51-75] e [76-100]. Encerre a entrada de dados
# com um número negativo.

# categoria 1: [0-25]
categoria1 = 0
# categoria 2: [26-50]
categoria2 = 0
# categoria 3: [51-75]
categoria3 = 0
# categoria 4: [76-100]
categoria4 = 0

idade = int(input('Digite sua idade (ou um número negativo para encerrar): '))

while idade > 0:
    if idade >= 0 and idade < 26:
        categoria1 += 1
    elif idade > 25 and idade < 51:
        categoria2 += 1
    elif idade > 50 and idade < 76:
        categoria3 += 1
    else:
        categoria4 += 1

    idade = int(input('Digite sua idade (ou um número negativo para encerrar): '))

print(f'Pensionistas de 0-25 anos: {categoria1}\nPensionistas de 26-50 anos: {categoria2}'
      f'\nPensionistas de 51-75 anos: {categoria3}\nPensionistas de 76-100 anos: {categoria4}')
