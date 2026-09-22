#Faça um programa que leia dois números e informe qual deles é o maior. Caso os dois números sejam iguais, o programa deverá 
# informar que possuem o mesmo valor.

from funcoes import is_number

n1 = is_number("Informe o primeiro número: ")
n2 = is_number("Informe o segundo número: ")

if n1>n2:
    print("O primeiro valor é maior")
elif n2>n1:
    print("O segundo valor é maior")
else:
    print("Os valores são iguais")