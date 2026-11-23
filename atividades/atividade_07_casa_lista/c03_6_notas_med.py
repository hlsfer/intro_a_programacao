#Faça um programa que leia 6 notas e armazene em uma lista. Depois, calcule a média da turma e mostre quais notas ficaram acima da média.

from funcoes import is_number

n = [is_number("Digite uma nota: ")]
soma = 0
acima = []

for i in range(5):
    n.append(is_number("Digite uma nota: "))
    
for i in n:
    soma += i
    
media = soma/(len(n))
print(f"Valor médio das notas da turma: {media}")

for i in n:
    if i > media:
        acima.append(i)
        
print(f"Notas acima da média da turma: {acima}")