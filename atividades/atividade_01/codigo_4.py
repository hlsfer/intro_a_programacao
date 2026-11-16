#4. Crie um programa que peça ao usuário a quantidade de quilômetros percorridos e a quantidade de litros de combustível gastos, 
# e depois mostre o consumo médio do veículo.

km = float(input("Quantidade de quilômetros percorridos: "))
litros = float(input("Quantidade de combustível gasto: "))
consumo = km / litros
print(f"O consumo médio do veículo é: {consumo:.2f} km/l")