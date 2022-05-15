class Rectangle:
    def __init__(self, w, h):
        self.w, self.h = w, h

    def area(self):
        return self.w * self.h


# 基础信息，设置一个类
def main1():
    d = Rectangle(2, 3)
    print(d.area())
    d.h = 12
    d.w = 3
    print(d.area())


class PoInt:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return "(%d,%d)" % (self.x, self.y)


# 对类进行一个比较，转字符串
def main2():
    a = PoInt(1, 2)
    b = PoInt(1, 2)
    c = PoInt(2, 3)
    print(a.__eq__(b))
    print(a.__eq__(c))
    print(a == b)  # 若在class里面已经定义，则可以直接使用==,<,>等
    print(str(a))


if __name__ == "__main__":
    main1()
    main2()
