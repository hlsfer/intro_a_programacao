#Faça um programa que leia 10 números inteiros e mostre a soma apenas dos números positivos.

from funcoes import is_int

n = 0

for i in range(10):
    num = is_int("Digite um número inteiro: ")
    if num > 0:
        n = n + num

print(f"Soma dos números inteiros positivos: {n}")