# DataFrame是带行列标签的二维表格，每一列都是一个Series

import pandas as pd

def mian():
    # 让表格可以识别中文，输出更加美观
    pd.set_option('display.unicode.east_asian_width',True)

    scores = [['男',108,115,97],["女",115,87,105],['女',100,60,130],['男',112,80,50]]
    names = ['刘一哥','王二姐','张三妹','李四弟']
    courses = ['性别','语文','数学','英语']
    df = pd.DataFrame( data = scores, index = names, columns = courses)
    print(df)

    # 访问
    print(df.values[0][1],type(df.values))      # 108 <class 'numpy.ndarray'>
    print(list(df.index))                       # ['刘一哥', '王二姐', '张三妹', '李四弟']
    print(list(df.columns))                     # ['性别', '语文', '数学', '英语']
    print(df.index[2],df.columns[2])            # 张三妹 数学

if __name__ == "__main__":
    mian()