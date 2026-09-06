#Faça um programa que leia dois números e informe qual deles é o maior, ou se eles são iguais.

from funcoes import is_number

num1 = is_number("Digite um número: ")
num2 = is_number("Digite um número: ")

if num1 > num2:
    print("O primeiro número é maior que o segundo")
elif num1 < num2:
    print("O primeiro número é menor que o segundo")
else:
    print("Os números são iguais")