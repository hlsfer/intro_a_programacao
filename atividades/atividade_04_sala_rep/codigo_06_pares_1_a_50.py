#Faça um programa que mostre todos os números pares de 1 até 50 usando for.

par = 0

for i in range(1, 51):
    res = (0+i)%2
    if res == 0:
        par+=1
        
print(f"Número total de pares: {par}")