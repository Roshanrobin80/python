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

a=int(input("Enter a number: "))
b=1
while b<=10:
    c=a*b
    print(f"{a}*{b}={c}")
    b+=1
