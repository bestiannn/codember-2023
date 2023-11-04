import os

# Obtén la ruta absoluta del archivo en ejecución
current_file = os.path.abspath(__file__)

# leer archivo de texto que esta en la misma carpeta que este archivo
with open(os.path.join(os.path.dirname(current_file), 'message_01.txt')) as f:
    data = f.read()
    palabras = data.split()
    palabras_ordenadas = {}
    for palabra in palabras:
        palabra = palabra.lower()
        if palabra in palabras_ordenadas:
            palabras_ordenadas[palabra] += 1
        else:
            palabras_ordenadas[palabra] = 1

# Imprime el contenido del archivo
# print(palabras_ordenadas)

# Imprime el resultado final
print("submit ", end='')
for palabra, cantidad in palabras_ordenadas.items():
    print(f'{palabra}{cantidad}', end='')