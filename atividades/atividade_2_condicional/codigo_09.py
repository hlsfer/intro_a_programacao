#Faça um programa que leia uma senha e informe se ela está correta ou incorreta, considerando a senha python123.

c_pass = "python123"

while True:
    password = input("Digite a sua senha: ")
    if password == c_pass:
        print("Senha autenticada com sucesso")
        break
    else:
        print("Sennha incorreta. Tente novamente.")