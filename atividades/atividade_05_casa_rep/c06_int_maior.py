#Faça um programa que leia 8 números inteiros e informe qual foi o maior número digitado.

from funcoes import is_int

n = is_int("Digite um número inteiro: ")

for i in range(7): 
    num = is_int("Digite um número inteiro: ")
    if num > n:
        n = num

print(f"Maior número: {n}")