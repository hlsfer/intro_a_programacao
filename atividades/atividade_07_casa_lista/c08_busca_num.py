#Faça um programa que leia 10 números e armazene em uma lista. Depois, peça ao usuário um número para pesquisar. O programa deve informar quantas vezes esse número aparece na lista.

from funcoes import is_number

n = [is_number("Digite um número: ")]
count = 0

for i in range(9):
    n.append(is_number("Digite um número: "))
    
num = is_number("Digite um número para ser testado: ")    

for i in n:
    if i == num:
        count+=1
    
print(f"O número {num} aparece {count} vezes nessa lista.")