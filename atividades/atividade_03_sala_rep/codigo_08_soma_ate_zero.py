#8.Faça um programa que peça números ao usuário e continue repetindo até que ele digite 0. 
#No final, mostre a soma de todos os números digitados.

from funcoes import is_number

pass_end = 0
f_value = 0

while True:
    passw = is_number("Digite 0 para encerrar o programa e dar a soma final. \nDigite um número: ")
    if pass_end == passw:
        break
    else:
        f_value = passw + f_value
        
print(f"Soma final: {f_value}")