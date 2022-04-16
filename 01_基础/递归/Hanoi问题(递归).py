import time

def ss(n,x,y,z):
	s="-->"
	if n==1:
		print(x+s+z,end=" ")
	else:
		ss(n-1,x,z,y)
		print(x+s+z,end=" ")
		ss(n-1,y,x,z)
	
n=int(input("请输入个数"))

a=time.time()
ss(n,"A","B","C")
b=time.time()
c=b-a
print("\n总共用时",c)