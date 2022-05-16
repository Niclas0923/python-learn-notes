import time


# 获取当前时间并分类，预备分情况休眠
def getob():
    s = int(time.strftime("%H", time.localtime()))
    if s > 21 or s < 9:
        if s > 21:
            ob1 = [1, 24 - s + 9]
        else:
            ob1 = [1, 9 - s]
    else:
        ob1 = [0, (21 - s) * 10]
    return ob1  # ob = [类型:1是夜间2是日常,持续小时数]


m = int(time.time())
ob = getob()
while 1:

    n = int(time.time())
    n = n - m
    if n > 6:
        break
        # 逻辑判断休眠时间并迭代ob
    if ob[0] == 1:
        ob[1] -= 1  # 小时数减1
        if ob[1] == 0:  # 减完转为日常
            ob = [0, 120]
        print(ob)
        time.sleep(0.1)

    else:
        ob[1] = ob[1] - 1  # 小时数0.1
        if ob[1] == 0:  # 减完转为夜间
            ob = [1, 12]
        print(ob)
        time.sleep(0.01)
