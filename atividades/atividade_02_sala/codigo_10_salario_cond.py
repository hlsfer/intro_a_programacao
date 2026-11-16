#Faça um programa que receba o salário de um funcionário e a quantidade de anos trabalhados na empresa. Funcionários com menos de 2 anos não recebem bônus. Funcionários com 2 até 5 anos recebem 5% de bônus sobre o salário. Funcionários com mais de 5 anos e salário abaixo de R$ 3.000,00 recebem 10% de bônus. Funcionários com mais de 5 anos e salário igual ou superior a R$ 3.000,00 recebem 15% de bônus. Ao final, o programa deverá mostrar o salário original, o valor do bônus e o salário final.

from funcoes import is_number, is_int

sal = is_number("Digite o seu salário em R$: ")
anos = is_int("Digite a quantidade de anos trabalhados na empresa (números inteiros apenas): ")

if anos >= 2 and anos <= 5:
    inc = 0.05
    inc_val = sal * inc
    sal_1 = sal + inc_val
    print(f"Salário inicial: {sal} R$\nValor do bônus: {inc_val} R$\nSalário final: {sal_1} R$")
elif anos > 5 and sal < 3000:
    inc = 0.1
    inc_val = sal * inc
    sal_1 = sal + inc_val
    print(f"Salário inicial: {sal} R$\nValor do bônus: {inc_val} R$\nSalário final: {sal_1} R$")
elif anos > 5 and sal >= 3000:
    inc = 0.15
    inc_val = sal * inc
    sal_1 = sal + inc_val
    print(f"Salário inicial: {sal} R$\nValor do bônus: {inc_val} R$\nSalário final: {sal_1} R$")
else:
    print("Não se encaixa em nenhuma das categorias")