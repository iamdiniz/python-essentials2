"""
Sintaxe:
    a palavra lambda e os : são essenciais.

                            keyword:
    nome_da_funcao_lambda = lambda: "valor"

    sem_argumentos = lambda: "Olá, Mundo!"

    com_um_argumento = lambda argumento: argumento ** 2

    dois_argumento = lambda argumento1, argumento2: argumento1 + argumento2

"""

print("Exemplo com soma:")
soma = lambda num1, num2: num1 + num2
print(soma(5, 5))

# exemplo de uso: filtrando pares com filter

print("Exemplo filtrando lista com pares:")
numeros = [1, 2, 3, 4, 5]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # Saída: [2, 4]

# dobrando os numeros com map

print("Exemplo criando uma nova lista com os numeros dobrados da lista anterior:")
lista_de_numeros = [1, 2, 3, 4]
dobrados = list(map(lambda x: x * 2, lista_de_numeros))
print(dobrados)  # Saída: [2, 4, 6, 8]