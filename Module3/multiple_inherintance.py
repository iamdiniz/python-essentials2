class Goku:
    var_a = 10
    def fun_a(self):
        return 11

class Vegeta:
    var_b = 20
    def fun_b(self):
        return 21 
 
class Vegito(Goku, Vegeta): # Herança múltipla. Herda de mais de uma superclasse
    pass
 
super_vegito = Vegito()
 
print(super_vegito.var_a, super_vegito.fun_a())
print(super_vegito.var_b, super_vegito.fun_b())