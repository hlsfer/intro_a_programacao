#Uma loja possui 12 produtos. Para cada produto, leia o nome e a quantidade em estoque. Depois, mostre os produtos com estoque menor que 5, o produto com maior estoque, o produto com menor estoque e a quantidade total de itens no estoque.

from funcoes import is_int

matriz_estq = []
    
for j in range(1, 13):
    nome_temp = input(f"Digite o nome do produto {j}: ")
    qnt_temp = is_int(f"Digite a quantidade do produto {j} no estoque: ")
    matriz_estq.append([nome_temp, qnt_temp])

nome_menor_estq = matriz_estq[0][0]
num_menor_estq = matriz_estq[0][1]
nome_maior_estq = matriz_estq[0][0]
num_maior_estq = matriz_estq[0][1]
total_itens = 0

for i in matriz_estq:
    nome = i[0]
    num = i[1]
    if num < 5:
        print(f"Produto: {nome} está com estoque abaixo de 5.")
    if num > num_maior_estq:
        num_maior_estq = num
        nome_maior_estq = nome
    if num < num_menor_estq:
        num_menor_estq = num
        nome_menor_estq = nome     
    total_itens += num

print(f"Produto com MAIOR estoque: {nome_maior_estq}")
print(f"Produto com MENOR número no estoque: {nome_menor_estq}")
print(f"Número total de itens no estoque: {total_itens}")