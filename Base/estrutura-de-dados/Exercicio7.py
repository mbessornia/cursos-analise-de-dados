# Para um estudo envolvendo o nível de multiplicação de bactérias em uma colônia, foi coletado
# o número de bactérias por dia (em milhares) e pode ser observado a seguir:
# [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]. Tendo esses valores, faça um código
# que gere uma lista contendo o percentual de crescimento de bactérias por dia, comparando o número
# de bactérias em cada dia com o número de bactérias do dia anterior.
# Dica: para calcular o percentual de crescimento usamos a seguinte equação:
# 100 * (amostra_atual - amostra_passada) / (amostra_passada).

cresc_bac = {
    'Dias': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Quantidade': [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9],
    'Percentual': [0]
}

for i in range(1, len(cresc_bac['Quantidade'])):
    qtd_atual = cresc_bac['Quantidade'][i]
    qtd_anterior = cresc_bac['Quantidade'][i - 1]

    diferenca = qtd_atual - qtd_anterior
    percentual = (100 * diferenca) / qtd_anterior

    cresc_bac['Percentual'].append(round(percentual, 2))

for i in range(len(cresc_bac['Dias'])):
    print(f'Dia {cresc_bac['Dias'][i]}: {cresc_bac['Percentual'][i]}% de crescimento em relação ao dia anterior!')
