#求斐波那契数列的第k项
k = int (input("请输入要求斐波那契数列的项数："))
f = [1]*k
for i in range(2,k):
    f[i]=f[i-1]+f[i-2]
print("斐波那契数列的第%d项是%d"%(k,f[k-1]))
