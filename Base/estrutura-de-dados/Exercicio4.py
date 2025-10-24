# Colete novamente 5 inteiros e imprima a lista em ordem inversa à enviada.
lista_numeros = []

for i in range (0, 5):
    numero = int(input('Digite um número:'))
    lista_numeros.append(numero)

lista_numeros.sort(reverse=True)

print(f'Esta é a lista em ordem reversa: {lista_numeros}')