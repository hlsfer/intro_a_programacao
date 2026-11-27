#Uma loja possui 5 vendedores e registra as vendas de cada vendedor durante 4 dias. Crie uma matriz 5x4. Depois, mostre o total vendido por cada vendedor, o total vendido por dia, o vendedor que mais vendeu e o dia com maior venda total.

from funcoes import is_number

matriz_vendedor = []

for i in range(5):
    linha = []
    for j in range(4):
        linha.append(j)
    matriz_vendedor.append(linha)

for i in range(len(matriz_vendedor)):
    for j in range(4):
        valor_diario = is_number(f"Vendedor {i+1}------Digite quanto você vendeu no dia {j+1}: ")
        matriz_vendedor[i][j] = valor_diario
    
cada_vendedor = []

for i in range(len(matriz_vendedor)):
    soma_vendedor = sum(matriz_vendedor[i])
    cada_vendedor.append(soma_vendedor)
    
print("Quanto cada vendedor vendeu: ", cada_vendedor)
    
por_dia = []    

for i in range(len(matriz_vendedor)-1):
    val = 0
    for j in range(len(matriz_vendedor)):
        val += matriz_vendedor[j][i]
    por_dia.append(val)
        
print("Valor das vendas por dia: ", por_dia)

melhor_vendedor = 0
maior_venda = cada_vendedor[0]

for i in range(len(cada_vendedor)):
    if cada_vendedor[i] > maior_venda:
        maior_venda = cada_vendedor[i]
        melhor_vendedor = i
        
print("Melhor vendedor: ", melhor_vendedor + 1)

melhor_dia = por_dia[0]
melhor_dia_indice = 0

for i in range(len(por_dia)):
    if por_dia[i] > melhor_dia:
        melhor_dia = por_dia[i]
        melhor_dia_indice = i
        
print("Melhor dia de vendas: ", melhor_dia_indice + 1)