#Leia 15 números inteiros e some apenas os números que sejam pares e maiores que 10. Ao final, mostre a soma dos pares especiais, a quantidade de números somados e a média desses números, caso exista pelo menos um.

from funcoes import is_int

soma = 0
qtd_par = 0

for i in range(5):
    valor_temp = (is_int("Digite um número: "))
    if valor_temp % 2 == 0 and valor_temp > 10:
        soma += valor_temp
        qtd_par += 1
    
if qtd_par > 0:
    print(f"Soma de todos os pares que atendem a condição: {soma}")
    print(f"Quantidade de números que foram somados: {qtd_par}")
    print(f"Média dos números somados: {soma/qtd_par:.2f}")
else:
    print("Nenhum número digitado atende às condições")