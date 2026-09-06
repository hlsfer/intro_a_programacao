#Faça um programa que leia uma senha e informe se ela está correta ou incorreta, considerando a senha python123.

c_pass = "python123"
attempts = 3

while True:
    password = input(f"Digite a sua senha ({attempts} tentativas restantes): ")
    if password == c_pass:
        print("Senha autenticada com sucesso")
        break
    else:
        print("Sennha incorreta. Tente novamente.")
        attempts -= 1
        if attempts == 0:
            print("Atingiu o limite de tentativas. Tente novamente mais tarde.")
            break