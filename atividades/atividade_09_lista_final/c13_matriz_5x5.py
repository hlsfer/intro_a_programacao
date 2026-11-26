#Leia uma matriz 5x5 de números inteiros. Mostre o maior valor encontrado, a linha em que ele está e a coluna em que ele está. Caso o maior valor apareça mais de uma vez, mostre a primeira posição encontrada.

from funcoes import is_number

matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        num_temp = is_number("Digite um número: ")
        linha.append(num_temp)
    matriz.append(linha)

for i in matriz:    
    print(i)

maior = matriz[0][0]
pos = [0][0]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
            pos = [i, j]

            
print(f"O maior valor na matriz é: {maior}")
print(f"A posição do maior número na matriz é: linha {pos[0]+1} e coluna {pos[1]+1}")