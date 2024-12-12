numeros = [1, 2, 3, 4, 5, 6]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # Saída: [2, 4, 6]

# filtra para mim todos aqueles que são par...
"""
O filter retorna um objeto do tipo filter, que é um iterador. Para visualizar os resultados,
geralmente convertemos para uma lista, tupla, etc.:
"""

# filtrando todos com a letra P
palavras = ["Python", "map", "lambda", "Programação"]
com_p = list(filter(lambda palavra: palavra.startswith("P"), palavras))
print(com_p)  # Saída: ['Python', 'Programação']
