def metade(valor, form=True):
    x = (valor/2)
    if form == False:
        return x
    else:
        return "R${:.2f} ".format(x).replace(".", ",")


def dobro(valor, form=True):
    x = (valor*2)
    if form == False:
        return x
    else:
        return "R${:.2f} ".format(x).replace(".", ",")


def aumentar(valor, form=True, porc=1):
    x = ((valor*(porc/100)) + valor)
    if form == False:
        return x
    else:
        return "R${:.2f} ".format(x).replace(".", ",")


def reduzindo(valor, form=True, porc=1):
    x = (valor - (valor*(porc/100)))
    if form == False:
        return x
    else:
        return "R${:.2f} ".format(x).replace(".", ",")



def resumo(valor, mais=10, menos=13):
    print("_"*32), print("        RESUMO DO VALOR"), print("_"*32)
    if "." in valor:
        print("Preço analisado:  R${:.2f}".format(valor).replace(".", ","))
    else:
        print("Preço analisado:  R${:.2f}".format(valor))
    print(f"Dobro do preço:   {dobro(valor)}")
    print(f"Metade do Preço:  {metade(valor)}")
    print(f"{mais}% de aumento:   {aumentar(valor, porc=mais)}")
    print(f"{menos}% de redução:   {reduzindo(valor, porc=menos)}")
    print("_"*32)
