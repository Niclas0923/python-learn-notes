import cv2
import numpy as np
import time

# 返回人脸的坐标的图表
def return_face(a):
    # 人脸特征的详细说明    仅正面人脸
    face_detector = cv2.CascadeClassifier("人脸特征数据/haarcascade_frontalface_alt.xml")
    # 变为黑白，提高成功率
    a1=cv2.cvtColor(a,code = cv2.COLOR_BGR2GRAY)
    # 返回值为坐标x,y和长度宽度w,h
    faces = face_detector.detectMultiScale(a1,
    scaleFactor=1.05,            # 缩放大小，默认1.1   越小要求越低，检测的更多，计算量更大
    minNeighbors=3,             # 邻居个数，默认3
    minSize=(120,120),          # 最小的尺寸
    )
    return faces

# 在b上对于人脸的坐标a进行标记并加入c
def biaoji(a,b,c):
    for x,y,w,h in a:
        # ss = time.time()
        star_s = cv2.resize(c,(w,h))
        for i in range(w):
            for j in range(h): 
                if (star_s[i,j]>0).any():
                    b[y+i,x+j]=star_s[i,j]
        # ss1 =time.time()
        # print(ss1-ss)                     # 一个狗头0.5s
    return b

# 对于a进行抠图,返回扣好的图和蒙版
def koutu(a):
    # a = cv2.cvtColor(a,code=cv2.COLOR_BGR2HSV)
    
    lower_red = np.array([0,0,0])
    upper_red = np.array([240,255,255])
    b1 = cv2.inRange(a, lower_red, upper_red)
    b2 = cv2.bitwise_and(a,a, mask= b1) 
    return b2

def main():
    # tupian = cv2.imread("5_检测人脸/hulan.jpg")
    # tupian = cv2.imread("6_人脸贴纸画/WJGLXQ.jpg")
    # tupian = cv2.imread("/Applications/buildier/code/python/learn/opencv/5_检测人脸/heying.jpg")
    tupian = cv2.imread("/Applications/buildier/code/python/learn/opencv/6_人脸贴纸画/sss.png")
    #IMG_1103.HEIC
    goutou = cv2.imread("6_人脸贴纸画/goutou.png")

    goutou = koutu(goutou)
    # print(star)
    # 输入照片(360, 236)
    faces = return_face(tupian)
    tupian = biaoji(faces,tupian,goutou)
    #print(tupian)

    cv2.imshow("输入任意关闭窗口",tupian)       # 显示照片
    cv2.waitKey()                            # 等待键盘输入，有输入就关闭窗口
    cv2.destroyAllWindows() 

if __name__ == "__main__":
    main()