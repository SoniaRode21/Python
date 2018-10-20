from turtle import *;
import math ;

canvas = Screen();
t = Turtle();
t.speed(10);
canvas.bgcolor("#6E7289");
width=int(input("Enter the width of the letters :"));

height=2*width;

def main():
    canvas.reset();
    canvas.setworldcoordinates(0, 0, 1000, 1000);
    t.penup();
    t.goto(50,500);
    drawS();
    space();
    drawO();
    space();
    drawN();
    space();
    drawI();
    space();
    drawA();
    space();
    space();
    drawR();
    spaceR();
    drawO();
    space();
    drawD();
    space();
    drawE();

    canvas.exitonclick();





def drawS():
    t.pendown();
    t.forward(width/2);
    t.circle(width/2, 180);
    t.left(180);
    t.circle(width/2,-180);
    t.backward(width/2);
    t.penup();
    t.left(90);
    t.forward(height);
    t.right(90);
    t.forward(width);
    t.left(180);


    #t.goto(x,y);

def space() :

    t.forward(width+30);

def spaceR() :
    t.forward(width+10);

def drawO() :
    t.pendown();
    t.forward(width);
    t.left(90);
    t.forward(width*2);
    t.left(90);
    t.forward(width);
    t.left(90);
    t.forward(width*2);
    t.penup();
    t.left(90);

def drawN( ) :
    t.pendown();
    t.left(90);
    t.forward(height);
    t.right(155);
    t.forward(width*2.24);
    t.left(155);
    t.forward(height);
    t.penup();
    t.left(155);
    t.forward(width*2.24);
    t.left(115);


def drawI() :
    t.pendown()
    t.forward(width);
    t.backward(width/2);
    t.left(90);
    t.forward(height);
    t.left(90);
    t.forward(width/2);
    t.backward(width);
    t.penup();
    t.forward(width/2);
    t.left(90);
    t.forward(height);
    t.right(90);
    t.forward(width/2);
    t.left(180);

def drawA() :
    t.left(90);
    t.pendown();
    t.forward(height);
    t.right(90);
    t.forward(width);
    t.right(90);
    t.forward(height);
    t.backward(height/2);
    t.right(90);
    t.forward(width);
    t.left(90);
    t.forward(height/2);
    t.left(90);
    t.penup();

def drawR() :
    t.left(90);
    t.pendown();
    t.forward(height);
    t.left(90);
    t.circle(width/2+10,-180);
    t.right(45);
    t.forward(((height/2)-20)*1.41);
    t.penup();
    t.left(225);
    t.forward((height/2)-20);
    t.left(180);


def drawD() :
    t.pendown();
    t.left(90);
    t.forward(height);
    t.left(90);
    t.circle(height/2,-180);
    t.penup();

def drawE() :
    t.pendown();
    t.forward(width);
    t.backward(width);
    t.left(90);
    t.forward(height);
    t.right(90);
    t.forward(width);
    t.backward(width);
    t.right(90);
    t.forward(height/2);
    t.left(90);
    t.forward(width);
    t.backward(width);
    t.right(90);
    t.forward(height/2);
    t.left(90);

main();