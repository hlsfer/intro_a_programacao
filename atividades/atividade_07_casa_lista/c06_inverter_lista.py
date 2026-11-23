#Faça um programa que leia 7 números e armazene em uma lista. Depois, crie uma nova lista com os valores na ordem inversa.
#Atenção: não use reverse()

from funcoes import is_number

n = [is_number("Digite um número: ")]
n2 = []

for i in range(6):
    n.append(is_number("Digite um número: "))

for i in range(len(n)-1, -1, -1):
    n2.append(n[i])

print(f"Lista original: {n}")    
print(f"Lista invertida: {n2}")