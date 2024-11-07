"""fazer com que ela herde de Exception nos permite criar um novo tipo de erro com informações
adicionais quando herdamos de Exception dizemos ao python que a classe deve ser tratada como
uma exceção.
"""
class SaldoInsuficienteError(Exception):
    def __init__(self, saldo, valor_saque):
        super().__init__(f"Saldo insuficiente para saque. Saldo atual: R${saldo:.2f}, Tentativa de saque: R${valor_saque:.2f}")
        self.saldo = saldo
        self.valor_saque = valor_saque
"""
Usamos o super().__init__() para acessar métodos e propriedades da classe 'mãe' (ou superclass)
da classe atual. nesse caso, estamos chamando o construtor da classe Exception e passar
uma mensagem de erro. até porque o __init__ faz um papel de construtor né.
"""

class ContaBancaria:
    def __init__(self, saldo=0.0):
        self.saldo = saldo
    
    def sacar(self, valor):
        if valor > self.saldo:
            # Lança a exceção personalizada se o saldo for insuficiente
            raise SaldoInsuficienteError(self.saldo, valor)
        
        self.saldo -= valor
        print(f"Saque de R${valor:.2f} realizado com sucesso! Saldo atual: R${self.saldo:.2f}")

# Criando uma conta com saldo inicial de R$100.00
conta = ContaBancaria(100.0)

try:
    # Tentativa de saque de um valor maior que o saldo
    conta.sacar(150.0)
except SaldoInsuficienteError as e:
    print("Erro:", e)  # Exibe a mensagem detalhada da exceção