# Nested if

a=int(input("1st number: "))
b=int(input("2nd number: "))
c=int(input("3rd number: "))
if a>b:
    if a>c:
        print("1st number is big")
    else:
        print("3rd number is big")
else:
    if b>c:
        print("2nd number is big")
    else:
        print("3rd number is big")


