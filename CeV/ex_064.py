nu_user = som = 0
while nu_user != 999:
    nu_user = int(input("Digite um valor: "))
    som += nu_user
    if nu_user == 999:
        som = som - 999
print(f"A soma entre todos os números digitados foi {som}")
