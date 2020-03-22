a = [5, 10, 15, 20, 25]

def newList (a):
        b = []
        b.append(a[0])
        b.append(a[len(a)-1])
        return b

c=newList(a)

print(c)