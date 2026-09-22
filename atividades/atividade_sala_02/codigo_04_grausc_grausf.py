#Faça um programa que receba uma temperatura em graus Celsius e converta para Fahrenheit. 
# Utilize a fórmula F = (C × 9 / 5) + 32.

from funcoes import is_number

temp_c = is_number("Digite a temperatura em graus Celsius: ")
temp_f = (temp_c * 1.8) + 32
print(f"A temperatura em Fahrenheit é: {temp_f:.2f} °F")