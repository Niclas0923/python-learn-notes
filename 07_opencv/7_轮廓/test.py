import cv2 as cv

def mmm (src):
    grad_x = cv.Scharr(src, cv.CV_32F, 1, 0) # 增强版（Sobel）图像
    grad_y = cv.Scharr(src, cv.CV_32F, 0, 1)
    gradx = cv.convertScaleAbs(grad_x) # 转变
    grady = cv.convertScaleAbs(grad_y)
    gradxy = cv.addWeighted(gradx, 1, grady, 2, 0)
    #cv.imshow(“gradient”, gradxy)
    gradxy = cv.blur(gradxy, (3, 3))
    gradxy = cv.blur(gradxy, (3, 3))
    gradxy = cv.GaussianBlur(gradxy, (7, 7), 0)
    gradxy = cv.blur(gradxy, (3, 3))
    gradxy = cv.cvtColor(gradxy, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gradxy, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    binary = cv.GaussianBlur(binary, (7, 7), 0)
    binary = cv.blur(binary, (3, 3))
    #cv.imshow("binary image", binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (40, 40))
    binary1 = cv.morphologyEx(binary, cv.MORPH_CLOSE, kernel)
    binary2 = cv.morphologyEx(binary, cv.MORPH_CLOSE, kernel)
    #cv.imshow("close_op", binary1)

    cloneImage, contours = cv.findContours(binary2, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    area = []
    are = 0
    for j,i in enumerate (range(len(contours))):
        are = cv.contourArea(contours[i])
        area.append(are)
    i = area.index(max(area))
    contours =max(area)

    dst333=cv.drawContours(src, contours, i, (0, 0, 255), 2)
    cv.imshow('dst',dst333)
    detyyy=dst333
    return detyyy

goutou = cv.imread("7_轮廓/goutou.jpeg")

goutouk = mmm(goutou)

cv.imshow("goutou",goutouk)
cv.waitKey()
cv.destroyAllWindows()