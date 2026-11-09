#Faça um programa que mostre todos os números de 1 até 200 que são divisíveis por 5. Use for e if.

n = 0

for i in range(1, 201):
    if i % 5 == 0:
        n+=1
        print(i)
    