import cv2
import numpy as np

# 返回马赛克处理后的图片
def msk(a):
    ass = a[::15,::15]
    ass1 = np.repeat(ass,15,axis=0)            # 重复行(轴1)
    b = np.repeat(ass1,15,axis=1)              # 重复列(轴2)
    return b

# 返回人脸的坐标的图表
def return_face(a):
    # 人脸特征的详细说明    仅正面人脸
    face_detector = cv2.CascadeClassifier("5_检测人脸/haarcascade_frontalface_alt.xml")
    # 变为黑白，提高成功率
    a1=cv2.cvtColor(a,code=cv2.COLOR_BGR2GRAY)
    # 返回值为坐标x,y和长度宽度w,h
    faces = face_detector.detectMultiScale(a1,
    scaleFactor=1.3,            # 缩放大小，默认1.1   越小要求越低，检测的更多，计算量更大
    minNeighbors=4,             # 邻居个数，默认3
    minSize=(150,150),          # 最小的尺寸
    )
    return faces

def main():
    # tupian = cv2.imread("5_检测人脸/hulan.jpg")
    tupian = cv2.imread("5_检测人脸/heying.jpg")
    # 输入照片(360, 236)
    tupianm = msk(tupian)

    faces = return_face(tupian)

    # 替换人脸的部分为马赛克后的人脸
    for x,y,w,h in faces:
        tupian[y:y+h,x:x+w] = tupianm[y:y+h,x:x+w]
    cv2.imshow("msk face",tupian)           # 显示照片
    cv2.waitKey(0)                          # 等待键盘输入，有输入就关闭窗口
    cv2.destroyAllWindows() 
    

if __name__ == "__main__":
    main()