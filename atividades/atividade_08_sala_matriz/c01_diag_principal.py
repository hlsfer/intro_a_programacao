#print da diagonal principal 3x3

from funcoes import is_number

matriz = []

for i in range(3):
    l = []
    for j in range(3):
        num = is_number("Digite um número: ")
        l.append(num)
    matriz.append(l)

dig = []

for i in range(len(matriz)):
    for j in range(len(matriz)):
        if i == j:
            dig.append(matriz[i][j])

print(f"Diagonal principal da matriz: {dig}")