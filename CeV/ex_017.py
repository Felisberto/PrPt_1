u_cat_op = float(input("Cateto Oposto: "))
u_cat_ad = float(input("Cateto Adjacente: "))
from math import hypot
print(f"Tendo o valor do cateto oposto de {u_cat_op} e do cateto adjacente de {u_cat_ad}.\nO comprimetro da hipotenusa é de {hypot(u_cat_op, u_cat_ad)}")
