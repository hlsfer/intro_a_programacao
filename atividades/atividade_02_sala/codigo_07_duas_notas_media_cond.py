#Faça um programa que leia duas notas de um aluno e calcule sua média. Se a média for maior ou igual a 7, o aluno deverá ser 
#considerado aprovado. Se a média for maior ou igual a 5 e menor que 7, deverá ficar em recuperação. Caso a média seja menor que 5, 
#deverá ser considerado reprovado.

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

media = ((n1+n2)/2)

if media >= 7:
    print(f"Notas: {n1} e {n2}")
    print(f"Média: {media}")
    print("Aprovado")
elif media >= 5 and media < 7:
    print(f"Notas: {n1} e {n2}")
    print(f"Média: {media}")
    print("Recuperação")
else:
    print(f"Notas: {n1} e {n2}")
    print(f"Média: {media}")
    print("Reprovado")