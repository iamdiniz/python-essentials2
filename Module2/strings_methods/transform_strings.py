# Transformar numero em string
numero_inteiro = 13
numero_flutuante = 1.3
inteiro_transformado_em_string = str(numero_inteiro)
flutuante_transformado_em_string = str(numero_flutuante)

print(inteiro_transformado_em_string + ' ' + flutuante_transformado_em_string)
print(type(inteiro_transformado_em_string))
print(type(flutuante_transformado_em_string))

# Transformar string em numero; só é valido quando a string representa um número vaálido; caso contrario: ValueError
string_em_numero = '13'
transformar_string_em_flutuante = '1.3'
numero_transformado = int(string_em_numero)
flutuante_transformado = float(transformar_string_em_flutuante)

print(numero_transformado + flutuante_transformado)
print(type(numero_transformado))
print(type(flutuante_transformado))