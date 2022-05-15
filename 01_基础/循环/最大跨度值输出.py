# 输出一组数的最大值与最小值的差值
a = input("请输入一串数字来求最大的跨度值（数字间用空格隔开）").split(" ")
b = len(a)
print(a)
for o in range(b):
    if int(a[0]) < int(a[o]):
        a[0], a[o] = a[o], a[0]
for o in range(2, b):
    if int(a[1]) > int(a[o]):
        a[1], a[o] = a[o], a[1]
print("最大跨度值为：" + str(int(a[0]) - int(a[1])))
