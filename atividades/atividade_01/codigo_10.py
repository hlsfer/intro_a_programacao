#10. Crie um programa que peça o nome do aluno e três notas, calcule a média final e mostre uma mensagem com o nome do aluno e sua média.

nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3
print(f"Aluno: {nome}\nMédia final: {media:.2f}.")