gastot = prodc = me = cot = 0
namep = " "
while True:
    name_prod = str(input("Nome do produto: "))
    prod_pric = float(input("Preço do produto: "))
    cot += 1
    gastot += prod_pric
    if prod_pric >= 1000:       
        prodc += 1
    if cot == 1 or prod_pric < me:
        me = prod_pric
        namep = name_prod
    ec = " "
    while ec not in "SN":
        ec = str(input("Deseja continuar?: [S/N]: ")).strip().upper()[0]
    if ec == "N":
        if prodc >= 1:
            print(f"Nesta compra há mais de {prodc} produtos com preço acima de 1000 reais.")
        else:
            print("Não há produtos acima de 1000 reais.")
        break
        
print(f"O gasto total na compra foi de {gastot} reais.")
print(f"O produto mais barato comprado foi {namep} custando {me} reais.")
