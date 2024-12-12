# Verificar se números em uma lista são pares usando map com lambda
numeros = [1, 2, 3, 4, 5, 6]
pares = list(map(lambda x: x % 2 == 0, numeros))
print(pares)  # Saída: [False, True, False, True, False, True]