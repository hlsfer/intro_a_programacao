#Faça um programa que leia 10 números e armazene em uma lista. Depois, calcule separadamente:
#Soma dos pares
#Soma dos ímpares

from funcoes import is_int

n = [is_int("Digite um número: ")]
par = []
impar = []
soma_p = 0
soma_i = 0

for i in range(9):
    n.append(is_int("Digite um número: "))
    
for i in n:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)
        
for i in par:
    soma_p += i
    
for i in impar:
    soma_i += i
    
print(f"Soma dos pares: {soma_p}")
print(f"Soma dos ímpares: {soma_i}")

