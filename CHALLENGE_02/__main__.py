import os

# Obtén la ruta absoluta del archivo en ejecución
current_file = os.path.abspath(__file__)

# leer archivo de texto que esta en la misma carpeta que este archivo
with open(os.path.join(os.path.dirname(current_file), 'message_02.txt')) as f:
    data = f.read()
    cont = 0
    for char in data:
        if char == '#':
            cont += 1
        elif char == '@':
            cont -= 1
        elif char == '*':
            cont *= cont
        elif char == '&':
            print(cont, end='')