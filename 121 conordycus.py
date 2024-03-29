# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random

#-----game configuration----
shape = "circle"
size = 3
color ={"green","red","purple","yellow"}
score = 0
font_setup = ("Arial", 20, "normal")
timer = 5
counter_interval = 1000  
timer_up = False

#-----initialize turtle-----
counter =  trtl.Turtle()
counter.penup()
counter.goto(305,275)
counter.ht()

steve = trtl.Turtle(shape = shape)
steve.color(color)
steve.shapesize(size)
steve.speed(0)

point = trtl.Turtle()
point.penup()
point.goto(-385,285)
font = ("Roboto",25,"bold")
point.write(score, font = font)
point.ht()



#-----game functions--------
def turtle_clicked(x,y):
    print("steve was clicked")
    change_position()
    score_counter()

def change_position():
    steve.penup()
    steve.ht()
    new_xpos = random.randint(-400,400)
    new_ypos = random.randint(-300,300)
    steve.goto(new_xpos,new_ypos)
    steve.st()

def score_counter():
    global score
    score += 1
    print(score)
    point.clear()
    point.write(score,font = font)

def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.goto(0,0)
    counter.write("Game Over", font=font_setup)
    timer_up = True
    game_over()

  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval) 

def game_over():
    wn.bgcolor("red")
    steve.ht()



#-----events----------------

steve.onclick(turtle_clicked)



wn = trtl.Screen()
wn.bgcolor("blue")# my customization is to change the background color
wn.ontimer(countdown, counter_interval) 
wn.mainloop()   