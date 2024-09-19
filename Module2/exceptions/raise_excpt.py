numero = int(input("Digite um número: "))
if numero > 10:
    raise TypeError("Digitou um número maior que 10")
print(numero)