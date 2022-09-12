n_stu_on = str(input("Nome: "))
n_stu_se = str(input("Nome: "))
n_stu_th = str(input("Nome: "))
n_stu_fo = str(input("Nome: "))
lt = [n_stu_on, n_stu_se, n_stu_th, n_stu_fo]
from random import choice
print(f"Quem foi escolhido foi {choice(lt)}")
