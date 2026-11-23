#Faça um programa que leia 8 números e armazene em uma lista. Depois, informe se existem números repetidos na lista.

from funcoes import is_number

n = [is_number("Digite um número: ")]
dup = []
rep = False

for i in range(7):
    n.append(is_number("Digite um número: "))
    
for i in n:
    for j in dup:
        if i == j:
            rep = True
    dup.append(i)
    
if rep == True:
    print("Há números repetidos nessa lista.")
else:
    print("NÃO há números repetidos nessa lista.")