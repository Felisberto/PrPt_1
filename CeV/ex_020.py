from random import shuffle
na_on = str(input("Nome: "))
na_se = str(input("Nome: "))
na_th = str(input("Nome: "))
na_fr = str(input("Nome: "))
ls = [na_on, na_se, na_th, na_fr]
shuffle(ls)
print(ls)
