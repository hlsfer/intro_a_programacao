#Faça um programa que leia 10 números e armazene em uma lista. Depois, mostre:
#Quantidade de positivos
#Quantidade de negativos
#Quantidade de zeros

from funcoes import is_number

n = [is_number("Digite um número: ")]
pos = 0
neg = 0
zero = 0

for i in range(9):
    n.append(is_number("Digite um número: "))
    
for i in n:
    if i > 0:
        pos+=1
    if i < 0:
        neg+=1
    if i == 0:
        zero+=1    
        
print(f"Total de números positivos: {pos}\nTotal de números negativos: {neg}\nTotal de zeros (nulos): {zero}")