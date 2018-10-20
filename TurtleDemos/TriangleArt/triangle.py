
import turtle
'''
def triangle(depth,length) :
    if depth==0 :
        pass
    else :
        for i in range(0,3) :
            turtle.forward(length)
            turtle.left(120)
            triangle(depth - 1, length / 2)

#needed code for problem solving session
'''
def triangle(depth,length) :
    if depth==0 :
        pass
    else :
        for i in range(0,3) :
            turtle.forward(length)
            triangle(depth - 1, length / 2)
            turtle.left(120)
'''

def triangle1(length ):
    for i in range(0, 3):
        turtle.forward(length)
        turtle.left(120)
def triangle(length) :

   for i in range(0,3):
        turtle.forward(length)
        triangle1(length/2)
        turtle.left(120)
        '''
def main( ) :
    #triangle(6,200)
    triangle(3,100)
    turtle.mainloop()

main()