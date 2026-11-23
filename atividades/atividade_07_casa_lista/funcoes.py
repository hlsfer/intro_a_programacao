def is_int(num):
    while True:
        res = input(num)
        try:
            return int(res)
        except ValueError:
            print("Apenas números inteiros")

def is_number(num):
    while True:
        res = input(num)
        try:
            return float(res)
        except ValueError:
            print("Apenas números são aceitos.")