#Faça um programa que leia a quantidade de faltas de um aluno e informe se ele está dentro do limite ou acima do limite, considerando limite de 10 faltas.

from funcoes import is_int

while True:
    faltas = is_int("Digite a quantidade de faltas do aluno: ")
    if faltas < 0:
        print("VALOR INVALIDO")
    else:
        break

if faltas > 10:
    print("Aluno reprovado por falta")
else:
    print("Aluno dentro do limite permitido de faltas")