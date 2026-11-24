#Leia uma lista com 10 números inteiros e verifique qual é o tamanho da maior sequência crescente consecutiva. Exemplo: na lista [1, 2, 3, 1, 2, 5, 6, 0, 1, 2], a maior sequência crescente é 1, 2, 5, 6, logo a resposta é 4.

from funcoes import is_int

n = [is_int("Digite um número inteiro: ")]
maior_seq = 1
atual_seq = 1

for i in range(9):
    n.append(is_int("Digite um número inteiro: "))
    
for i in range(len(n) - 1):
    if n[i] < n[i + 1]:
        atual_seq += 1
        if atual_seq > maior_seq:
            maior_seq = atual_seq
    else:
        atual_seq = 1
        
print(f"A maior sequência consecutiva de números crescentes é: {maior_seq}")