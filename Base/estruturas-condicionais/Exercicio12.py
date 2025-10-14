tipo_combustivel = str.lower(input('Escolha o combustível que será abastecido:\nE - Etanol\nD - Diesel\n')) 
qtd = float(input('Digite a quantidade em litros a ser abastecido: '))
valor_desconto = 0
preco_total = 0

if tipo_combustivel == 'E':
    if qtd <= 15:
        valor_desconto = qtd * 1.70 * 0.02
        preco_total = (qtd * 1.70) - valor_desconto
        print(f'O valor total da compra é de R$ {preco_total}')
    else:
        valor_desconto = qtd * 1.70 * 0.04
        preco_total = (qtd * 1.70) - valor_desconto
        print(f'O valor total da compra é de R$ {preco_total}')

elif tipo_combustivel == 'D':
    if qtd <= 15:
        valor_desconto = qtd * 2 * 0.03
        preco_total = (qtd * 2) - valor_desconto
        print(f'O valor total da compra é de R$ {preco_total}')
    else:
        valor_desconto = qtd * 2 * 0.05
        preco_total = (qtd * 2) - valor_desconto
        print(f'O valor total da compra é de R$ {preco_total}')
else:
    print('Digite um combustível válido!')
