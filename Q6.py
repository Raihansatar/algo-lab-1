x = input('Enter a string: ')

rx = x[::-1]
print(rx)

if rx == x:
    print('Palinmdrome')
else:
    print('Not Palinmdrome')