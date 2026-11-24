#Leia uma lista com 10 números inteiros. Depois, peça ao usuário um número e informe quantas vezes esse número aparece na lista. O programa não deve usar o método count().

from funcoes import is_int

n = []
count = 0

for i in range(10):
    n.append(is_int("Digite um número inteiro: "))
    
comparador = is_int("Digite um número inteiro para comparar com a lista: ")

for i in n:
    if comparador == i:
        count += 1

print(f"O número {comparador} se repete {count} vezes na lista.")