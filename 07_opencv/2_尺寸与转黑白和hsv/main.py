import cv2
import numpy as np

# 更改尺寸，直接拉长
def chicun(b):
    a = cv2.resize(b,(1000,1778))   # 变为2倍，等量变大,改变图片尺寸
    cv2.imshow("rose",a)

# 图片转换为黑白
def heibai(b):
    a = cv2.cvtColor(b,code = cv2.COLOR_BGR2GRAY)   # 转换为黑白图片，灰度化处理
    cv2.imshow("rose02",a)

# 图片转换为hsv
def hsv(o):
    a = cv2.cvtColor(o,code = cv2.COLOR_BGR2HSV)    # 转换为hsv颜色模型，色调饱和度和亮度
    cv2.imshow("rose03",a)

def main():
    tupian = cv2.imread('2_尺寸与转黑白和hsv/wenzi01.png')
    
    hsv(tupian)          #更改这个函数的名称来实现不同功能
    
    cv2.waitKey(0)  # 0代表一直等待，5000代表5s
    cv2.destroyAllWindows()

if __name__ =="__main__":
    main()