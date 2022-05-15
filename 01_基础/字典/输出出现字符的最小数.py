# s = input("请输入:").split(" ")

s = 'Diese schöne Seite von Liebesbeziehungen und die damit verbundenen Gefühle erfahren wir meist'

s = s.lower()

# 写入字典并计数
sun = {}
for i in range(len(s)):
    if s[i] in sun:
        sun[s[i]][0] += 1
    else:
        sun[s[i]] = [1, i]

# if " " in sum :
#     sum = sum.pop(" ")    #不能运行所以注释


o = []
# 转为列表，准备排序
for i in sun.items():
    o.append(i)

# 排序
o.sort(key=lambda x: (x[1][0], x[1][1]))

# #验证用
# for i in range(len(o)):
#     print(o[i][0],o[i][1][0])

print(o[0][0], o[0][1][0])
