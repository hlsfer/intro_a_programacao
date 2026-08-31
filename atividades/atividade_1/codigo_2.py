#2. Faça um programa que solicite três números inteiros e mostre a soma total entre eles.
print("Insira três números inteiros para calcular a soma total entre eles.")
while True:
    num1 = input("Digite o primeiro número: ")
    try:
        num1 = int(num1)
        break
    except ValueError:
        print("Apenas números inteiros")

while True:
    num2 = input("Digite o segundo número: ")
    try:
        num2 = int(num2)
        break
    except ValueError:
        print("Apenas números inteiros")

while True:
    num3 = input("Digite o terceiro número: ")
    try:
        num3 = int(num3)
        break
    except ValueError:
        print("Apenas números inteiros")

soma = num1 + num2 + num3
print(f"A soma dos três números é: {soma}")