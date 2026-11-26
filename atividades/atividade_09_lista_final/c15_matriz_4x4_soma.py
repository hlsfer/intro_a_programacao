#Leia uma matriz 4x4 e mostre a soma de cada linha. Exemplo de saída: Linha 1: soma = 20; Linha 2: soma = 15; Linha 3: soma = 30; Linha 4: soma = 18.

from funcoes import is_number

matriz = []
soma_linha = []

for i in range(4):
    linha = []
    soma_temp = 0
    for j in range(4):
        num = is_number("Digite um número: ")
        linha.append(num)
        soma_temp += num
    matriz.append(linha)
    soma_linha.append(soma_temp)
    
print("Matriz completa:")    
for i in matriz:
    print(i)
    
for i in range(len(soma_linha)):
    print(f"A soma da linha {i + 1} é {soma_linha[i]} ")