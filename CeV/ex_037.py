from time import sleep
sm = 0
while True:
    ni_user = int(input("Digite um número: "))
    print("Escolha uma opção abaixo para converter o número digitado:"
          " \n[ 1 ] Binário \n[ 2 ] Octal \n[ 3 ] Hexagonal \n[ 4 ] Sair do Programa")
    c_user = int(input("Opção escolhido: "))
    if c_user == 1:
        sm = bin(ni_user)
    elif c_user == 2:
        sm = oct(ni_user)
    elif c_user == 3:
        sm = hex(ni_user)
    elif c_user == 4:
        print("Encerrando Programa...")
        sleep(1.5)
        print("Programa Finalizado.")
        break
    else:
        print("Valor inválido, tente novamente.")
    print(sm)
