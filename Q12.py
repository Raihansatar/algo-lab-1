
number = eval(input('Enter new Number: '))



def Fib(x):
    if x<=0:
        print('Wrong Number')
    elif x==1:
        return 0
    elif x==2:
        return 1
    else:
        return Fib(x-1) + Fib(x-2)

for i in range (number+1):
    print(Fib(i))

#print(Fib(number))

