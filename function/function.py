'''def sample():
    print('carlos')
    print('cafu')
    print('kaka')
a=[1,2,3,4,5]
print(a)
a.append(10)
sample()
a=[1,2,3,4,5]
print(a)
a.append(10)
sample()'''

#calling global and local variable

'''def sample():
    b=10            #local variable
    print('inside function a=',a)
    print('inside function b=',b)
a=20                #global variable
sample()
print('outside function a=',a)
print('outside funcyion b=',b)'''

'''def sample():
    a=10
    print('inside function a =',a)
a=20
sample()
print('outside function a =',a)'''

#global keyword

'''def sample():
    global a
    a=10
    print('welcome',a)
sample()
print(a)

#return keyword

def sample():
    a=10
    b=20
    return 'welcome',a,b
c,a1,b1=sample()
print(a1)
print(b1)
print(c)'''

#arithematic operations 

'''def number():
    a=int(input('Enter a number: '))
    b=int(input('Enter a number: '))
    return a,b
def add():
    a,b=number()
    print(a+b)

while True:
    print(''''''
1.add
2.sub
3.mul
4.div
5.flr div
6.exit
      '''''')
    ch=int(input('Enter your choice: '))
    if ch==1:
        add()

    elif ch==2:
        a,b=number()
        print(a-b)

    elif ch==3:
        a,b=number()
        print(a*b)

    elif ch==4:
        a,b=number()
        print(a/b)

    elif ch==5:
        a,b=number()
        print(a//b)

    elif ch==6:
        break
    else:
        print('Invalid choice')
        '''
#Types of argument
#1 positional argument

'''def sample(a,b):
    print(a,b)
sample(10,20)
sample('asd',20)
sample(['asd',20,21],20)  '''  

#keyword argument

'''def sample(name,age):
    print('name:',name)
    print('age:',age)
sample('anu',20)
sample(20,'arun')
sample(age=20,name='akhil')'''

#Lambda function

'''data=lambda a,b:a+b
print(data(10,5))'''

'''data=lambda:print('welcome')
data()'''

#filter

'''l=['hello','welcome','apple','kiwi']
print(list(filter(lambda x:'e' in x,l)))'''