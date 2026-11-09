#Faça um programa que conte quantos números entre 1 e 100 são múltiplos de 3. No final, mostre a quantidade encontrada.

n = 0

for i in range(1, 101):
    if i % 3 == 0:
        n+=1
        
print(f"Total de números múltiplos de 3 entre 1 e 100: {n}")