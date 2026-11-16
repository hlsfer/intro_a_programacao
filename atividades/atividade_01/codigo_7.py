#7. Crie um programa que peça a base e a altura de um triângulo, calcule sua área e mostre o resultado na tela.

base = float(input("Digite a base do triângulo: "))
altura = float(input("Digite a altura do triângulo: "))
area = (base * altura) / 2
print(f"A área do triângulo é: {area:.2f}")