_author = 'Soniya Rode'

"""
queue.py
description: A linked queue (FIFO) implementation
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

class Queue:

    __slots__ = "front", "back","capacity"

    def __init__( self,cap ):
        """ Create a new empty queue.
        """
        self.front = None
        self.back = None
        self.capacity=cap

    def __str__( self ):
        """ Return a string representation of the contents of
            this queue, oldest value first.
        """
        result = "Queue["
        n = self.front
        while n != None:
            result += " " + str( n.value )
            n = n.link
        result += " ]"
        return result

    def is_empty( self ):
        return self.front == None

    def enqueue( self, newValue ,l):
        l.insert_keep_new(newValue)
        self.front = l.front
        self.back=l.back
        if self.front is not None:
            self.back.link=None

    def dequeue( self,l ):
        l.remove_oldest()
        self.front = l.front
        self.back=l.back
        if self.front is not None:
            self.back.link=None


    def peek( self ):
        assert not self.is_empty(), "peek on empty stack"
        return self.front.value

    insert = enqueue
    remove = dequeue

def test():
    s = Queue(4)
    lqueue=ring_buffer.RingBuffer(4)


    #print( s )
    for value in 1, 2, 3:
        s.enqueue(value ,lqueue)
        print( s )
    print( "Dequeueing:", s.peek() )
    s.dequeue(lqueue)
    print( s )
    for value in 15, 16:
        s.insert(value,lqueue )
        print( s )
    print( "Removing:", s.peek() )
    s.remove(lqueue)
    print( s )
    while not s.is_empty():
        print( "Dequeueing:", s.peek() )
        s.dequeue(lqueue)
        print( s )


if __name__ == "__main__":
    test()
