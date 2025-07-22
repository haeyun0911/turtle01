import turtle
import math
#스크린 생성
s=turtle.getscreen()

#거북이 변수 지정
t=turtle.Turtle()

t.shape("turtle")
#장애물 중심좌표
obs=t.pos()
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
t.rt(180)

t.pendown()

def check_collision(a,obs):
    robot_x,robot_y=a
    obs_x,obs_y=obs
    for obs_x,obs_y,radius in obstacles:
        collision_distance=distance(robot_x,robot_y,obs_x,obs_y)
        if collision_distance <= radius + 10:
            print("충돌")
            return True
        
    return False
while True:
    a=t.pos()
    check_collision(a,obs)
    t.fd(1)

def distance(x1,y1,x2,y2):
    return math.sqrt((x2-x1)**2+(y2-y1)**2)
'''
t.fd(100)
t.lt(45)
t.fd(150)
t.rt(90)
t.fd(150)
t.lt(45)
'''