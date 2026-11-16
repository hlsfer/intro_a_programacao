#Faça um programa que leia a temperatura e informe se está quente ou frio, considerando quente quando for maior que 30 graus.

from funcoes import is_number

temp = is_number("Digite a temperatura em graus Celsius: ")
if temp > 30:
    print("Está quente.")
else:
    print("Está frio.")