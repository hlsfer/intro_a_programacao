#Faça um programa que leia três notas de um aluno, calcule a média e mostre o resultado na tela.

from funcoes import is_number

while True:
    n1 = is_number("Digite a primeira nota (máximo 10): ")
    if n1 > 10:
        print("Valor acima do máximo permitido")
    elif n1 < 0:
        print("Valores negativos não aceitos")
    else: 
        break

while True:
    n2 = is_number("Digite a segunda nota (máximo 10): ")
    if n2 > 10:
        print("Valor acima do máximo permitido")
    elif n2 < 0:
        print("Valores negativos não aceitos")
    else: 
        break

while True:
    n3 = is_number("Digite a segunda nota (máximo 10): ")
    if n3 > 10:
        print("Valor acima do máximo permitido")
    elif n3 < 0:
        print("Valores negativos não aceitos")
    else: 
        break

media = ((n1+n2+n3)/3)

print(f"Nota 1 = {n1}\nNota 2 = {n2}\nNota 3 = {n3}\nMédia = {media:.2f}")