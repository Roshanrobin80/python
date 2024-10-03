'''class school:
    def notes(self,sub):
        print('notes in school',sub)
class std(school):
    def notes(self,sub):
        print('notes in std',sub)
        super().notes(sub)
manu=std()
manu.notes('py')'''

class bank:
    def __init__(self):
        print('add bank details')
class users(bank):
    def __init__(self):
        super().__init__()
        print('add user details')

sbi=bank()
