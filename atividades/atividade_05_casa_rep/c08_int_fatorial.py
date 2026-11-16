#Faça um programa que leia um número inteiro e calcule o seu fatorial.

from funcoes import is_int

n = 1
num = is_int("Digite um número inteiro positivo: ")

while num < 0:
    print("APENAS NÚMEROS POSITIVOS!")
    num = is_int("Digite um número inteiro POSITIVO: ")

for i in range(2, num + 1):
    n *= i

print(f"Valor de {num} fatorial: {n}")
