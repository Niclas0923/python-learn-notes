s = input("请输入一串数字用空格隔开从大到小进行排序").split(" ")
zongshu = len(s)
for i in range(zongshu-1):
	for o in range(i,zongshu):
		if float(s[i])>float(s[o]):
			s[i],s[o]=s[o],s[i]
for i in range(zongshu):
	print(s[i],end=" ")
