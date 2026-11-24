#Crie uma função chamada senha_forte(senha) que receba uma senha e retorne se ela é forte ou fraca. Uma senha será considerada forte se possuir pelo menos 8 caracteres, tiver pelo menos uma letra maiúscula, tiver pelo menos uma letra minúscula e tiver pelo menos um número. Não é necessário verificar caracteres especiais.

def senha_forte(senha: list[str]) -> str:
    cont_maiusculo = False
    cont_minusculo = False
    cont_num = False
    if len(senha) < 8:
        return "Senha fraca."
    for i in senha:
        if i.isupper():
            cont_maiusculo = True
        if i.islower():
            cont_minusculo = True
        if i.isdigit():
            cont_num = True
    if cont_maiusculo and cont_minusculo and cont_num:
        return "Senha forte."
    else:
        return "Senha fraca."
    
senha = input("Digite sua senha: ")
print(senha_forte(senha))