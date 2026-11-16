#Faça um programa que solicite o nome, a idade e a cidade do usuário. Ao final, apresente uma mensagem exibindo todas as informações 
# digitadas.

from funcoes import is_int

nome = input("Digite o seu nome: ")
idade = is_int("Digite a sua idade: ")
cid = input("Digite a sua cidade: ")

print(f"Seu nome é: {nome}\nSua idade é: {idade}\nSua cidade é: {cid}")