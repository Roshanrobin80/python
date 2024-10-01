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


'''class Bank:
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
obj1.balance()'''

# INHERITANCE

#1 single inheritance

'''class syn:
    def python(self):
        self.a=10
        print('python',self.a)
    def php(self):
        print('php')
class novavi(syn):
    def DM(self):
        print('dm works')
    def web_dev(self):
        print('web dev')

novavi_staff=novavi()
novavi_staff.DM()
novavi_staff.python()
std1=syn()
std1.python()'''

#2 multiple inheritance

'''class father:
    def shop(self):
        print('shop')
    def car(self):
        print('car')
class mother:
    def dress_shop(self):
        print('dress shop')
class child(father,mother):
    def bike(self):
        print('bike')
somu=child()
somu.shop()
somu.car()
somu.dress_shop()
somu.bike()
'''

#work-school,tution(parent class) student(child class)

'''class school:
    def maths(self):
        print('maths')
    def physics(self):
        print('physics')
    def malayalam(self):
        print('malayalam')
class tution:
    def chemistry(self):
        print('chemistry')
    def physics_t(self):
        print('physics')
class student(school,tution):
    def sports(self):
        print('sports')
roshan=student()
roshan.maths
roshan.physics()
roshan.malayalam()
roshan.chemistry()
roshan.physics_t()
roshan.sports()'''

#3 multi-level inheritance

class kerala_university:
    def exam(self):
        print('exam')
    def result(self):
        print('result')
class college:
    def notes(self):
        print('notes')
    def labs(self):
        print('labs')
class student(kerala_university,college):
    def uniform(self):
        print('uniform')
sam=student()
sam.exam()
sam.result()
sam.notes()
sam.labs()
sam.uniform()