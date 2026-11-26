#Em uma eleição com 4 candidatos, leia 30 votos. Os votos válidos são: 1 para candidato A, 2 para candidato B, 3 para candidato C e 4 para candidato D. Qualquer outro número será considerado voto nulo. Ao final, mostre o total de votos de cada candidato, o total de votos nulos, o candidato vencedor e se houve empate.

from funcoes import is_int

matriz_candidatos = []

for i in range(5):
    linha = []
    if i > 3:
        v_temp = 0
        n_temp = (f"Nulos")
        linha.append(n_temp)
        linha.append(v_temp)
    else:     
        v_temp = 0
        n_temp = (f"Candidato {i + 1}")
        linha.append(n_temp)
        linha.append(v_temp)
    matriz_candidatos.append(linha)
    
for i in range(30):
    print("Selecione para qual candidato vai o seu voto:\n1. Candidato A\n2. Candidato B\n3. Candidato C\n4. Candidato D\nPressione qualquer outro número para voto nulo.")
    voto = is_int("")
    if voto >= 1 and voto <= 4:
        matriz_candidatos[voto - 1][1] += 1
    else:
        matriz_candidatos[4][1] += 1
        
voto_maior = matriz_candidatos[0][1]
for i in range(4):
    if matriz_candidatos[i][1] > voto_maior:
        voto_maior = matriz_candidatos[i][1]
    
vencedor = []
for i in range(4):
    linha = []
    if matriz_candidatos[i][1] == voto_maior:
        linha.append(matriz_candidatos[i][0])
        linha.append(matriz_candidatos[i][1])
        vencedor.append(linha)

print("Resultado final:")        
for i in matriz_candidatos:
    print(f"{i[0]} --- Votos: {i[1]}")

if voto_maior == 0:
        print("Nenhum candidato recebeu votos válidos.")       
elif len(vencedor) > 1:
    print("Houve empate entre os candidatos: ")
    for i in range(len(vencedor)): 
        print(vencedor[i][0])
    print(f"com {vencedor[i][1]} voto(s) cada.")        
else:
        print(f"O vencedor foi o candidato {vencedor[0][0]} com um total de {vencedor[0][1]} votos.")