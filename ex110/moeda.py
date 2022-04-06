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


def aumentar(valor, form=True):
    x = ((valor*(10/100)) + valor)
    if form == False:
        return x
    else:
        return "R${:.2f} ".format(x).replace(".", ",")


def reduzindo(valor, form=True):
    x = (valor - (valor*(13/100)))
    if form == False:
        return x
    else:
        return "R${:.2f} ".format(x).replace(".", ",")



def resumo():
    print("_"*32), print("        RESUMO DO VALOR"), print("_"*32)