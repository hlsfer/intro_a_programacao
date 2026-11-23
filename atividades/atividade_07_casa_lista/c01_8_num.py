#Faça um programa que leia 8 números e armazene em uma lista. Depois, mostre o maior número digitado e a posição em que ele aparece na lista.

from funcoes import is_number

n = [is_number("Digite um número: ")]
maior = n[0]
i_maior = 0

for i in range(7):
    n.append(is_number("Digite um número: "))
    
for i in n:
    if i > maior:
        maior = i

for i in range(1, len(n)):
    if n[i] > n[i_maior]:
        i_maior = i

print(f"O maior valor da lista é: {maior}")
print(f"O maior valor está na posição {i_maior} na lista (considerando o range de 0 a {len(n)-1})")