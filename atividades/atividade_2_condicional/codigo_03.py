#Faça um programa que leia o salário de uma pessoa e informe se ela recebe acima de 2000 reais ou 2000 reais ou menos.

from funcoes import is_number

salario = is_number("Digite o seu salário: ")

if salario > 2000:
    print("Você recebe acima de 2000 reais.")
else:
    print("Você recebe menos de 2000 reais.")