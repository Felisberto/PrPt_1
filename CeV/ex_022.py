from itertools import count


name_user = str(input("Digite seu nome: ")).strip()
print(f"Seja muito bem-vindo(a), {name_user}!")
print(f"Seu nome em maiúsculo fica {name_user.upper()}")
print(f"Seu nome em minúsculo fica {name_user.lower()}")
print(f"Seu nome contem {len(name_user) - name_user.count(' ')} caracteres")
print(f"Seu primeiro nome tem {name_user.find(' ')} caracteres")
