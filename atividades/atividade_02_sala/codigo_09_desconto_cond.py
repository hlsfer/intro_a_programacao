#Faça um programa que receba o valor total de uma compra e calcule o desconto de acordo com as seguintes regras: compras abaixo de R$ 100,00 não recebem desconto; compras entre R$ 100,00 e R$ 499,99 recebem 10% de desconto; compras de R$ 500,00 ou mais recebem 15% de desconto. Ao final, o programa deverá mostrar o valor original da compra, o valor do desconto e o valor final a ser pago.

from funcoes import is_number

val = is_number("Digite o valor da sua compra em R$: ")

if val >= 500:
    desc = 0.15
    val_desc = val * desc
    val_1 = (val - val_desc)
    print(f"Valor inicial: {val} R$\nValor final com desconto: {val_1} R$\n Desconto total: {val_desc:.2f} R$")
elif val >= 100 and val < 500:
    desc = 0.10
    val_desc = val * desc
    val_1 = (val - val_desc)
    print(f"Valor inicial: {val} R$\nValor final com desconto: {val_1} R$\n Desconto total: {val_desc} R$")
else:
    print(f"Valor inelegível para desconto: {val} R$")