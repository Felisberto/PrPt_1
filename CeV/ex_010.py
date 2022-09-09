quant_unit_real = float(input("R$: "))
conv_dolar = quant_unit_real / 5.17
conv_euro = quant_unit_real / 5.20
conv_in = conv_dolar / 0.0070 
# Valores da moeda no dia, podendo aumentar ou diminuir#
print(f"Você possui {quant_unit_real} reais.")
print(f"Com {quant_unit_real} reais você pode comprar:")
print(f"{conv_dolar:.2f} Doláres.")
print(f"{conv_euro:.2f} Euros.")
print(f"{conv_in:.3f} Ienes.")
