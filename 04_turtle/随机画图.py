import time
import random
import turtle as t

# def panduan():
#     s = int(time.time())
#     s *= 10 ^ 7
#     s = int(s)
#     s %= 3
#     return s

t.Turtle()
#t.shape('turtle')
t.speed(9)

for i in range(200):
    # a=panduan()
    a = random.randint(0,5)
    if a==0:
        t.lt(120)
    elif a==1:
        t.lt(60)
    elif a==2:
        t.lt(180)
    elif a==3:
        t.rt(60)
    elif a==4:
        t.rt(120)
    t.fd(20)

t.done()
    # time.sleep(0.1)
