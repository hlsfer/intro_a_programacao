#Faça um programa que leia 10 números inteiros e conte quantos deles são positivos, negativos e iguais a zero. No final, mostre a quantidade de positivos, negativos e zeros.

from funcoes import is_int

pos = 0
neg = 0
zero = 0

for y in range(10):
    num = is_int("Digite um número inteiro: ")
    if num > 0:
        pos+=1
    if num < 0:
        neg+=1
    if num == 0:
        zero+=1
        
print(f"Total de números positivos: {pos}\nTotal de números negativos: {neg}\nTotal de zeros (nulos): {zero}")