#Faça um programa que leia a idade de uma pessoa e informe se ela pode entrar no evento, considerando entrada permitida apenas para maiores de 18 anos.

from funcoes import is_int

idade = is_int("Digite a sua idade: ")

if idade >= 18:
    print("Entrada permitida")
else:
    print("Entrada proibida. Evento destinado a maiores de 18 anos")