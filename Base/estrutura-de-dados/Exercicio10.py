# Um instituto de meteorologia deseja fazer um estudo de temperatura média de cada mês do ano.
# Para isso, você precisa fazer um código que colete e armazene essas temperaturas médias em uma lista.
# Depois, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual e
# em que mês elas ocorreram, mostrando os meses por extenso (Janeiro, Fevereiro, etc.).

temperatura_anual = {
    'Nomes': ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
              'Novembro', 'Dezembro'],
    'Media': []
}
meses_acima_media = {
    'Nomes': [],
    'Media': []

}

for i in range(12):
    temperatura_anual['Media'].append(int(input(f'Digite a média de temperatura do mês {i + 1}: ')))

media_anual = round(sum(temperatura_anual['Media'])/len(temperatura_anual['Media']), 2)

for i in range(12):
    if temperatura_anual['Media'][i] > media_anual:
        meses_acima_media['Nomes'].append(temperatura_anual['Nomes'][i])
        meses_acima_media['Media'].append(temperatura_anual['Media'][i])

print('---------------------------------------------')
print(f'Meses com a temperatura acima da média anual: {media_anual}°C')
for i in range(len(meses_acima_media['Media'])):
    print(f'{meses_acima_media['Nomes'][i]}: {meses_acima_media['Media'][i]}°C')
print('---------------------------------------------')