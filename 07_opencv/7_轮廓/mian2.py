import cv2
import numpy as np

# canny 轮廓
def ckoutu(a):
    g = cv2.cvtColor(a,code=cv2.COLOR_RGB2GRAY)
    g2 = cv2.GaussianBlur(g,(5,5),2)                # 高斯平滑，高斯模糊
    g3 = cv2.Canny(g2,75,200)                       # 边缘检测
    return g3

# findContours 轮廓
def fkoutu(g):
    cloneImage, contours, heriachy = cv2.findContours(g, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    area = []
    are = 0
    for j,i in enumerate (range(len(contours))):
        are = cv2.contourArea(contours[i])
        area.append(are)
    i = area.index(max(area))
    contours =max(area)
    dst333=cv2.drawContours(g, contours, i, (0, 0, 255), 2)
    cv2.imshow('dst',dst333)
    detyyy=dst333
    return detyyy


def main():
    goutou = cv2.imread("7_轮廓/goutou.jpeg")

    goutouk = fkoutu(goutou)

    cv2.imshow("goutou",goutouk)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__=="__main__":
    main()