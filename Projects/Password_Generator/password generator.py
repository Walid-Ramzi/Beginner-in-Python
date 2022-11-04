def Password():
    from random import shuffle
    from random import choice

    letters = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    symbols = "%@-_!.#"
    characters = list(letters + numbers + symbols)
    shuffle(characters)
    length = int(input("Password length : "))
    password = []
    for i in range(length):
        password.append(choice(characters))
    print()
    print("".join(password))

while True:
    print()
    Password()