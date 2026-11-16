#8. Faça um programa que peça o valor de um produto e o percentual de desconto, calculando quanto o produto passará a custar após o desconto.

valor_produto = float(input("Digite o valor do produto: "))
desconto = float(input("Digite o percentual de desconto: "))
valor_final = valor_produto * (1 - desconto / 100)
print(f"Valor final após o desconto: {valor_final:.2f}")