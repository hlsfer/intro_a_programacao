#Leia 10 números inteiros entre 1 e 5 e mostre quantas vezes cada número apareceu. Exemplo de saída: Número 1 apareceu 2 vezes; Número 2 apareceu 0 vezes; Número 3 apareceu 4 vezes; Número 4 apareceu 1 vez; Número 5 apareceu 3 vezes.

from funcoes import is_int

matriz_num = []

for i in range(5):
    linha = []
    z = 0
    linha.append(i+1)
    linha.append(z)
    matriz_num.append(linha)
    
for i in range(10):
    while True:
        num_temp = is_int("Digite um número entre 1 e 5: ")
        if num_temp <= 5 and num_temp >= 1:
            matriz_num[num_temp - 1][1] += 1    
            break
        else:
            print("Apenas números entre 1 e 5 (1, 2, 3, 4 ou 5).")
            
for i in range(len(matriz_num)):
    print(f"O número {matriz_num[i][0]} apareceu {matriz_num[i][1]} vezes")