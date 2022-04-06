def metade(valor, form=False):
    x = (valor/2)
    if form == False:
        return x
    else:
        return "R${:.2f} ".format(x).replace(".", ",")
def dobro(valor, form=False):
    x = (valor*2)
    if form == False:
        return x
    else:
        return "R${:.2f} ".format(x).replace(".", ",")


def aumentar(valor, form=False):
    x = ((valor*(10/100)) + valor)
    if form == False:
        return x
    else:
        return "R${:.2f} ".format(x).replace(".", ",")


def reduzindo(valor, form=False):
    x = (valor - (valor*(13/100)))
    if form == False:
        return x
    else:
        return "R${:.2f} ".format(x).replace(".", ",")

