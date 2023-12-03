import os

# Obtén la ruta absoluta del archivo en ejecución
current_file = os.path.abspath(__file__)

# leer archivo de texto que esta en la misma carpeta que este archivo
with open(os.path.join(os.path.dirname(current_file), 'files_quarantine.txt')) as f:
    data = f.read()
    good_files = []

    for line in data.splitlines():
        first_part, second_part = line.split('-')
        current_checksum = ""
        for char in first_part:
            if first_part.count(char) == 1:
                current_checksum += char
        if current_checksum == second_part:
            good_files.append(first_part)

#print(good_files)
print(good_files[32])