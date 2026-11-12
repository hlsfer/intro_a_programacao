#Faça um programa que leia 10 números inteiros e calcule a média apenas dos números maiores que zero. Caso nenhum número positivo seja digitado, mostre uma mensagem informando que não foi possível calcular a média.

from funcoes import is_int

total = 0

for i in range(10):
    num = is_int("Digite um número inteiro: ")
    if num > 0:
        total += num

if total <= 0:
    print("Nenhum número positivo digitado. Impossível calcular a média.")
else:
    total = total/10
    print(f"Média final: {total}")