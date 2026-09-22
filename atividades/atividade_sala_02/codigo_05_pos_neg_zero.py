#Faça um programa que leia um número inteiro e informe se ele é positivo, negativo ou igual a zero.

from funcoes import is_int

num = is_int("Digite um número inteiro: ")
if num > 0:
    print("Valor positivo")
elif num < 0:
    print("Valor negativo")
else:
    print("O valor é zero")
