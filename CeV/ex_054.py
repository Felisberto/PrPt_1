from datetime import date
y_a = date.today().year
mo = me = 0
for c in range(1, 8):
    bdn_user = int(input("Digite o seu ano de nascimento: "))
    yo = y_a - bdn_user
    if yo > 18:
        mo += 1
    elif yo < 18:
        me += 1
print(f"Há {mo} usuários cadastrados com mais de 18 anos de idade.")
print(f"Há {me} usuários cadastrados com menos de 18 anos de idade.")
