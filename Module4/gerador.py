# gerador é isso aqui: for in range() é o range.

def contar_ate_5():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

# Usando o "gerador" que a função criou
for numero in contar_ate_5():
    print(numero)
