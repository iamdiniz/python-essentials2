class Pessoa:
    def __init__(self, nome, cor, altura,):
        self.nome = nome
        self.cor = cor
        self.altura = altura

    def pensar_no_calculo(self, numero1, numero2):
        soma = numero1 + numero2
        print(f"A soma dos números é {soma}")

pessoa1 = Pessoa("Mel", "Black", "1.10")
print(pessoa1.nome)
pessoa1.pensar_no_calculo(5, 5)