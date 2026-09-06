#Faça um programa que leia um número e informe se ele é maior que 10 ou menor ou igual a 10.

from funcoes import is_number

num = is_number("Informe um número para descobrir se ele é menor, maior ou igual a 10: ")

if num > 10:
    print("Número maior que 10")
elif num < 10:
    print("Número menor que 10")
else:
    print("Número igual a 10")