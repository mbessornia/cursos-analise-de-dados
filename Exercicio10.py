n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))

op = str.lower(input('Qual operação você deseja?\n\n- Soma\n- Subtração\n- Multiplicação\n- Divisão\n'))

if op == 'soma':
    resultado = n1 + n2
elif op == 'subtração':
    resultado = n1 - n2
elif op == 'multiplicação':
    resultado = n1 * n2
elif op == 'divisão':
    resultado = n1 / n2
else:
    print('Digite uma operação válida')

if resultado % 2 == 0:
    info1 = 'par'
else:
    info1 = 'ímpar'

if resultado % 1 == 0:
    info2 = 'inteiro'
else:
    info2 = 'decimal'

print(f'Resultado: {resultado}, {info2} e {info1}')
