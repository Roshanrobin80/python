'''a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
while a<=b:
    print(a)
    a+=1'''

#sum of natural,odd and even numbers

'''a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
sum=0
odd=0
even=0
while a<=b:
    sum+=a
    if a%2==0:
        even+=a
    else:
        odd+=a
    a+=1
print("sum pf natural numebrs",sum)
print("sum of even numebrs",even)
print("sum of odd numebrs",odd)'''

#multiplication table of a no.

'''a=int(input("Enter a number: "))
b=1
while b<=10:
    c=a*b
    print(f"{a}*{b}={c}")
    b+=1'''

#itertaive loop for string

'''a='python'
i=0
l=len(a)
while i<l:
    print(a[5])
    i+=1'''

#reverse of string

'''a='barca'
i=0
l=len(a)
b=a[::-1]
while i<l:
    print(b[i])
    i+=1'''

#reverse of a number

'''a=int(input("Enter a number: "))
rev=0
while a>0:
    d=a%10
    rev=rev*10+d
    a//=10
    print('rev',rev)'''

#fibonnaci series

num=int(input("Enter the limit: "))
a=0
b=1
i=0
while i<num:
    print(a)
    c=a+b
    a=b
    b=c
    i+=1 







    

