n_p_o = float(input("Nota: "))
n_p_s = float(input("Nota: "))
med = (n_p_o + n_p_s) / 2
if med <= 5:
    print("\033[41mREPROVADO!\033[41m")
elif med <= 6.9:
    print("\033[43mRECUPERAÇÃO\033[43m")
else:
    print("\033[42mAPROVADO\033[42m")
