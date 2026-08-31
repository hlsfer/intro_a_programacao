def is_int(num):
    while True:
        res = input(num)
        try:
            return int(res)
        except ValueError:
            print("Apenas números inteiros")

num1 = is_int("Digite o primeiro número: ")
num2 = is_int("Digite o segundo número: ")
num3 = is_int("Digite o terceiro número: ")
soma = num1 + num2 + num3
print(f"A soma dos três números é: {soma}")