class Empresario:
    def __init__(self, nome, nome_empresa, dinheiro,):
        self.nome = nome
        self.nome_empresa = nome_empresa
        self.__dinheiro = dinheiro

    def get_dinheiro(self): # se não tiver o get, não tem como obter esse dado
        return self.__dinheiro

empresario1 = Empresario("Mel", "E-Corp", "2.000")
print(empresario1.get_dinheiro())