def verificar_idade(idade):
    if idade < 18:
        raise ValueError("Idade deve ser 18 ou mais.")
    print("Idade válida!")

try:
    verificar_idade(15)
except ValueError as e:
    print("Erro:", e)