# 输入几个数求和
a = input("输入几个数求和，用空格隔开\n").split(" ")
s = 0
for i in a:
    s += float(i)
print("计算结果为："+str(s))
