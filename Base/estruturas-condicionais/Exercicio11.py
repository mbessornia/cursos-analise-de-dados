l1 = float(input(f'Informe o primeiro lado do triângulo: ')) 
l2 = float(input(f'Informe o segundo lado do triângulo: ')) 
l3 = float(input(f'Informe o terceiro lado do triângulo: '))


if (l1 + l2) < l3:
    print('Não é possível formar um triângulo.')
elif (l2 + l3) < l1:
    print('Não é possível formar um triângulo.')
elif (l1 + l3) < l2:
    print('Não é possível formar um triângulo.')
else:
    if l1 == l2 == l3:
        print('É possível formar um triângulo equilátero!')
    elif l1 == l2 or l2 == l3 or l1 == l3:
        print('É possível formar um triângulo Isósceles!')
    elif l1 != l2 != l3:
        print('É possível formar um triângulo Escaleno!')

