def number():
    a=int(input('Enter a number'))
    b=int(input('Enter a number'))
    return(a,b)
def add():
    a,b=number()
    print(a+b)

def sub():
    a,b=number()
    print(a-b)

def mul():
    a,b=number()
    print(a*b)

def div():
    a,b=number()
    print(a/b)

def mod():
    a,b=number()
    print()

while True:
    ('''
     1.add
     2.sub
     3.mul
     4.div
     5.mod
     6.exit
     ''')
    ch=int(input('Enter your choice :'))
    if ch==1:
        add()