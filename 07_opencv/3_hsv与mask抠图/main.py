import cv2
import numpy as np

# 图片转换为hsv
def hsv(o):
    a = cv2.cvtColor(o,code = cv2.COLOR_BGR2HSV)    # 转换为hsv颜色模型，色调饱和度和亮度
    # a=o  # 可以看出不进行hsv变换就不能进行提取
    # 定义在hsv空间中蓝色的范围
    lower_blue = np.array([110,90,90])            # 这里的数值已经经过测试优化了
    upper_blue = np.array([217,255,255])
    
    b = cv2.inRange(a, lower_blue, upper_blue)
    # 根据定义的蓝色范围标记图片
    # inRange 判断你是否在这个范围内
    # 在就标记成0(白)，不在就标记成255(黑)
    
    c = cv2.bitwise_and(o,o, mask= b)     #仅取蓝色范围的图像
    # cv2.bitwise_and(a,b)(省略了mask=nein)表示：
    # a与b进行二进制“与”运算（不同返回0，相同返回原值）

    # cv2.bitwise_and(a,b,mask=c)表示：
    # 若mask处为1则只进行与运算     若mask处为0则直接填充0     
    # 相当于只算面具展示出来的部分的与运算
    # 面具包裹的(0处)则直接不计算，直接展示为0(黑色部分)
    return a,b,c

def main():
    tupian = cv2.imread('3_hsv与mask抠图/wenzi01.png')
    
    (a,b,c)=hsv(tupian)

    # 黑转白
    for i in range(c.shape[0]):
        for j in range(c.shape[1]):
            if (c[i,j]==0).all():
                c[i,j]=255
    

    cv2.imshow("01",tupian)
    cv2.imshow("02",a)
    cv2.imshow("03",b)
    cv2.imshow("04",c)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ =="__main__":
    main()