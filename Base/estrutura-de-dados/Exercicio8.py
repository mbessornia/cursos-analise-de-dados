# Para uma seleção de produtos alimentícios, precisamos separar o conjunto de IDs dados por
# números inteiros sabendo que os produtos com ID par são doces e os com ID ímpar são amargos.
# Monte um código que colete 10 IDs. Depois, calcule e mostre a quantidade de produtos doces e amargos.
lista_produtos = []
amargos = 0
doces = 0

for i in range(1, 11):
    lista_produtos.append(int(input('Digite o ID do produto: ')))

for id_produto in lista_produtos:
    if lista_produtos[id_produto] % 2 == 0:
        doces += 1
    else:
        amargos += 1

print(f'Produtos doces: {doces}\nProdutos amargos: {amargos}')