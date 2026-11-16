from funcoes import is_int

par = 0

n = is_int("Digite um número inteiro: ")

for i in range(1, n+1):
    res = (0+i)%2
    if res == 0:
        par+=1
        
print(f"Número total de pares: {par}")