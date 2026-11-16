#Faça um programa que leia um número e informe se ele é par ou ímpar.

from funcoes import is_int

numero = is_int("Digite um número inteiro para descobrir se ele é par ou impar: ")

if numero%2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")