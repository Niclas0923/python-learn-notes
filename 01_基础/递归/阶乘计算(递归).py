a = int(input("请输入要求几的阶乘："))
s = [1] * a
for i in range(1, a):
    s[i] = s[i - 1] * (i + 1)
print(str(a) + "的阶乘是" + str(s[a - 1]))
