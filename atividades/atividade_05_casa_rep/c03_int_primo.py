#Faça um programa que leia um número inteiro e informe se ele é primo ou não.

from funcoes import is_int

num = is_int("Digite um número inteiro: ")
n = 0

for i in range(1, num+1):
    if num%i == 0:
        n+=1

if n == 2:
    print(f"{num} é um número primo")
else:
    print(f"{num} NÃO é um número primo")