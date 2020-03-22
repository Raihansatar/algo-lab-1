
a= [1,2,2,2,2,5,5,4,3]


def removedup (a):
    b=[]
    a.sort()

    for i in range(len(a)):
        if i ==0:
            b.append(a[i])
        else:

            if a[i]==a[i-1]:
                continue
            else:
                b.append(a[i])
    return b

print(removedup(a))
