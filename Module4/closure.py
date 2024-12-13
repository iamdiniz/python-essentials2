def saudacao(nome):
    def mensagem():
        return f"Olá, {nome}!"
    return mensagem

cumprimento = saudacao("Diniz")  # Aqui, o nome "Diniz" é lembrado pela função mensagem
print(cumprimento())  # Saída: Olá, Diniz!

