_author = 'Soniya Rode'


"""
stack.py
description: A linked stack (LIFO) implementation
"""

import ring_buffer
class LinkedNode:

    __slots__ = "value", "link"

    def __init__( self, value, link = None ):
        """ Create a new node and optionally link it to an existing one.
            param value: the value to be stored in the new node
            param link: the node linked to this one
        """
        self.value = value
        self.link = link


class Stack:

    __slots__ = "top","capacity"

    def __init__( self ,cap):
        """ Create a new empty stack.
        """
        self.top = None
        self.capacity=cap

    def __str__( self ):
        """ Return a string representation of the contents of
            this stack, top value first.
        """
        result = "Stack["
        n = self.top
        while n != None:
            result += " " + str( n.value )
            n = n.link
        result += " ]"
        return result

    #Checks if stack is empty
    def is_empty( self ):
        return self.top == None


    #Pushes to the stack
    def push( self,lstack, newValue ):
        lstack.insert_keep_new(newValue)
        self.top = lstack.front
        lstack.back.link=None




    #Pops from the stack
    def pop( self,lstack ):
        assert not self.is_empty(), "Pop from empty stack"
        lstack.remove_newest()
        if lstack._size==0:
            self.top=None
            return -1
        lstack.back.link= None

        self.top = lstack.front

    def peek( self,lstack ):
        assert not self.is_empty(), "peek on empty stack"
        return lstack.back.value

    insert = push
    remove = pop

def test():
    s = Stack(8)
    lstack=ring_buffer.RingBuffer(s.capacity)

    for value in 1, 2, 3:
        s.push( lstack,value )
        print( s )

    print( "Popping:" )
    s.pop(lstack)
    print( s )
    print("Peeking:")
    print(s.peek(lstack))
    for value in 15, 16:
        s.insert(lstack,value )
        print( s )
    print( "Removing:" )
    s.remove(lstack)
    print( s )
    while not s.is_empty():
        print( "Popping:")
        s.pop(lstack)
        print( s )
    # print( "Trying one too many pops... ", end="" )


if __name__ == "__main__":
    test()
