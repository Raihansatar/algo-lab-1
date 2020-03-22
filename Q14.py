text = input('Enter a text: ')

st = text.split(' ')

for i in range(len(st)):
    print(st[i][::-1], end =' ')