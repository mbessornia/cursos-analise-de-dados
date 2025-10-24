# Desenvolva um programa que informa a nota de um(a) aluno(a) de acordo com suas respostas.
# Ele deve pedir a resposta desse(a) aluno(a) para cada questão e é preciso verificar se a resposta
# foi igual ao gabarito. Cada questão vale um ponto e existem as alternativas A, B, C ou D.


lista_gabarito = ['D', 'A', 'C', 'B', 'A', 'D', 'C', 'C', 'A', 'B']
lista_resposta = []
nota = 0

for i in range(0, 10):
    resposta = str(input(f'Digite a resposta da questão {i+1}: ').upper())
    while resposta not in ['A', 'B', 'C', 'D']:
        resposta = str(input(f'Alternativa inválida. Digite apenas A, B, C ou D: ').upper())
    lista_resposta.append(resposta)

for i in range(0, 10):
    if lista_resposta[i] == lista_gabarito[i]:
        nota += 1

print(f'Nota: {nota}')