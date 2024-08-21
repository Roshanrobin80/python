#pattern design

'''for i in range(3):
    for j in range(3):
        print(i,end=' ')
    print()'''

'''a=0
for i in range(3):
    for j in range(3):
        print(a,end=' ')
        a+=1
    print()'''



'''for i in range(3):
    for j in range(3):
        print(i+j,end=' ')
    print()'''

#0 1 2
#2 1 0
#0 1 2
#2 1 0

'''for i in range(4):
    for j in range(3):
        if i%2==0:
            print(j,end=' ')
        else:
            print(2-j,end=' ')
    print()'''

#0
#0 1
#0 1 2

'''for i in range(1,4):
    for j in range(i):
        print(j,end=' ')
    print()'''

#0
#1 2 
#3 4 5

'''a=0
for i in range(1,4):
    for j in range(i):
        print(a,end=' ')
        a+=1
    print()'''

#0
#1 1
#2 2 2

'''for i in range(1,4):
    for j in range(i):
        print(i-1,end=' ')
    print()'''

#0
#1 0
#2 1 0

'''a=0
for i in range(1,4):
    for j in range(i):
        print(a-j,end=' ')
    a+=1
    print()'''

        