#3.Faça um programa que peça ao usuário um número e depois mostre a tabuada desse número de 1 até 10 usando while.


from funcoes import is_number

num = is_number("Digite um número: ")
n = 1

while n <= 10:
    num_f = num*n
    print(num_f) 
    n += 1
    
