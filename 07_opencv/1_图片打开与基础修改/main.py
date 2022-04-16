import cv2
import numpy as np

# 基础，图像的组成，数据类型和打开
def a1(a):
    print(a.shape) # (3508, 2480, 3)
    print(type(a)) # <class 'numpy.ndarray'>
    print(a)  # 三维数组(彩色图片“高度，宽度，像素rgb”)
    print(" ")

# 图像的弹出和轻度修改
def a2(a):
    cv2.imshow("rose",a)                 # 弹出窗口进行展示
    # cv2.imshow("rose",rose[:,:,::-1])       # 颜色反转  (::-1) 表示反转
    # cv2.imshow("rose",rose[::-1,:,:])       # 高度反转，上下颠倒
    cv2.imshow("rose",a[:,::-1,:])       # 宽度反转，左右镜像
    cv2.waitKey()                           # 等待键盘输入，有输入就关闭窗口
    cv2.destroyAllWindows()                 # 回收内存

def main():
    ranran = cv2.imread("1_图片打开与基础修改/可爱然然.jpeg")
    a1(ranran)
    a2(ranran)


if __name__ == "__main__":
    main()
