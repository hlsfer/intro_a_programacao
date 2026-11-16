#Faça um programa que leia a idade de uma pessoa e informe se ela pode votar, considerando idade mínima de 16 anos.

from funcoes import is_int

idade = is_int("Digite a sua idade: ")
if idade >= 16:
    print("Você pode votar.")
else:
    print("Você não pode votar.")