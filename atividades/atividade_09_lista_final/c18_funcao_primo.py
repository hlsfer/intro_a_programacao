#Crie uma função chamada eh_primo(numero) que retorne True se o número for primo e False caso contrário. Depois, leia 10 números e mostre apenas os números primos digitados.

from funcoes import is_int

def eh_primo(numero) -> bool:
    n = 0
    for i in range(1, numero+1):
        if numero%i == 0:
            n+=1
    if n == 2:
        return True
    else:
        return False
    
primos = []

for i in range(10):
    num = is_int("Digite um número inteiro: ")
    if eh_primo(num) and num not in primos:
        primos.append(num)
        
print(f"Números primos: {primos}")