def dividir(dividendo, divisor):
    assert divisor != 0, "O divisor não pode ser zero!" # a mensagem é opcional
    return dividendo / divisor

print("Resultado: ", dividir(7, 1))

#**************************************************************************************
print()

def processar_lista(lista):
    assert isinstance(lista, list), "O argumento deve ser uma lista."
    for i in lista:
        print(i)
        
lista = [1, 2, 3, "fim"]
numero_aleatorio = 5
print("Lista: ", processar_lista(lista))

#**************************************************************************************
print()

def buscar_item(lista, index):
    assert index < len(lista), "Index fora dos limites."
    return lista[index]

print(buscar_item(lista, 0))