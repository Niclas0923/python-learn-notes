import cv2
import numpy as np

def turnhsv(o):
    a = cv2.cvtColor(o,code = cv2.COLOR_BGR2HSV)
    return a
# 手工绘制
def shou(o):
    h,w,c = o.shape
    mask = np.zeros((h, w), dtype=np.uint8)
    # 手动标点获取的数据，类似ps里面的铰链工具
    x_data = np.array([80, 256, 616, 816, 790, 456, 286, 158, 131])+10   # 横坐标
    y_data = np.array([394,170, 107, 258, 477, 819, 801, 744, 584])+10   # 纵坐标
    # pts = np.vstack((x_data, y_data)).astype(np.uint8).T     # vstack是数值上的及联
    pts = np.c_[x_data,y_data]                              # 与上一行输出相同
    cv2.fillPoly(mask, [pts], (255),8,0)
    return mask

# 自动绘制
def auto(a):
    hsv = turnhsv(a)
    lower_red = np.array([100,0,0]);upper_red = np.array([220,255,255]) # 浅红色和深红色
    mask = cv2.inRange(hsv,lower_red,upper_red)     # 获取面具
    return mask

def main():
    hua = cv2.imread('7_轮廓/hua.png')
    
    mask = auto(hua)
    hua1 = cv2.bitwise_and(hua,hua,mask=mask)
    

    # cv2.imwrite("test.png",hua1)
    cv2.imshow("test",hua1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ =="__main__":
    main()