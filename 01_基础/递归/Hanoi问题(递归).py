import time


def ss(i, x, y, z):
    s = "-->"
    if i == 1:
        print(x + s + z, end=" ")
    else:
        ss(i - 1, x, z, y)
        print(x + s + z, end=" ")
        ss(i - 1, y, x, z)


n = int(input("请输入个数"))

a = time.time()
ss(n, "A", "B", "C")
b = time.time()
c = b - a
print("\n总共用时", c)
