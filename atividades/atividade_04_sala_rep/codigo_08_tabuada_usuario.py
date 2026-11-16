#Faça um programa que leia um número inteiro e mostre a tabuada desse número de 1 até 10 usando for.

from funcoes import is_int

num = is_int("Digite um número inteiro: ")

for i in range(1, 11):
    res = num*i
    print(res) 