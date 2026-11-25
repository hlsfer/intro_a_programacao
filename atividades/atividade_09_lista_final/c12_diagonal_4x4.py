#Leia uma matriz 4x4 de números inteiros e calcule a soma dos elementos da diagonal principal. A diagonal principal é formada pelos elementos em que o número da linha é igual ao número da coluna.

from funcoes import is_int

matriz = []

for i in range(4):
    l = []
    for j in range(4):
        n = is_int("Digite um número inteiro: ")
        l.append(n)
    matriz.append(l)

diag = []
    
for i in range(len(matriz)):
    for j in range(len(matriz)):
        if i == j:
            diag.append(matriz[i][j])
            
print(f"Diagonal principal da matriz: {diag}")
print(f"Soma dos valores da diagonal principal da matriz: {sum(diag)}")