#Faça um programa que solicite a idade de uma pessoa e informe sua classificação de acordo com a faixa etária. Pessoas com até 12 anos serão classificadas como crianças, de 13 até 17 anos como adolescentes, de 18 até 59 anos como adultos e pessoas com 60 anos ou mais como idosos.

from funcoes import is_int

idade = is_int("Digite a sua idade: ")
if idade >= 60:
    print("Idoso")
elif idade >= 18 and idade < 60:
    print("Adulto")
elif idade >= 13 and idade < 18:
    print("Adolescente")
else:
    print("Criança")