#7.Faça um programa que peça 5 números ao usuário e no final mostre a média deles.

from funcoes import is_number

n = 1
num_f = 0

while n <= 5:
    num = is_number("Digite uma nota: ")
    num_f = num + num_f
    n += 1

media = (num_f / n)

print(f"Seu número final é: {media}")