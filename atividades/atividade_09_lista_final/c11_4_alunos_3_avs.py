#Uma turma possui 4 alunos e cada aluno realizou 3 avaliações. Crie uma matriz 4x3 para armazenar as notas. Depois, calcule a média de cada aluno e informe sua situação. Considere aprovado quem tiver média maior ou igual a 7.

from funcoes import is_number

matriz_completa = []
matriz_notas = []

for i in range(4):
    linha_nota = []
    nome_temp = input(f"Digite o nome do aluno {i+1}: ")
    for j in range(3):
        while True:
            nota_temp = is_number(f"Digite a nota {j+1} do aluno {i+1}: ")
            if nota_temp < 0 or nota_temp > 10:
                print("Valores de nota devem estar entre 0 e 10.")
            else:    
                linha_nota.append(nota_temp)
                break
    matriz_notas.append(linha_nota)
    matriz_completa.append([nome_temp, linha_nota])

for i in matriz_completa:
    nome = i[0]
    notas = i[1]
    media = sum(notas)/len(notas)
    print(f"Aluno: {nome}")
    print(f"Notas: {notas}")
    if media >= 7:
        print(f"Aprovado com média: {media}\n")
    else:
        print(f"Reprovado com média: {media}\n")