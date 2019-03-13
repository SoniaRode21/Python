_author = 'Soniya Rode'

import stack
import queue
import ring_buffer

'''
    The program  calls the test functions of the stack and queue classes  and compares the result to the list stack and queue
'''



def testStack():
        stack.test()

def testQueue():
        queue.test()

def testBuffer():
        ring_buffer.test()



if __name__ == '__main__':
        testStack()
        testQueue()
        testBuffer()
