#6. Desenvolva um programa que peça a idade de uma pessoa e mostre quantos meses de vida ela possui aproximadamente.

idade = int(input("Digite a sua idade: "))
meses_min = idade * 12
meses_max = meses_min + 11
print(f"Você tem entre {meses_min} e {meses_max} meses de vida.")