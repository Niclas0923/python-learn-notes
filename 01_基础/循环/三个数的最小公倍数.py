# 求三个数的最小公倍数
a, b, c = map(lambda ss: int(ss),
              input("请输入三个数来求他们的最小公倍数，用空格隔开\n").split(' '))
i, n = 1, 1
while i % a != 0 or i % b != 0 or i % c != 0:
    i += 1
print("%d,%d,%d的最小公倍数是%d" % (a, b, c, i))
