import turtle
import math
import random

def trees( noOfTrees,house) :
    wood=0;
    #To randomly call tree functions
    while noOfTrees>0 :

        #store wood from each tree
        wood+=random.choice(treesArray)()

        #If the user wants a house
        if house=='y' or house=='Y':
            space()
            wallLength=100
            drawHouse(wallLength)
            wood+=(2*wallLength+ 2*(math.sqrt((wallLength/2)**2 + (wallLength/2)**2)))
            house='N'

        noOfTrees=noOfTrees-1
    return wood

def pine() :
    space()
    length=random.randint(50,150)
    drawTrunk(length)
    drawTriangle()
    drawTrunk(length)
    turtle.left(180)
    return length

def maple() :
    space()
    length = random.randint(50, 200)
    drawTrunk(length)
    drawCircle()
    drawTrunk(length)
    turtle.left(180)
    return length

def other():
    space()
    length = random.randint(50, 200)
    drawTrunk(length)
    drawCircle()
    turtle.right(180)
    drawCircle()
    turtle.right(180)
    drawCircle()
    drawTrunk(length)
    turtle.left(180)
    return length

def drawTrunk( length) :
    turtle.left(90)
    turtle.forward(length)
    turtle.right(90)
    return

def drawTriangle() :
    triangleSide=random.randint(20,50)
    turtle.forward(triangleSide/2)
    for i in range(0,3) :
        turtle.left(120)
        turtle.forward(triangleSide)
    turtle.backward(triangleSide/2)
    turtle.left(180)
    return

def drawCircle() :
    radius=random.randint(10,30)
    turtle.circle(radius)
    turtle.left(180)
    return

def space() :

    turtle.forward(random.randint(60,70))
    return

def drawHouse( length ) :

        turtle.forward(length)
        turtle.left(90)
        turtle.forward(length)
        turtle.left(45)
        turtle.forward(math.sqrt((length/2)**2 + (length/2)**2))
        turtle.left(90)
        turtle.forward(math.sqrt((length/2)**2 + (length/2)**2))
        turtle.left(45)
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(length)
        return



def day(wallWood) :

    drawHouse(wallWood)
    drawSun(wallWood)

def drawSun(wallWood) :

    turtle.up()
    turtle.left(90)
    turtle.forward(2*wallWood)
    turtle.down()
    turtle.circle(random.randint(20,30))

def setWidow() :
    turtle.penup()
    turtle.setposition(-250, -200)
    turtle.down()

#List to store tree functions
treesArray=[pine,maple,other]

def main() :

    noOfTrees = int(input("Enter the number of trees in your forest"))
    house=input("Is there a house in the forest (Y/N) ? ")
    setWidow()
    #function to draw night scene
    totalWood=trees(noOfTrees,house)

    input("Night is done, press enter for day")

    print("We have ",totalWood ,"units of lumber for building")
    wallWood=totalWood*((2-math.sqrt(2))/2)
    print("We will build a house with walls ",wallWood," tall.")
    turtle.reset()
    setWidow()
    day(wallWood)


    turtle.mainloop()



main()