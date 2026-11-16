#Faça um programa que leia o nome de um aluno e sua nota, informando se ele foi aprovado ou reprovado.

from funcoes import is_number

nome = input("Digite o nome do aluno: ")

while True:
    nota = is_number("Digite a nota do aluno (máximo 10): ")
    if nota > 10:
        print("Valor acima do máximo permitido")
    else:
        break

if nota >= 7:
    print(f"Aluno {nome} aprovado.")
else:
    print(f"Aluno {nome} reprovado")