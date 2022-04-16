import re

m1 = r"\d{10}|[^一-鿆][一-鿆]{2,3}[^一-鿆]"   # 学号和名字(不过好像没用上。。。)
m2 = r'[^\d\()](\d{10})[^\d].*[^-:\'\d](\d{1,2})[^:\d]'   # 学号和做题数量
m3 = r'\(-(\d+)\)'       # 这个最后法相是没有任何意义的，所有也废弃了
m4 = r'[^\d\()](\d{10})[^\d]'  # 仅学号
m5 = r'[^一-鿆]([一-鿆]{2,3})[^一-鿆]' # 仅姓名
m6 = r'[^一-鿆]([一-鿆]{2,3})[^一-鿆].*[^-:\'\d](\d{1,2})[^:\d]' # 姓名和做题量

# 返回一个学号和姓名的列表，其中每项类似：['1700942085', '钬叟玦']
def duid():
    ss = []
    while 1:
            s = open("id.txt","r",encoding="utf8")
            a = s.read()
            if a in ss:
                break
            else:
                ss.append(a)
            
    s.close()
    s = ss[0].split("\n")
    s=s[:-1]
    o = []              # 存储着学生学号和学生姓名
    for i in s:
        o.append(i.split("\t"))
    return o

# 返回一个学生做题信息的列表，每项类似：['182\t1700942048\t\t0\t0:00:00\t(-9)\t\t\t\t\t\t\t\t\t\t\t']
def duxx():
    ss = []
    while 1:
            s = open("finalscore.txt","r",encoding="utf8")
            a = s.read()
            if a in ss:
                break
            else:
                ss.append(a)
    s.close()
    o = ss[0].split("\n")
    ss = []
    for i in o:
        ss.append([i])
    ss = ss[:-1]
    return ss

# input总数据，在本地输出txt文件
def xieru(a):
    ss = open("XYX.txt","w",encoding="utf8")       #创建文件
    ss.write("学号\t姓名\t题数\t分数\n")
    for i in range(len(a)):
        ss.write(str(a[i][0])+'\t'+str(a[i][1])+"\t"+str(a[i][2])+"\t"+str(a[i][3])+"\n")                       #写入并且增加一个回车
    ss.close()

# 分数计算
def fen(a):
    a = int(a)
    if a ==0:
        return 0
    elif a ==1:
        return 50
    elif a ==2:
        return 60
    elif 2<a:
        return (60+4*(a-2))

# 主函数
def main():

    # 获取仅有学号和姓名的列表来筛选数据，还有对总数据进行一个简单整理
    a = duid()
    id = []; name = [] # 仅记录学号和姓名的列表
    xx = duxx()
    for i in a:
        id.append(i[0])
        name.append(i[1])

    # 这一段是来提取总数据中有学号的部分，筛选出xx1
    xx1 = []
    for i in xx:
        s = i[0]
        lst = re.findall(m4,s)
        if lst==[]:
            pass
        elif lst[0] in id:
            xx1.append([s])

    # 用来筛选仅有名字的部分，在去寻找是否有学号，有就忽略，没有就用in测试，并筛选出xx2
    xx2 = []
    for i in xx:
        s = i[0]
        lst = re.findall(m5,s)
        # print(lst)
        if lst==[]:
            pass
        else:
            a00 = re.findall(m4,s)
            if a00 ==[]:
                if lst[0] in name:
                    xx2.append([s])

    # 制作一个列表ss来收集所有数据，列表的每项为：学号，姓名，做题数，得分
    ss =[]
    # 写入姓名学号
    for i in a:
        ss.append([i[0],i[1],0,0])
    # 写入xx1的数据
    for i in xx1:
        s = i[0]
        lst = re.findall(m2,s)
        # print(lst)                # [('1700944247', '4')]
        aa = lst[0][0]
        ab = lst[0][1]
        ab =fen(ab)
        for o in range(len(ss)):
            if ss[o][0] == aa:
                ss[o][2] = lst[0][1]
                ss[o][3] = ab
                break
    # 写入xx2的数据
    for i in xx2:
        s = i[0]
        lst = re.findall(m6,s)
        # print(lst)                # [('姓名', '4')]
        ao = lst[0][0]
        ab = lst[0][1]
        ab = fen(ab)
        for o in range(len(ss)):
            if ss[o][1] == ao:
                ss[o][2] = lst[0][1]
                ss[o][3] = ab
                break
    # 排序
    ss.sort(key = lambda x:(x[0]))
    # 写入
    xieru(ss)


if __name__ =="__main__":
    main()