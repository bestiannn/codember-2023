import os

# Obtén la ruta absoluta del archivo en ejecución
current_file = os.path.abspath(__file__)

# leer archivo de texto que esta en la misma carpeta que este archivo
with open(os.path.join(os.path.dirname(current_file), 'encryption_policies.txt')) as f:
    data = f.read()
    incorrect_passwords = []

    for line in data.splitlines():
        parameters = line.split(':')[0]
        min_value = parameters.split(' ')[0].split('-')[0]
        max_value = parameters.split(' ')[0].split('-')[1]
        char_value = parameters.split(' ')[1]
        password = line.split(':')[1]
        
        char_count = password.count(char_value)
        if char_count < int(min_value) or char_count > int(max_value):
            incorrect_passwords.append(password)

#print(f'Hay {len(incorrect_passwords)} passwords incorrectas')
#print(incorrect_passwords)

print(f'La password incorrecta numero 13 es: {incorrect_passwords[12]}')