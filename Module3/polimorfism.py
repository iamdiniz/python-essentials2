class Animal:
    def falar(self):
        raise NotImplementedError("Subclasse precisa implementar este método")

class Cachorro(Animal):
    def falar(self):
        return "Au Au!"

class Gato(Animal):
    def falar(self):
        return "Miau!"

# # Usando polimorfismo
# animais = [Cachorro(), Gato()]

# for animal in animais:
#     print(animal.falar())

gato = Gato()
print(gato.falar())

dog = Cachorro()
print(dog.falar())