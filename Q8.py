print('r = rock\np = paper\ns = scissor')
tie = False

while tie==False:
    p1 = input('P1: Choose one: ')
    p2 = input('P2: Choose one: ')
    if p1!=p2:
        if p1 == 'r'and p2 == 's':
            print('P1 Win')
        elif p1 == 's'and p2 == 'p':
            print('P1 Win')
        elif p1 == 'p' and p2 == 'r':
            print('P1 Win')
        else:
            print('P2 win')
        break
    else:
        tie = True
        print('Try again')



