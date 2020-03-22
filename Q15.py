import random
length = 8


def password (passlength):
    text = 'abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?'
    newpass = ''

    for i in range(passlength):
        newpass = newpass + random.choice(text)

    return print(newpass)

print(password(length))