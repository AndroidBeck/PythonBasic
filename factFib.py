__author__ = 'Evdokimov'

def factorial(x):
    if x==1:
        return 1
    return x*factorial(x-1)

#print(factorial(4))

def fib(x):
    if x ==0 or x ==1:
        return 1
    return fib(x-1) + fib(x-2)

#print fib(30)

#Beautiful variation
#fib = lambda n: fib(n - 1) + fib(n - 2) if n > 2 else 1

def fibgen(x):
    i=2
    a=0
    b=1
    print("0: {0}".format(a)) #fib(0)
    print("1: {0}".format(b)) #fib(1)
    while i<=x:
        fib = a+b
        print("{0}: {1}".format(i,fib))
        i+=1
        a,b = b,fib


fibgen(100)
#print(fib(30))
