#Crie uma função chamada situacao_aluno(media) que receba a média de um aluno e retorne sua situação. A função deve retornar “Aprovado”, se a média for maior ou igual a 7; “Recuperação”, se a média for maior ou igual a 5 e menor que 7; e “Reprovado”, se a média for menor que 5. O programa deve ler o nome e a média de 8 alunos e exibir um relatório final.

from funcoes import is_number

def situacao_aluno(media: list[float]) -> str:
    if media >= 7:
        return "Aprovado"
    elif media < 7 and media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"
    
nome = []
nota_media = []

for i in range(1, 9):
    nome.append(input(f"Digite o nome do aluno {i}: "))
    while True:
        nota_media_temp = is_number(f"Digite a média do aluno {i}: ")
        if nota_media_temp > 10 or nota_media_temp < 0:
            print("Apenas valores entre 0 e 10.")
        else:
            break 
    nota_media.append(nota_media_temp)

for i in range(len(nome)):
    print(f"Aluno: {nome[i]}")
    print(f"Média: {nota_media[i]}")
    print(f"Situação: {situacao_aluno(nota_media[i])}\n")