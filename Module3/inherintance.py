class Pai:
    def __init__(self, name, idade, dinheiro):
        self.name = name
        self.idade = idade
        self.dineiro = dinheiro

    def __str__(self): # Esse método foi herdado
        return f"My name is {self.name}. \n I hava a {self.idade} years old. Ima Pursuing ${self.dineiro:.3f}" # separador de casas decimais :.2f


class Filho(Pai):
    def __init__(self, name, idade, dinheiro):
        Pai.__init__(self, name, idade, dinheiro)


obj = Filho("Diniz", 21, 2.000)

print(obj)
# Out: My name is Andy. I hava a 21 years old