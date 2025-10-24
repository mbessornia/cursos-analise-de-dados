# Faça um programa que, ao inserir um número qualquer, cria uma lista contendo todos os
# números primos entre 1 e o número digitado.

numero = int(input('Digite um número qualquer'))
lista_numeros_primos = [1]

def is_primo(numero):
    cont = 0
    for i in range (2, numero+1):
        if numero % i == 0:
            cont += 1
    return cont == 1


for i in range(1, numero+1):
    if is_primo(i):
        lista_numeros_primos.append(i)

print(lista_numeros_primos)
