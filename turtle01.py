import turtle
import math
#스크린 생성
s=turtle.getscreen()

#거북이 변수 지정
t=turtle.Turtle()

t.shape("turtle")
t.speed(1)
#장애물 만들기
t.penup()
t.fd(50)
t.pendown()
t.rt(90)
t.fd(50)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(50)
#출발점으로이동
t.penup()
t.rt(90)
t.fd(50)
t.lt(45)
t.fd(200)
#출발점 좌표
a=t.pos()
print(a)
t.pendown()

t.rt(180)
t.fd(100)
t.lt(45)
t.fd(150)
t.rt(90)
t.fd(150)
t.lt(45)


print(b)
while True:
    b=t.pos()
    
    if b[0]>=150.00 or b[1]>=150.00:
        print("도착했습니다")
        break
        
    t.fd(1)

    
def cal_distance(a,b):
    x1, y1 = a
    x2, y2 = b
    distance = math.sqrt((x2-x1)**2+(y2-y1)**2)
    return distance

print(cal_distance(a,b))
