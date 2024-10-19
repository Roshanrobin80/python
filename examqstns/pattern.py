# A 
# B A 
# C B A 
# D C B A 

'''a=65
for i in range(1,5):
    for j in range(i):
        print(chr(a-j),end=' ')
    a+=1
    print()'''

# A B C 
# A B 
# A 


'''x=4
for i in range(1,4):
    a=65
    for j in range(1,x):
        print(chr(a),end=' ')
        a+=1
    x-=1
    print('')'''


# 1 2 3 
# 1 2 
# 1 

'''x=4
for i in range(1,4):
    a=1
    for j in range(1,x):
        print(a,end=' ')
        a+=1
    x-=1
    print('')'''

# 1 2 1 
# 1 2 1 
# 1 2 1 

'''for i in range(1,4):
    for j in range(1,4):
        if j%2==0:
            print('2',end=' ')
        else:
            print('1',end=' ')
    print('')'''