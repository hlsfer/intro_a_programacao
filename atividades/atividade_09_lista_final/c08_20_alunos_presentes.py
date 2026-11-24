#Leia o nome de 20 alunos presentes em uma aula. Depois, permita que o usuário pesquise o nome de um aluno. O programa deve informar se o aluno está presente ou ausente.

n = []

for i in range(20):
    n.append(input(f"Digite o nome do aluno {i+1}: "))
    
nome = input("Digite o nome do aluno que você quer pesquisar: ")

for i in n:
    if i == nome:
        print("Aluno presente")
        break
    else:
        print("Aluno ausente")
        break