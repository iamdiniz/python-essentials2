# Compreensão de gerador
numeros_gen = (x for x in range(5))  # Isso cria um gerador, não uma lista

# Transformando o gerador em uma lista
numeros_lista = list(numeros_gen)

print(numeros_lista)  # Agora temos uma lista real
