nu_on = int(input("Digite o primeiro valor: "))
nu_se = int(input("Digite o segundo valor: "))
nu_th = int(input("Digite o terceiro valor: "))
mo = me = vi = 0
if nu_on > nu_se and nu_th < nu_on:
    mo = nu_on
    print(f"O maior número foi o {mo}")
elif nu_se > nu_on and nu_th < nu_se:
    mo = nu_se
    print(f"O maior número foi o {mo}")
elif nu_th > nu_on and nu_se < nu_th:
    mo = nu_th
    print(f"O maior número foi o {mo}")
if nu_on < nu_se and nu_th > nu_on:
    me = nu_on
    print(f"O menor número foi o {me}")
elif nu_se < nu_on and nu_th > nu_se:
    me = nu_se
    print(f"O menor número foi o {me}")
elif nu_th < nu_on and nu_se > nu_th:
    me = nu_th
    print(f"O menor número foi o {me}")
if nu_on == nu_se == nu_th == nu_on:
    vi = nu_on
    print(f"Não há números maiores nem menores, todos são iguais sendo todos {vi}.")
