#Faça um programa que leia a temperatura e informe se está quente ou frio, considerando quente quando for maior que 30 graus.

def is_number(num):
    while True:
        res = input(num)
        try:
            return float(res)
        except ValueError:
            print("Apenas números são aceitos.")

temp = is_number("Digite a temperatura em graus Celsius: ")
if temp > 30:
    print("Está quente.")
else:
    print("Está frio.")