#Faça um programa que leia a idade de uma pessoa e informe se ela pode votar, considerando idade mínima de 16 anos.

def is_int(num):
    while True:
        res = input(num)
        try:
            return int(res)
        except ValueError:
            print("Apenas números inteiros")

idade = is_int("Digite a sua idade: ")
if idade >= 16:
    print("Você pode votar.")
else:
    print("Você não pode votar.")