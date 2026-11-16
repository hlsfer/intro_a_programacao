#5.Faça um programa que peça ao usuário um número maior que zero. Caso ele digite um valor inválido, o programa deve continuar pedindo 
#até que ele digite um número válido.


from funcoes import is_number

while True:
    num = is_number("Digite um número maior que zero: ")
    if num <= 0:
        print("VALOR INVALIDO")
    else:
        print("Valor aceito!")
        break