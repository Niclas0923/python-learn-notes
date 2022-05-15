s = input("请输入一串数字用空格隔开从大到小进行排序").split(" ")
sun = len(s)
for i in range(sun-1):
	for o in range(i, sun):
		if float(s[i]) > float(s[o]):
			s[i], s[o] = s[o], s[i]
for i in range(sun):
	print(s[i], end=" ")
