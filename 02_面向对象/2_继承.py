import datetime

# 制造了一个类student
class student:
    def  __init__(self,a,b,c,d):
        self.name = b
        self.id = a
        self.birthyear = c
        self.gender = d
    def print__init__(self):
        print ("name:",self.name)
        print ("id:",self.id)
        print ("birthday:",self.birthyear)
        print ("gender:",self.gender)
        print ("age:",self.age())
    def age(self):
        return datetime.datetime.now().year - self.birthyear

# 以student为基础，继承了其全部内容并增添新内容
class undergraduatestudent(student):
    def __init__(self, id, name, birthyear, gender, department):
        student.__init__(self,id, name, birthyear, gender)
        self.department = department
    def print__init__(self):
        super().print__init__()
        print("department:",self.department)

a = undergraduatestudent(114115,"ooo",2000,"M","jixie")
a.print__init__()

print("")

b = undergraduatestudent(114116,"sss",20002,"M","moshu")
b.print__init__()