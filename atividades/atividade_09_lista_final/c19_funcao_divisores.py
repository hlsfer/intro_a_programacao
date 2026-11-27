#Crie uma função chamada quantidade_divisores(numero) que receba um número inteiro positivo e retorne quantos divisores ele possui. Exemplo: o número 6 possui os divisores 1, 2, 3 e 6. Portanto, a resposta é 4.

from funcoes import is_int

def quantidade_divisores(numero):
    qnt = 0
    for i in range(1, numero+1):
        if numero%i == 0:
            qnt += 1
    return qnt

while True:
    n = is_int("Digite um número inteiro: ")
    if n <= 0:
        print("Apenas números inteiros positivos.")
    else:
        break

div = []

for i in range(1, n+1):
    if n%i == 0:
        div.append(i)
        
print(f"O número {n} possui {quantidade_divisores(n)} divisor(es), sendo ele(s): {div}")