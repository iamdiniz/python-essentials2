# Verificar se números em uma lista são pares usando map com lambda
numeros = [1, 2, 3, 4, 5, 6]
pares = list(map(lambda x: x % 2 == 0, numeros))
print(pares)  # Saída: [False, True, False, True, False, True]

"""
A map retorna um objeto do tipo map, que é um iterador. Para visualizar o resultado,
geralmente o convertemos para uma lista ou outra estrutura, como o list()
"""