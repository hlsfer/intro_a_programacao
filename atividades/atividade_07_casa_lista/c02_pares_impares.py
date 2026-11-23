#Faça um programa que leia 10 números e armazene em uma lista. Depois, crie duas novas listas: uma contendo os números pares e outra contendo os números ímpares.

from funcoes import is_int

n = [is_int("Digite um número: ")]
par = []
impar = []

for i in range(9):
    n.append(is_int("Digite um número: "))
    
for i in n:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)
        
print(f"Lista dos pares: {par}")
print(f"Lista dos ímpares: {impar}")