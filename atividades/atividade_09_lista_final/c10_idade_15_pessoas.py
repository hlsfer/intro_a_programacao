#Leia a idade de 15 pessoas e armazene em uma lista. Depois, mostre a quantidade de menores de idade, a quantidade de adultos, a quantidade de idosos, a média das idades, a maior idade e a menor idade. Considere menor de idade quem tem menos de 18 anos, adulto quem tem de 18 até 59 anos e idoso quem tem 60 anos ou mais.

from funcoes import is_int

idade_geral = []
idade_menor = []
idade_adulto = []
idade_idoso = []
valor_maior = 0
valor_menor = 0

for i in range(15):
    while True:
        idade_temp = is_int(f"Digite a idade da pessoa {i+1}: ")
        if idade_temp < 0:
            print("Valor digitado não pode ser menor que 0.")
        else:
            break        
    if idade_temp >= 60:
        idade_idoso.append(idade_temp)
    elif idade_temp < 18:
        idade_menor.append(idade_temp)
        valor_menor = idade_temp
    else:
        idade_adulto.append(idade_temp)
    idade_geral.append(idade_temp)
    
for i in idade_geral:
    if i > valor_maior:
        valor_maior = i
    if i < valor_menor:
        valor_menor = i
    
print(f"Média das idades: {sum(idade_geral)/len(idade_geral)}")
print(f"Quantidade de menores de idade: {len(idade_menor)}")
print(f"Quantidade de adultos: {len(idade_adulto)}")
print(f"Quantidade de idosos: {len(idade_idoso)}")
print(f"Maior idade: {valor_maior}")
print(f"Menor idade: {valor_menor}")