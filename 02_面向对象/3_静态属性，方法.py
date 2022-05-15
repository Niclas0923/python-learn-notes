class employee:
    totalsalary = 0  # 声明全局变量

    def __init__(self, name, income):
        self.name, self.income = name, income

    def pay(self, salary):
        self.income += salary
        employee.totalsalary += salary

    def printall(self):
        print("name:", self.name)
        print("incom:", self.income)

    @staticmethod  # 声明全局函数
    def printtotalsalary():
        print(employee.totalsalary)


e1 = employee("ooo", 0)
e2 = employee("lll", 0)
e1.pay(100)
e2.pay(200)
employee.printtotalsalary()
print(e1.income)
e1.printall()
