import turtle
import random
import time
from random import randint
from random import seed

for _ in range(1):
    value = randint(-15, 15)


def fel():
    ypozicio = urhajo.ycor()
    ypozicio += 20
    urhajo.sety(ypozicio)


def le():
    ypozicio = urhajo.ycor()
    ypozicio -= 20
    urhajo.sety(ypozicio)


def jobbra():
    xpozicio = urhajo.xcor()
    xpozicio += 20
    urhajo.setx(xpozicio)


def balra():
    xpozicio = urhajo.xcor()
    xpozicio -= 20
    urhajo.setx(xpozicio)


kijelzo = turtle.Turtle()
kijelzo.hideturtle()

space = turtle.Screen()
space.setup(width=800, height=600)
space.bgpic("hatter.png")
space.addshape("sprite.gif")
space.addshape("meteor2.gif")
space.tracer(0)
space.listen()
space.onkeypress(fel, "Up")
space.onkeypress(le, "Down")
space.onkeypress(balra, "Left")
space.onkeypress(jobbra, "Right")

urhajo = turtle.Turtle()
urhajo.shape("sprite.gif")
urhajo.penup()

meteor_jobbrol = turtle.Turtle()
meteor_jobbrol.shape("meteor2.gif")
meteor_jobbrol.penup()

eletjelzo = turtle.Turtle()
eletjelzo.hideturtle()
eletjelzo.penup()
eletjelzo.color("red")
eletjelzo.setx(-370)
eletjelzo.sety(230)
eletjelzo.write("❤ 3", align="left", font=("Arial", 30, "bold"))

meteor_jobbrol.setx(400)
meteor_jobbrol.sety(value * 20)

szamlalo = 0
robbanas_szamlalo = 0

while meteor_jobbrol.xcor() > -400:
    space.update()
    time.sleep(0.1)
    if urhajo.xcor() == meteor_jobbrol.xcor()-60 and urhajo.ycor() == meteor_jobbrol.ycor():
        robbanas_szamlalo += 1
        meteor_jobbrol.setx(-450)
        szamlalo -= 1
        eletjelzo.clear()
        eletjelzo.write(f'❤ {3 - robbanas_szamlalo}', align="left", font=("Arial", 30, "bold"))
    if urhajo.ycor() > 300:
        urhajo.sety(-300)
    if urhajo.ycor() < -300:
        urhajo.sety(300)
    if urhajo.xcor() > 400:
        urhajo.setx(-400)
    if urhajo.xcor() < -400:
        urhajo.setx(400)
    meteor_mozgas = meteor_jobbrol.xcor()
    meteor_mozgas -= 20
    meteor_jobbrol.setx(meteor_mozgas)

while meteor_jobbrol.xcor() <= -400:
    szamlalo += 1
    kijelzo.clear()
    kijelzo.write(szamlalo, align="center", font=("Arial", 30, "bold"))
    for _ in range(1):
        value = randint(-15, 15)
    meteor_jobbrol.setx(400)
    meteor_jobbrol.sety(value * 20)
    while meteor_jobbrol.xcor() > -400 and robbanas_szamlalo != 3:
        space.update()
        time.sleep(0.1)
        if urhajo.xcor() == meteor_jobbrol.xcor()-60 and urhajo.ycor() == meteor_jobbrol.ycor():
            robbanas_szamlalo += 1
            meteor_jobbrol.setx(-450)
            szamlalo -= 1
            eletjelzo.clear()
            eletjelzo.write(f'❤ {3 - robbanas_szamlalo}', align="left", font=("Arial", 30, "bold"))
        if urhajo.ycor() > 300:
            urhajo.sety(-300)
        if urhajo.ycor() < -300:
            urhajo.sety(300)
        if urhajo.xcor() > 400:
            urhajo.setx(-400)
        if urhajo.xcor() < -400:
            urhajo.setx(400)
        meteor_mozgas = meteor_jobbrol.xcor()
        meteor_mozgas -= 20
        meteor_jobbrol.setx(meteor_mozgas)
    if robbanas_szamlalo == 3:
        space.clear()
        kijelzo.clear()
        meteor_jobbrol.clear()
        urhajo.clear()
        space.bgcolor("black")
        while True:
            kijelzo.color("white")
            kijelzo.write(f'MEGHALTÁL! PONTSZÁM: {szamlalo + 1}', align="center", font=("Arial", 30, "bold"))
# CREATED BY VIKI, PATRIK & MARTIN