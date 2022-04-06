def metade(valor):
    x = (valor/2)
    return x


def dobro(valor):
    x = (valor*2)
    return x


def aumentar(valor):
    x = ((valor*(10/100)) + valor)
    return x


def reduzindo(valor):
    x = (valor - (valor*(13/100)))
    return x


def moeda(valor):
    return "R${:.2f}".format(valor).replace(".", ",")
