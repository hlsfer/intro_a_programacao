#Leia o salário de 10 funcionários e armazene em uma lista. Crie uma função que receba essa lista e retorne o maior salário, o menor salário, a média salarial e a quantidade de funcionários que recebem acima da média.

from funcoes import is_number

def salario(sal: list[float]) -> tuple[float, float, float, int]:
    maior = sal[0]
    menor = sal[0]
    media = sum(sal)/len(sal)
    a_media = 0
    
    for i in sal:
        if i > maior:
            maior = i
        elif i < menor:
            menor = i
        if i > media:
            a_media += 1

    return maior, menor, media, a_media

sal = []

for i in range(10):
    while True:
        sal_temp = is_number(f"Digite o salário do funcionário {i + 1}: ")
        if sal_temp < 0:
            print("Salário pode ser apenas números positivos.")
        else:
            break
    sal.append(sal_temp)
    
a, b, c, d = salario(sal)

print(f"O maior salário é: {a}\nO menor salário é: {b}\nA média salarial é: {c}\n{d} funcionários possuem salários acima da média.")