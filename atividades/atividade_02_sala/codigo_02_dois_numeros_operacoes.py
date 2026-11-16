#Faça um programa que leia dois números informados pelo usuário e apresente a soma, a subtração, a multiplicação e a divisão entre eles.

from funcoes import is_number

n1 = is_number("Digite o primeiro número: ")
n2 = is_number("Digite o segundo número: ")

soma = (n1+n2)
sub = (n1-n2)
mult = (n1*n2)
divi = (n1/n2)

print(f"Soma = {soma}\nSubtração = {sub}\nMultiplicação = {mult}\nDivisão = {divi}")