#Leia uma matriz 4x5 de números inteiros e descubra qual linha possui a maior soma. Ao final, mostre o número da linha e a soma dessa linha.

from funcoes import is_number

matriz = []
soma_linha = []

for i in range(4):
    linha = []
    soma_temp = 0
    for j in range(5):
        num = is_number("Digite um número: ")
        linha.append(num)
        soma_temp += num
    matriz.append(linha)
    soma_linha.append(soma_temp)
    
print("Matriz completa:")    
for i in matriz:
    print(i)

maior = 0
linha_maior = 0
    
for i in range(len(soma_linha)):
    if soma_linha[i] > maior:
        maior = soma_linha[i]
        linha_maior = i
        
print(f"A linha com maior soma é a linha: {linha_maior + 1}")
print(f"O valor da soma da linha {linha_maior + 1} é: {maior}")