from turtle import *
oyna=Screen()
oyna.bgcolor('black')
qal=Turtle()
qal.speed(100)
qal.pensize(20)
qal.up()
for i in range(4):
	qal.up()
	if i==1:
		qal.goto(-5,5)
		qal.color('cyan')
	elif i==2:
		qal.goto(5,-5)
		qal.color('red')
	elif i==3:
		qal.goto(0,0)
		qal.color('white')
	else:
		continue
	qal.down()
	qal.left(180)
	qal.circle(45,270,90)
	qal.speed(100)
	qal.forward(145)
	qal.left(180)
	qal.circle(64,90,90)
oyna.mainloop()
