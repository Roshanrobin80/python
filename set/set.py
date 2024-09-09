#intro

'''s={1,4,5,6,8,'abc',2.0,4,5}
for i in s:
    print(i)
if 7 in s:
    print('True')
else:
    print('false')'''

'''L=[1,2,3,4,5,1,2,3,4]
s=set(L)
L=list(s)
print(L)'''

#set methods
#add,delete 

'''s=set()
s.add(10)
s={10,11,12}
s.pop()
s.discard(10)
s.remove(11)
s.clear()
s.copy()
print(s)'''

'''s={1,2,3,4,5}
#s1={1,2,3,6}
# print(s.difference(s1))
# print(s.union(s1))
#print(s.intersection(s1))
#print(s.symmetric_difference(s1))
s2={6,7,8}
#print(s.isdisjoint(s2))
s1={1,2,3,4,5,6}
#print(s.issubset(s1))
#print(s1.issuperset(s))
#print(s.update({10,11,12}))
#print(s.difference_update(s1))'''

#input names & display on set

'''s=set()
a=int(input('Enter the limit: '))
for i in range(a):
    b=str(input('Enter name: '))
    s.add(b)
print(s)'''

#php=   {a,b,c}
# java= {a,c,d,e}
#python={a,b,d,f,g}

php=set()
a=int(input('Enter the limit: '))
for i in range(a):
    b=str(input('Enter name: '))
    php.add(b)


java=set()
e=int(input('Enter the limit: '))
for i in range(e):
    c=str(input('Enter name: '))
    java.add(c)


python=set()
f=int(input('Enter the limit: '))
for i in range(f):
    d=str(input('Enter name: '))
    python.add(d)
print('python =',python)
print('php =',php)
print('java =',java)
inter=php.intersection(java)
print('Common in 3 sub =',inter.intersection(python))
diff=php.symmetric_difference(java)
print('Only in 1 sub =',diff.symmetric_difference(python))


