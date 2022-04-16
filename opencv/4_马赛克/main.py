import cv2
import numpy as np

def msk(a):
    # a2 = cv2.resize(a,(24,36))
    a2 = a[::10,::10] # 每10*10个像素取一个
    a21 = np.repeat(a2,10,axis=0)           # 重复行
    a3 = np.repeat(a21,10,axis=1)           # 重复列
    return a3
   


def facemsk(a):
    # 人脸左上角是90，70    右下角是150，135
    face = a[70:135,90:150]
    face1 = face[::5,::5]
    face2 = np.repeat(face1,5,axis=0)           # 重复行
    face3 = np.repeat(face2,5,axis=1)           # 重复列
    # 此处正好可以直接接入，若不同则需裁切:face3 = face3[:15,:20]
    a[70:135,90:150] = face3
    return a


def main():
    tupian = cv2.imread("4_马赛克/WJG.jpg")
    # 输入照片(360, 236)

    tupian = facemsk(tupian)
    
    cv2.imshow("test",tupian)               # 显示照片
    cv2.waitKey()                           # 等待键盘输入，有输入就关闭窗口
    cv2.destroyAllWindows() 
    

if __name__ == "__main__":
    main()
