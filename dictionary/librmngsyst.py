lib=[]
id=1000
while True:
    print('''
1.Add book
2.View book
3.Update book
4.Delete book
5.Search book
6.Exit
''')
    ch=int(input('enter a choice: '))
    if ch==1:
        bname=str(input('enter book name: '))
        id+=1
        bid=id
        price=int(input('enter price of book: '))
        stock=int(input('enter stocks of book: '))
        lib.append({'bname':bname,'bid':bid,'price':price,'stock':stock})

    elif ch==2:
        for i in lib:
            print(i)

    elif ch==3:
        bid=int(input('enter book id: '))
        f=0
        for i in lib:
            if i['bid']==bid:
                nstock=int(input('enter new stocks of book: '))
                nprice=int(input('enter new price: '))
                i['stock']=nstock
                i['price']=nprice
                f=1
        if f==0:
            print('invalid id')

    elif ch==4:
        bid=int(input('enter book id: '))
        f=0
        for i in lib:
            if i['bid']==bid:
                lib.remove(i)
                f=1
        if f==0:
            print('invalid id')

    elif ch==5:
        bid=int(input('enter book id: '))
        f=0
        for i in lib:
            if i['bid']==bid:
                print(i)
                f=1
        if f==0:
            print('invalid id')
    elif ch==6:
        break
    else:
        print('invalid choice')