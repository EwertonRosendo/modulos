def metade(valor, form=True):
    x = (valor/2)
    return x if form is False else moeda(x)
def dobro(valor, form=True):
    x = (valor*2)
    return x if form is False else moeda(x)


def aumentar(valor, form=True):
    x = ((valor*(10/100)) + valor)
    return x if form is False else moeda(x)


def reduzindo(valor, form=True):
    x = (valor - (valor*(13/100)))
    return x if form is False else moeda(x)

def moeda(valor):
    return "R$ {:.2f}".format(valor).replace(".", ",")