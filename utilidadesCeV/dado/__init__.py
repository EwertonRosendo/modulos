from utilidadesCeV import moeda
def validador(valor=""):
    if "," in valor or valor.isnumeric():
        valor.replace(",", ".")
        return True
    while valor.isnumeric() is False:
        valor = input("\033[31mInforme um valor valido\033[m")
    if valor.isnumeric() is True:
        return True


