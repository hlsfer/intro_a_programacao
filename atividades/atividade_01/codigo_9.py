#9. Elabore um programa que peça ao usuário uma temperatura em graus Celsius e mostre o valor correspondente em Fahrenheit.

temp_c = float(input("Digite a temperatura em graus Celsius: "))
temp_f = (temp_c * 1.8) + 32
print(f"A temperatura em Fahrenheit é: {temp_f:.2f} °F")