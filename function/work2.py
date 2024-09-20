
def reg():
    if len(user)==0:
        id=101
    else:
        id=user[-1]['id']+1
    email=str(input('enter your email: '))
    f=0
    for i in user:
        if i['email']==email:
            f=1
            reg()
    if f==0:
        name=str(input('enetr name: '))
        age=int(input('enter age: '))
        phone=int(input('enter phone no: '))
        password=input('enter password: ')
        user.append({'id':id,'name':name,'age':age,'email':email, 'phone':phone,'password':password})

def login():
    uname=input('enter uname: ')
    password=input('enter pass: ')
    f=0
    if uname=='admin' and password=='admin':
         f=1
    usr=''
    for i in user:
         if uname==i['email'] and password==i['password']:
              f=2
              usr=i
    return f,usr

user=[]
lib=[]
while True:
    print('''
    1.register
    2.login
    3.exit
     ''')
    ch=int(input('enter your choice: '))
    if ch==1:
        reg()
    elif ch==2:
        f,usr=login()
        if f==1:
            print('admin login')
        elif f==2:
            print('user logged in')
        elif f==0:
            print('invalid uname or password')