#输出n的因子
n = int(input("请输入正整数n来求n的因子:"))
if n<=0:
    print("输入错误")
else:
    for i in range(1,n+1):
        if n % i==0:
            print(i,end=" ")