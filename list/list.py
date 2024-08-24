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