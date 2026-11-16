#Faça um programa que leia um número inteiro e informe quantos divisores ele possui.

from funcoes import is_int

num = is_int("Digite um número inteiro: ")
n = 0

for i in range(1, num+1):
    if num%i == 0:
        n+=1

print(f"Número de divisores de {num}: {n}")