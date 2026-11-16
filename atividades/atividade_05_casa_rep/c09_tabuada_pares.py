#Faça um programa que leia um número inteiro e mostre a tabuada dele de 1 até 20, exibindo apenas os resultados pares.

from funcoes import is_int

num = is_int("Digite um número: ")

for i in range(1, 21):
    res = num*i
    if res%2 == 0:
        print(res) 