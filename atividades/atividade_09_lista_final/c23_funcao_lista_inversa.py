#Crie uma função que receba uma lista e retorne outra lista com os elementos em ordem inversa. Não use reverse(), [::-1] ou reversed().

def lista_inversa(lista: list) -> list:
    lista_inversa = []
    for i in range(len(lista)-1, -1, -1):
        lista_inversa.append(lista[i])
    return lista_inversa

lista_teste = []

while True:
    sair = "sair"
    val_temp = input("Digite algo (digite 'sair' para encerrar): ")
    if val_temp != sair:
        lista_teste.append(val_temp)
    else:
        break
    
print(f"Lista original: {lista_teste}")
print(f"Lista inversa: {lista_inversa(lista_teste)}")
    