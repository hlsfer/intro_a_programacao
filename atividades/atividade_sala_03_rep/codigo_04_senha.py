#4.Faça um programa que peça ao usuário para digitar uma senha. O programa só deve parar quando ele digitar a senha correta: 1234.


from funcoes import is_number

c_pass = "1234"
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