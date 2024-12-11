# Vamos criar um gerador que gera os números 0, 1, 2, 3, 4
numeros_gen = (x for x in range(5))  # Isso cria um gerador, não uma lista

# Para ver os valores gerados, você pode percorrer o gerador
for numero in numeros_gen:
    print(numero)
