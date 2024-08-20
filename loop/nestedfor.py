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

for i in range(4):
    for j in range(3):
        if i%2==0:
            print(j,end=' ')
        else:
            print(2-j,end=' ')
    print()
        