#Leia uma lista com 12 números inteiros e crie uma nova lista contendo apenas os números positivos e zero. O programa não deve usar funções prontas de filtro.

n = []
n_pos = []

for i in range(12):
    while True:   
        try: 
            num_temp = int(input("Digite um número inteiro: "))
            break
        except ValueError:
            print("Apenas números inteiros")
    
    n.append(num_temp)
    if num_temp >= 0:
        n_pos.append(num_temp)
        
print(f"Lista original: {n}")
print(f"Lista apenas com positivos e zero: {n_pos}")
