n_tp = input("Digite algo: ")
print(type(n_tp))
print("Tem apenas números:", n_tp.isnumeric())
print("Tem apenas letras:", n_tp.isalpha())
print("Tem letras e números juntos:", n_tp.isalnum())
print("Está tudo em maiúsculo:", n_tp.isupper())
print("Está tudo em minúsculo:", n_tp.islower())
