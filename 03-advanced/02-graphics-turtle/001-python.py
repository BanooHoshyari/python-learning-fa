
import turtle
import time
from math import sin, cos, radians

window = turtle.Screen()
window.title("ساعت ساده")

# قلم برای رسم دایره ساعت
pen1 = turtle.Turtle()
pen1.shape('turtle')
pen1.speed(0)
pen1.penup()
pen1.goto(0, -100)
pen1.pendown()
pen1.circle(100)

# قلم برای نقطه مرکز
pen2 = turtle.Turtle()
pen2.speed(0)
pen2.penup()
pen2.goto(0, 0)
pen2.dot(15)

# قلم برای عقربه
pen3 = turtle.Turtle()
pen3.speed(0)
pen3.penup()
pen3.color("red")

r = 80
theta = 0

while True:
    x = r * sin(radians(theta))
    y = r * cos(radians(theta))
    pen3.goto(x, y)
    time.sleep(0.1)   # سرعت حرکت عقربه
    theta += 6        # هر ۶ درجه = ۱ ثانیه (تقریباً)
    
    if theta >= 360:
        theta = 0

window.mainloop()
