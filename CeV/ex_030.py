n_pri = int(input("Escolha um número: "))
if n_pri % 2 == 0:
    print("O número escolhido é \033[42mPAR\033[42m.")
else:
    print("O número escolhido é \033[41mÍMPAR\033[41m.")
