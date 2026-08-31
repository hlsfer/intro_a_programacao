def is_float(num):
    while True:
        res = input(num)
        try:
            return float(res)
        except ValueError:
            print("Apenas números decimais")

num1 = is_float("Digite o número para mostrar a terça parte: ")
terca_parte = num1 / 3
print(f"A terça parte do número é: {terca_parte}")