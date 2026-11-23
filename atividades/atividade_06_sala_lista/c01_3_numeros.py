#append remove pop len()

from funcoes import is_number

n = [is_number("Digite um número: ")]

for i in range(2):
    n.append(is_number("Digite um número: "))
    
print(n)