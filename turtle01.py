import turtle

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
#경로표시 일시해제
#t.pendown()

t.rt(180)
t.fd(100)
t.lt(45)
t.fd(150)
t.rt(90)
t.fd(150)
t.lt(45)
t.fd(100)