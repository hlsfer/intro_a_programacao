#6.Faça um programa que peça 5 números ao usuário e no final mostre a soma de todos eles.

from funcoes import is_number

n = 1
num_f = 0

while n <= 5:
    num = is_number("Digite um valor: ")
    num_f = num + num_f
    n += 1

print(f"Seu número final é: {num_f}")