import numpy as np

def main():
    ary = np.array([1,2,3,4,5,6])
    # ary = np.arange(1,7,1)    # 起始值，终止值，步长  起始值默认为0，步长默认为1
    # print(ary,type(ary))      # [1 2 3 4 5 6] <class 'numpy.ndarray'>
    # print(ary.dtype)          # 数据类型 int64
    # 转换数据类型,把ary内的数据当作浮点型
    # print(ary.astype("float64").dtype) # float64


    # print(ary.tolist())       # [1, 2, 3, 4, 5, 6]  # 转换为列表

    # print(ary.shape)          # 维度   (6,)
    # print(ary.ndim)           # 维度    1
    # print(ary.size)           # 元素的个数 6
    # print(ary[1])             # 2
    # ary.shape = (2,3)           # 维度改为两行三列
    # print(ary,ary.shape)        #  [[1 2 3]
                                  #   [4 5 6]] (2, 3)
    

    # a1 = np.zeros(3,dtype='float64')     # [0. 0. 0.]  #浮点型
    # a2 = np.ones(3,dtype='int64')        # [1 1 1]  #整形
    # b = np.zeros_like(a1)            # [0. 0. 0.]   #生成维度与a一样的b
    # print(a1)
    # print(b)


    # 运算
    # print(ary)      # [1 2 3 4 5 6]
    # print(ary*3)    # [ 3  6  9 12 15 18]
    # print(ary>3)    # [False False False  True  True  True]


    # len与size的区别
    # ary = np.array([[1,2],[2,2]])
    # print(len(ary))     # 2 最外层数组中包含的元素数量
    # print(ary.size)     # 4 元素个数
    

    # 索引
    # ary = np.arange(1,19)
    # ary.shape = (3,2,3)
    # print(ary[0][1][0])     # 4
    # print(ary[0,1,0])       # 4
    

    # 第一种设置detype的方法
    # ary=[('zs',[11,12,12],13)]
    # a = np.array(ary,dtype='U2,3int64,int64')  # U2表示u字符出现两次
    # print(a)        # [('zs', [11, 12, 12], 13)]

    # 第二种，不推荐
    # a = np.array(ary,dtype=[('name','str',2),
    #                         ('scores','int64',3),
    #                         ('age','int64',1)])
    # print(a[0]['age'])          # 13

    # 第三种
    # a = np.array(ary,dtype={'names':['name','scores','ages'],
    # 'formats':['U3','3int64','int64']})
    # print(a[0]['ages'])

    # 第四种
    

    # print(a)




if __name__=="__main__":
    main()