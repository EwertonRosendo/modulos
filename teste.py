from ex107 import moeda
p = float(input("Digite um preço: R$ "))
print(f"A metade de R${p} é R${moeda.metade(p)}")
print(f"A metade de R${p} é R${moeda.dobro(p)}")
print(f"Aumentando 10% de R${p}, temos: R${moeda.aumentar(p)}")
print(f"Diminuindo 13% de {p}, temos: R${moeda.reduzindo(p)}")
