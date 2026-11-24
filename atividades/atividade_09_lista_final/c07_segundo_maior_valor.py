#Leia uma lista com 10 números inteiros e descubra o segundo maior valor da lista. Atenção: o maior valor pode aparecer mais de uma vez. Exemplo: na lista [4, 8, 8, 2, 6], o segundo maior valor é 6.

from funcoes import is_int

n = []
maior = float('-inf')
segundo_maior = float('-inf')

for i in range(10):
    n.append(is_int("Digite um número inteiro: "))
    
for i in n:
    if i > maior:
        segundo_maior = maior
        maior = i  
    elif i < maior and i > segundo_maior:
        segundo_maior = i
    
if segundo_maior != float('-inf'):
    print(f"O segundo maior número digitado é: {segundo_maior}")
else:
    print("Os números digitados são todos iguais.")