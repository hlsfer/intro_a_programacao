#Faça um programa que leia 8 números e armazene em uma lista. Depois, crie uma nova lista contendo apenas os números maiores que 10.

from funcoes import is_number

n = [is_number("Digite um número: ")]
maior_10 = []

for i in range(7):
    n.append(is_number("Digite um número: "))    

for i in n:
    if i > 10:
        maior_10.append(i)    
    
print(f"Lista de números maiores que 10: {maior_10}")