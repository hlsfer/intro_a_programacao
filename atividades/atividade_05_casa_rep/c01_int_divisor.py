#Faça um programa que leia um número inteiro e mostre todos os divisores desse número.

from funcoes import is_int

num = is_int("Digite um número inteiro: ")

for i in range(1, num+1):
    if num%i == 0:
        print(i)