'''class syn:
    def python():
        print('python prg')
    def java():
        print('java prg')
    def php():
        print('php prg')
manu=syn
manu.python()
akhil=syn
akhil.php() '''


class Bank:
    def __init__(s):
        s.name=input('Name: ')
        s.age=int(input('Age: '))
        s.bal=0

    def deposit(self,amt):
        self.bal+=amt
        print('deposit')
    def withdraw(self,amt):
        self.bal-=amt
        print('withdraw')
    def balance(self):
        print('balance',self.bal)

obj=Bank()
obj.deposit(5000)
obj.balance()
obj.withdraw(2000)
obj.balance()
print(obj.bal)

obj1=Bank()
obj1.deposit(1000)
obj1.balance()

