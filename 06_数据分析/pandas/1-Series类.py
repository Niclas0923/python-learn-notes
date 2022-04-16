import pandas as pd

def main():
    
    s = pd.Series(data=[80,90,100],index=['语文','数学','英语'])

    for i in s:
        print(i,end=" ")                   # 80 90 100
    print(" ")

    # 角标也可以访问元素
    print(s['语文'],s[1])                   # 80 90

    # 角标获取
    for i in range(len(s.index)):          # 语文 数学 英语
        print(s.index[i],end=' ')
    print(" ")

    # 切片应用
    print(s[0:2]['数学'])                   # 90
    print(s['数学':'英语'][1])              # 100

    # 元素增删
    s['体育'] = 110         # 在尾部增加
    s.pop('数学')           # 删除标签为数学的元素
    # 在尾部添加返回新的series类，但不改变s
    s2 = s.append(pd.Series(120,index=["政治"]))
    print(list(s2))                        # [80, 100, 110, 120]
    print(list(s))                         # [80, 100, 110]

    # 基础运算
    # 和 最小值 均值 中位数
    print(s.sum(),s.min(),s.mean(),s.median())
    # 290 80 96.66666666666667 100.0
    # 最大元素的标签和下标
    print(s.idxmax(),s.argmax())           # 体育 2


if __name__ == "__main__":
    main()