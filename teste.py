from ex108 import moeda
p = float(input("Digite um preço: R$ "))
print(f"A metade de R${p} é {moeda.moeda(moeda.metade(p))}")
print(f"A metade de R${p} é {moeda.moeda(moeda.dobro(p))}")
print(f"Aumentando 10% de R${p}, temos: {moeda.moeda(moeda.aumentar(p))}")
print(f"Diminuindo 13% de R${p}, temos: {moeda.moeda(moeda.reduzindo(p))}")
