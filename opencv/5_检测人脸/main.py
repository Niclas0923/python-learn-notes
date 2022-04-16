import cv2
import numpy as np

# 返回人脸的坐标的图表
def return_face(a):
    # 人脸特征的详细说明    仅正面人脸
    face_detector = cv2.CascadeClassifier("人脸特征数据/haarcascade_frontalface_alt.xml")
    # 变为黑白，提高成功率
    a1=cv2.cvtColor(a,code=cv2.COLOR_BGR2GRAY)
    # 返回值为坐标x,y和长度宽度w,h
    faces = face_detector.detectMultiScale(a1,
    scaleFactor=1.3,            # 缩放大小，默认1.1   越小要求越低，检测的更多，计算量更大
    minNeighbors=4,             # 邻居个数，默认3
    minSize=(150,150),          # 最小的尺寸
    )
    return faces

# 在b上对于人脸的坐标a进行标记
def biaoji(a,b):
    for x,y,w,h in a:
        # cv2.rectangle(tupian,               # 画矩形
        # pt1=(x,y),                          # 坐标1
        # pt2=(x+w,y+h),                      # 坐标2
        # color=[0,0,255],
        # thickness=2
        # )
        b=cv2.circle(b,                     # 画圆形
        center=(x+w//2,y+h//2),             # 圆心
        radius=3*w//5,                      # 半径
        color=[0,255,0],
        thickness=2
        )
    return b



def main():
    # tupian = cv2.imread("5_检测人脸/hulan.jpg")
    tupian = cv2.imread("5_检测人脸/heying.jpg")
    # 输入照片(360, 236)

    faces = return_face(tupian)

    # print(faces)
    
    tupian1 = biaoji(faces,tupian)
    
    cv2.imshow("test",tupian)               # 显示照片
    cv2.imshow("test1",tupian1)
    cv2.waitKey(0)                          # 等待键盘输入，有输入就关闭窗口
    cv2.destroyAllWindows() 
    

if __name__ == "__main__":
    main()