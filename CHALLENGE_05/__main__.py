import os

# Obtén la ruta absoluta del archivo en ejecución
current_file = os.path.abspath(__file__)

# leer archivo de texto que esta en la misma carpeta que este archivo
with open(os.path.join(os.path.dirname(current_file), 'database_attacked.txt')) as f:
    data = f.read()
    invalid_users = []

    for line in data.splitlines():
        id, username, email, age, location = line.split(',')

        if id == "" or not id.isalnum():
            invalid_users.append(username)
            continue
        if username == "" or not username.isalnum():
            invalid_users.append(username)
            continue
        if email == "" or "@" not in email or email.split("@")[0] == "" or "." not in email.split("@")[1] or email.split("@")[1].split(".")[0] == "" or email.split("@")[1].split(".")[1] == "":
            invalid_users.append(username)
            continue
        if age != "" and not age.isdigit():
            invalid_users.append(username)
            continue
        if location != "" and not location.replace(" ","").isalpha():
            invalid_users.append(username)
            continue

#print(invalid_users)
for user in invalid_users:
    print(user[0],end="")