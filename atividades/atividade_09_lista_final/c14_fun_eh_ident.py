#Crie uma função chamada eh_identidade(matriz) que receba uma matriz 3x3 e verifique se ela é uma matriz identidade. Uma matriz identidade possui valor 1 na diagonal principal e valor 0 em todas as outras posições. O programa deve informar se a matriz é ou não identidade.

def eh_identidade(matriz) -> str:
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i == j and matriz[i][j] != 1:
                return "Não é matriz identidade"
            if i != j and matriz[i][j] != 0:
                return "Não é matriz identidade"
                
    return "Matriz identidade"
    