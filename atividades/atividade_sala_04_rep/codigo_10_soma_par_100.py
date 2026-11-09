#Faça um programa que calcule e mostre a soma de todos os números pares de 1 até 100 usando for e if.

num = 0
par = 0

for i in range(1, 101):
    res = (0+i)%2
    if res == 0:
            num = num + i
        
print(f"Número total de pares: {par}")
print(num)