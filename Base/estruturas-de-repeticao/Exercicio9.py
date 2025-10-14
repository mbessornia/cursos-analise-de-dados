# Em uma eleição para gerência em uma empresa com 20 pessoas colaboradoras, existem quatro candidatos(as).
# Escreva um programa que calcule o(a) vencedor(a) da eleição. A votação ocorreu da seguinte maneira:
#
# Cada colaborador(a) votou em uma das quatro pessoas candidatas (que representamos pelos números 1, 2, 3 e 4).
# Também foram contabilizados os votos nulos (representados pelo número 5) e os votos em branco (representados pelo número 6).
# Ao final da votação, o programa deve exibir o número total de votos para cada candidato(a), os nulos e os votos em branco.
# Além disso, deve calcular e exibir a porcentagem de votos nulos em relação ao total de votos e a porcentagem de votos em branco em relação ao total de votos.

contador_votos = 0
voto_candidato1 = 0
voto_candidato2 = 0
voto_candidato3 = 0
voto_candidato4 = 0
voto_nulo = 0
voto_branco = 0
pct_voto_nulo = 0
pct_voto_branco = 0

while contador_votos < 20:
    print('1 - Candidato 1\n2 - Candidato 2\n3 - Candidato 3\n4 - Candidato 4\n5 - Voto nulo\n6 - Voto branco')
    voto = int(input('\nDigite o número para votar no seu candidato: '))
    if voto == 1:
        voto_candidato1 += 1
        contador_votos += 1
    elif voto == 2:
        voto_candidato2 += 1
        contador_votos += 1
    elif voto == 3:
        voto_candidato3 += 1
        contador_votos += 1
    elif voto == 4:
        voto_candidato4 += 1
        contador_votos += 1
    elif voto == 5:
        voto_nulo += 1
        contador_votos += 1
    elif voto == 6:
        voto_branco += 1
        contador_votos += 1
    else: print('Digite um número válido!')


pct_voto_nulo = (voto_nulo/20) * 100
pct_voto_branco = (voto_branco/20) * 100

if voto_candidato1 > voto_candidato2 and voto_candidato1 > voto_candidato3 and voto_candidato1 > voto_candidato4:
    print(f'O candidato 1 venceu as eleições!\nVotos brancos: {pct_voto_branco:.0f}%\nVotos nulos: {pct_voto_nulo:.0f}%')
elif voto_candidato2 > voto_candidato1 and voto_candidato2 > voto_candidato3 and voto_candidato2 > voto_candidato4:
    print(f'O candidato 2 venceu as eleições!\nVotos brancos: {pct_voto_branco:.0f}%\nVotos nulos: {pct_voto_nulo:.0f}%')
elif voto_candidato3 > voto_candidato1 and voto_candidato3 > voto_candidato2 and voto_candidato3 > voto_candidato4:
    print(f'O candidato 3 venceu as eleições!\nVotos brancos: {pct_voto_branco:.0f}%\nVotos nulos: {pct_voto_nulo:.0f}%')
elif voto_candidato4 > voto_candidato1 and voto_candidato4 > voto_candidato2 and voto_candidato4 > voto_candidato3:
    print(f'O candidato 4 venceu as eleições!\nVotos brancos: {pct_voto_branco:.0f}%\nVotos nulos: {pct_voto_nulo:.0f}%')

