# Caesar cipher. cada letra é substituida por seu consequente mais proximo (A se torna B, e B se torna C)
# exceção (Z se torna A)
text = input("Enter your message: ")
cipher = ''
for char in text:
    if not char.isalpha(): # se a letra não for alfabeto, ignore...
        continue
    char = char.upper()
    code = ord(char) + 1 # incrementa a letra (pra pegar a seguinte)
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)

print(cipher)
    