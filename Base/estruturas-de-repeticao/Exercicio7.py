# Os números primos possuem várias aplicações dentro da Ciência de Dados em criptografia e
# segurança, por exemplo. Um número primo é aquele que é divisível apenas por um e por ele mesmo.
# Assim, faça um programa que peça um número inteiro e determine se ele é ou não um número primo.

numero = int(input('Digite um número para verificarmos se ele é um número primo: '))

eh_primo = True

if numero <= 1:
    eh_primo = False
else:
    for i in range(2, numero):
        if numero % i == 0:
            eh_primo = False
        break

if eh_primo:
    print(f'O número {numero} é um número primo.')
else:
    print(f'O número {numero} não é um número primo')
