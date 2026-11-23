#Encontre o maior valor de um vetor

from funcoes import is_number

n = [is_number("Digite um número: ")]
atual = n[0]

for i in range(4):
    n.append(is_number("Digite um número: "))
    
for i in n:
    if i > atual:
        atual = i

print(atual)