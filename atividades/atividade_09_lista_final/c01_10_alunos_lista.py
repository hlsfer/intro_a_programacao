#Uma turma possui 10 alunos. Faça um programa que leia as notas dos alunos e armazene em uma lista. Depois, mostre a média da turma, a maior nota, a menor nota, a quantidade de alunos acima da média e a quantidade de alunos abaixo de 5.

from funcoes import is_number

nota = []
nota_maior = 0
nota_menor = 10
qt_acima = 0
qt_abaixo = 0

for i in range(1, 11):
    while True:
        nota_temp = is_number(f"Digite a nota do aluno {i}: ")
        if nota_temp > 10 or nota_temp < 0:
            print("Apenas valores entre 0 e 10.")
        else:
            break 
    nota.append(nota_temp)

for i in nota:
    if nota_maior < i:
        nota_maior = i    
    if nota_menor > i:
        nota_menor = i
        
    if i >= 7:
        qt_acima += 1
    if i < 5:
        qt_abaixo += 1

media = sum(nota)/len(nota)

qt_acima_2 = 0

for i in nota:
    if i >= media:
        qt_acima_2 += 1


print(f"Média da turma: {media:.3f};\nMaior nota: {nota_maior};\nMenor nota: {nota_menor};\nQuantidade de alunos acima da média 7: {qt_acima};\nQuantidade de alunos com nota abaixo de 5: {qt_abaixo};\nQuantidade de alunos acima da média da turma: {qt_acima_2}")