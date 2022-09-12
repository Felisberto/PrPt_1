u_se = float(input("Ângulo do seno: "))
u_co = float(input("Ângulo do cosseno: "))
u_tan = float(input("Ângulo da tangente: "))
from math import radians, sin, cos, tan
print(f"Ângulo do seno é {radians(sin(u_se))}")
print(f"Ângulo do cosseno é {radians(cos(u_co))}")
print(f"Ângulo da tangente é {radians(tan(u_tan))}")
print("FIM DO PROGRAMA.")
