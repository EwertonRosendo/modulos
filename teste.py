from ex109 import moeda
p = float(input("Digite um preço: R$"))
print(f"A metade de R${p} é {(moeda.metade(p, True))}")
print(f"A metade de R${p} é {(moeda.dobro(p, True))}")
print(f"Aumentando 10% de R${p}, temos: {(moeda.aumentar(p, True))}")
print(f"Diminuindo 13% de R${p}, temos: {(moeda.reduzindo(p, True))}")
