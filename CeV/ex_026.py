lrcs = str(input("Digite uma frase: ")).strip()
print("Em sua frase existe", lrcs.count("A") + lrcs.count("a"), "letra A digitadas.")
print("A letra a aparece pela primeira vez na poscição", lrcs.find("A"))
print("A letra a aparece pela última vez na posição", lrcs.rfind("a"))
