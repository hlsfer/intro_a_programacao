#Faça um programa que leia o nome e a nota de 5 alunos. Os nomes devem ser armazenados em uma lista e as notas em outra lista. Depois, o programa deve mostrar: Nome do aluno; Nota; Situação: Aprovado ou Reprovado. Considere aprovado quem tiver nota maior ou igual a 7.

from funcoes import is_number

nome = []
nota = []

for i in range(1, 6):
    nome.append(input(f"Digite o nome do aluno {i}: "))
    while True:
        valor_nota = is_number(f"Digite a nota do aluno {i}: ")
        if valor_nota > 10:
            print("Nota máxima: 10. Valores acima do máximo não permitidos.")
        elif valor_nota < 0:
            print("Nota mínima: 0. Valores negativos não permitidos.")
        else:
            nota.append(valor_nota)
            break
    
for i in range(len(nome)):
    print(f"Aluno: {nome[i]}")
    print(f"Nota: {nota[i]}")
    if nota[i] >= 7:
        print("Aprovado\n")
    else:
        print("Reprovado\n")