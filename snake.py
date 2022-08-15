import turtle
import time
import random 

hiz = 0.10
pencere = turtle.Screen()
pencere.title('Yılan Oyunu')
pencere.bgcolor('lightgreen')
pencere.setup(width=600,height=600)
pencere.tracer(0)



kafa = turtle.Turtle()
kafa.speed(0)
kafa.shape('square')
kafa.color('black')
kafa.penup()
kafa.goto(0,100)
kafa.direction = 'stop'

yem = turtle.Turtle()
yem.speed(0)
yem.shape('circle')
yem.color('red')
yem.penup()
yem.goto(0,0)
yem.shapesize(0.80,0.80)




point1 = (0, 290)
point2 = (290, 290)
point3 = (290,-290) 
point4 = (-290,-290)
point5 = (-290,290)  
point6 = (0,290) 

turtle.shapesize(0.01,0.01)
turtle.width(3)
turtle.color('blue')
turtle.penup()
turtle.goto(point1)
turtle.pendown()
turtle.goto(point2)
turtle.pendown()
turtle.goto(point3)
turtle.pendown()
turtle.goto(point4)
turtle.pendown()
turtle.goto(point5)
turtle.pendown()
turtle.goto(point6)


kuyruklar=[]
puan = 0
yaz = turtle.Turtle()
yaz.speed(0)
yaz.shape('square')
yaz.color('white')
yaz.penup()
yaz.goto(0,260)
yaz.hideturtle()
yaz.write('Puan : {}' .format(puan),align='center', font=('Courier', 24,'normal'))


def move():
    if kafa.direction == 'up':
        y = kafa.ycor()
        kafa.sety(y+20)
    if kafa.direction == 'down':
        y = kafa.ycor()
        kafa.sety(y-20)
    if kafa.direction == 'right':
        x = kafa.xcor()
        kafa.setx(x+20)
    if kafa.direction == 'left':
        x = kafa.xcor()
        kafa.setx(x-20)

def goUp():
    if kafa.direction != 'down':
        kafa.direction = 'up'

def goDown():
    if kafa.direction != 'up':
        kafa.direction = 'down'

def goRight():
    if kafa.direction != 'left':
        kafa.direction = 'right'

def goLeft():
    if kafa.direction != 'right':
        kafa.direction = 'left'

pencere.listen()
pencere.onkey(goUp, 'Up')
pencere.onkey(goDown, 'Down')
pencere.onkey(goRight, 'Right')
pencere.onkey(goLeft, 'Left')



    



while True:
    pencere.update()
    
    if kafa.xcor() > 291 or kafa.xcor() < -291 or kafa.ycor() > 291 or kafa.ycor() < -291:
        time.sleep(1)
        kafa.goto(0, 0)
        kafa.direction = 'stop'


        for kuyruk in kuyruklar:
            kuyruk.goto(1000,1000)
            kuyruklar= []
            puan = 0
            yaz.clear()
            yaz.write('Puan : {}' .format(puan),align='center', font=('Courier', 24,'normal'))
            
        hiz = 0.15
        

        
    if kafa.distance(yem) < 20:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        yem.goto(x,y)

        puan = puan +1
        yaz.clear()
        yaz.write('Puan : {}' .format(puan),align='center', font=('Courier', 24,'normal'))


        yeniKuyruk=turtle.Turtle()
        yeniKuyruk.speed(0)
        yeniKuyruk.shape('square')
        yeniKuyruk.color('white')
        yeniKuyruk.penup()
        kuyruklar.append(yeniKuyruk)

    for i in range(len(kuyruklar) -1,0,-1):
        x = kuyruklar[i - 1].xcor()
        y = kuyruklar[i - 1].ycor()
        kuyruklar[i].goto(x,y)
        
    if len(kuyruklar) > 0:
        x = kafa.xcor()
        y = kafa.ycor()
        kuyruklar[0].goto(x,y)
    
    move()
    time.sleep(hiz)

