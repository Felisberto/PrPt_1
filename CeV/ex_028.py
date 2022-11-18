from random import randint
pc = randint(0,5)
print("Acerte o número que estou pensando")
pl = int(input("Digite um número de 0 a 5.: "))
if pl == pc:
    print(f"Você acertou, o número que eu estava pensando era mesmo o {pl}")
else:
    print(f"Você errou. eu pensei no número {pc}")
    