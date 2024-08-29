'''l=[1,2,10,20,'abc',1]
print(l[0])
print(l[1])
if 10 in l:
    print('available')
else:
    print('not available')
for i in l:
    print(i)
l[1]=7
print(l)'''

#list methods
#adding
'''l=[]
l.append(10)
l.append('abc')
l.append([21,80,9])
if 21 in l:
    print('avl')
else:
    print('not')
l.extend([444,555,666])
l.insert(3,7)
print(l)'''

#delete

'''l=[10,20,30]
l.clear()
l.pop(0)
l.remove(30)
print(l)'''

#index,sort(ascending),reverse

'''l=[7,2,10,6,9,7]
print(l.index(10))
print(l.count(7))
l.sort()
l.reverse()
print(l)'''

#sum of list

'''l=[1,10,12,'abc',8.5]
sum=0
for i in l:
    if type(i)==int or type (i)==float:
        sum+=i
    print(sum)'''

#sum of odd no.s

'''l=[10,1,2,3,5,8,6]
o=0
e=0
for i in l:
    if i%2!=0:
        o+=i
    else:
        e+=i
print('sum of odd no.s= ',o)
print('sum of even no.s= ',e)'''

#avoid duplication

'''l=[10,1,2,3,5,8,6,1,3,8]
for i in l:
    if l.count(i)>=2:
        l.remove(i)
print(l)'''

#set method

'''l=[10,1,2,3,5,8,6,1,3,8]
s=set(l)
l=list(s)
print(l)'''

#3 method
 
'''l=[10,1,2,3,5,8,6,1,3,8]
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
print(l1)'''

#reverse and palindrome of string
'''l=['malayalam','amma','apple','orange']
for i in l:
    rev=i[::-1]
    if rev==i:
        print(rev,'palindrome')
    else:
        print(rev,'not palindrome')'''

#no.s not divisible by 3
'''l=[12,7,9,15,36,45,18]
for i in l:
    if i%3==0:
        print(i,'divisible')
else:
    print(i,'not divisible')'''

#arithematic operation choices

'''while True:
    print(''''''
1.add
2.sub
3.mult
4.div
5.exit
    '''''')
    ch=int(input('enetr your choice: '))
    if ch==1:
        a=int(input('enetr first no: '))
        b=int(input('enetr second no: '))
        c=a+b
        print(c)
    elif ch==2:
        a=int(input('enetr first no: '))
        b=int(input('enetr second no: '))
        c=a-b
        print(c)
    elif ch==3:
        a=int(input('enetr first no: '))
        b=int(input('enetr second no: '))
        c=a*b
        print(c)
    elif ch==4:
        a=int(input('enetr first no: '))
        b=int(input('enetr second no: '))
        c=a/b
        print(c)
    elif ch==5:
        break
    else:
        print('invalid choice')
'''

#student details
'''std=[]
while True:
    print(''''''
1.add std
2.view std
3.update std
4.delete std
5.exit
    '''''')
    ch=int(input('enetr your choice: '))
    if ch==1:
        name=str(input('eneter name: '))
        age=int(input('eneter age: '))
        mark=int(input('enter marks: '))
        std.append([name,age,mark])
    elif ch==2:
        for i in std:
            print(i)
    elif ch==3:
        name=str(input('enter name'))
        f=0
        for i in std:
            if name in i:
                mark=int(input('enter mark'))
                i[2]=mark
                f=1
        if f==0:
            print('invalid name')

    elif ch==4:
        name=str(input('enter name'))
        f=0
        for i in std:
            if name in i:
                std.remove(i)
                f=1
        if f==0:
            print('invalid name')
    elif ch==5:
        break
    else:
        print('invalid choice')'''

#employee details
emp=[]
id=100
import datetime
while True:
    print('''
1.register emp
2.view emp
3.update emp
4.delete emp
5.add work
6.search
7.exit
    ''')
    ch=int(input('enter your choice: '))
    if ch==1:
        name=str(input('enter name: '))
        id+=1
        empid=id
        age=int(input('enter age: '))
        place=str(input('enter place: '))
        salary=int(input('enter salary: '))
        position=str(input('enter positon: '))
        experience=str(input('enter experience: '))
        emp.append([name,age,id,place,salary,position,experience])
    elif ch==2:
        for i in emp:
            print(i)
    elif ch==3:
        name=str(input('enter name: '))
        f=0
        for i in emp:
            if name in i:
                salary=int(input('enter salary: '))
                i[2]=salary
                f=1
        if f==0:
            print('invalid name')
        f=0
        for i in emp:
            if name in i:
                experience=str(input('enter experience: '))
                i[3]=experience
                f=1
        if f==0:
            print('invalid name')
    elif ch==4:
        name=str(input('enter name: '))
        f=0
        for i in emp:
            if name in i:
                emp.remove(i)
                f=1
        if f==0:
            print('invalid name')
    elif ch==5:
        import datetime
        while True:
            id=input('eneter id: ')
            for i in emp:
                if id in i:
                    task=input('enter task: ')
                    date=datetime.datetime.now().strftime('%x')
                    i.append([task,date])
            print(emp)
    elif ch==6:
        id=input('enter id: ')
        f=0
        for i in emp:
            if id in i:
                print(i)
                f=1
            if f==0:
                print('id not found')        
    elif ch==7:
            break
    else:
            print('invalid choice')

   


