#Faça um programa que leia 10 números inteiros e mostre quantos são pares e quantos são ímpares.

from funcoes import is_int

par = 0
impar = 0

for i in range(10):
    num = is_int("Digite um número inteiro: ")
    if num%2 == 0:
        par+=1
    else:
        impar+=1

print(f"Número de pares:{par}\nNúmero de ímpares: {impar}")