#intro

'''d={'name':'Rahul','age':20,'place':'tvm'}
print(d['name'])
print(d['age'])
print(d['place'])'''

#iterative loop

'''d={'name':'Rahul','age':20,'place':'tvm'}
for i in d:
    print(i,d[i])'''

#updation

'''d={'name':'Rahul','age':20,'place':'tvm'}
d['place']='ktm'
d['age']='23'
print(d)'''

'''d={'name':'Rahul','age':20,'place':'tvm'}
if d['name']=='Rahul':
    print('available')
else:
    print('not available')'''

#methods of dictionary

'''d={'name':'roshan','age':21,'place':'adoor'}
#print(d.get('name1'))

#print(d.items())

#print(d.values())
#for i in d.values():
#    print(i)

#print(d.keys())

# a=d
# a=d.copy()
# print(id(a))
# print(id(d))
# d['mark']=50
# print(a)
# print(d)

#d.pop('age')
#d.popitem()
# d.setdefault('age')
# print(d)
# l=[10,11,12]
# print(d.fromkeys(l))'''

'''d={}
a=input('enter data: ')
b=input('enter data: ')
d[a]=b
print(d)'''

#shop management system

'''shp=[]
id=1000
while True:
    print(''''''
1.Add product
2.View product
3.Update product
4.Delete product
5.Exit
'''''')
    ch=int(input('enter a choice: '))
    if ch==1:
        pname=str(input('enter product name: '))
        id+=1
        pid=id
        price=int(input('enter price of product: '))
        stock=int(input('enter stocks of product: '))
        shp.append({'pname':pname,'pid':pid,'price':price,'stock':stock})

    elif ch==2:
        for i in shp:
            print(i)

    elif ch==3:
        pname=str(input('enter product name: '))
        f=0
        for i in shp:
            if i['pname']==pname:
                nstock=int(input('enter new stocks of product: '))
                nprice=int(input('enter new price: '))
                i['stock']=nstock
                i['price']=nprice
                f=1
        if f==0:
            print('invalid name')

    elif ch==4:
        pname=str(input('enter product name: '))
        f=0
        for i in shp:
            if i['pname']==pname:
                shp.remove(i)
                f=1
        if f==0:
            print('invalid name')
    elif ch==5:
        break
    else:
        print('invalid choice')'''

'''data=[{'name':'a','age':20},
{'name':'b','age':30},
{'name':'c','age':45},
{'name':'d','age':23},
{'name':'e','age':15}]
# for i in data:
    # print(i['age'])
print('{:<10}{:<10}'.format('name','age'))
print('_'*15)
for i in data:
    print('{:<10}{:<10}'.format(i['name'],i['age']))

print('{:<10}{:<10}'.format('name','age'))
print('_'*15)
for i in data:
    if i['age']<=30:
        print('{:<10}{:<10}'.format(i['name'],i['age']))

print('{:<10}{:<10}'.format('name','age'))
print('_'*15)
for i in data:
    if i['age']>30:
        print('{:<10}{:<10}'.format(i['name'],i['age']))'''
#method 2
'''a=[]
b=[]
for i in data:
    if i['age']<=30:
        b.append(i)
    else:
        a.append(i)
print(a)
print(b)'''

#method 3

'''a=[]
b=[]
b=[i for i in data if i['age']<=30]
a=[i for i in data if i['age']>30]
print(a)
print(b)'''

#display each number by words

'''n={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',}
a=int(input('Enter a number: '))
s=''
while a>0:
    d=a%10
    s=n[d]+' '+s
    a//=10
print(s)'''

#display list from dictionary

l=[{'name':'a','age':20,'project':['ems','sms']}]
#print(l[0]['project'][0])

#add to list
a=str(input('Enter project name: '))
l[0]['project'].append(a)
print(l)


