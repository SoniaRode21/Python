_author = 'Soniya Rode'


class LinkedNode:

    __slots__ = "value", "link"

    def __init__( self, value, link = None ):
        """ Create a new node and optionally link it to an existing one.
            param value: the value to be stored in the new node
            param link: the node linked to this one
        """
        self.value = value
        self.link = link

'''
RingBuffer class is a linked structure which is the underlying strucutre for stack and queue
'''
class RingBuffer:
    __slots__ = 'front' ,'back' , '_capacity' , '_size'

    def __init__(self,cap):
        """ Create an empty list.
        """
        self.front = None
        self.back=None
        self._capacity=cap
        self._size =0
    #Print the list
    def __str__(self):

        if self.front==None:
            return "Empty buffer"
        else:
            result = '['

            # Linked traversal.
            current = self.front
            while current is not self.back:
                result += str(current.value) + ', '
                current = current.link
            result += str(current.value)
            result += ']'

            return result
    #get the capacity
    def capacity(self):
        return self._capacity

    def size(self):
        return self._size

    def Print(self) :

        current = self.front

        if self.front==None:
            print("Empty buffer")
        else :
            print(str(current.value))
            current=self.front.link

            while(current!=self.back.link) :
                print( str(current.value))
                current = current.link


    # Inserts the new element and removes the oldest
    def insert_keep_new(self,val) :



        # insert into the buffer without removing any element
        newNode = LinkedNode(val)
        if self.front == None:
            self.front = newNode
        else:
            self.back.link = newNode
        self.back = newNode


        # If the buffer is already full, remove the oldest

        if self._size == self._capacity:
            self.front=self.front.link
            self._size-=1
        self._size+=1
        newNode.link=self.front






    #Keeps the oldest element if the buffer is full
    def insert_keep_old(self,val):
        if self._size == self._capacity:
            pass
        else :

            # insert into the buffer without removing any element
            newNode = LinkedNode(val)
            if self.front == None:
                self.front = newNode
            else:
                self.back.link = newNode
            self.back = newNode
            self._size+=1



    def remove_oldest(self):
        if self.front == None:
            print("Empty buffer")
            return

        self._size -= 1


        if self._size==0 :
            self.front=None
            self.back=None
        else:
            self.front=self.front.link
            self.back.link = self.front


    def remove_newest(self):
        if self.front == None:
            print("Empty buffer")


        self._size -= 1

        if self._size==0 :
            self.front=None
            self.back=None
        else:
            current = self.front
            prev = current
            while (current != self.back):

                prev = current
                current = current.link
            self.back=prev


    def find(self,val):

        current = self.front

        if current == None:

            return -1
        else:

            prev = None

            while current is not  self.back:
                if current.value==val:
                    return current
                #prev = current
                current = current.link
            if current.value==val:
                return current
        return -1



    def replace(self,cursor,val):
        cursor.value=val




def test():
        print('Creating empty ListStack named "a" of size 3')
        a = RingBuffer(3)


        for val in range(5):
            # 'inserting', val, 'into both a'
            a.insert_keep_new(val)
        print(a.capacity())
        print(a.size())
        print( 'currently contains ',a)
        print(a)
        print("Finding 4, replacing with 8")
        a.replace(a.find(4), 8)
        print(a.Print())
        print("Finding  8 returns its cursor")
        print( a.find(8))

        print('Afetr remove oldest a ')
        a.remove_oldest()
        print(a)
        print('Afetr remove oldest a ')
        a.remove_oldest()
        print(a)
        print('Afetr remove oldest a ')
        a.remove_oldest()
        print(a)

        b = RingBuffer(4)

        for val in range(6):
            #print('inserting', val, 'into both a')
            b.insert_keep_old(val)
        print(b.capacity())
        print(b.size())
        print('currently contains b')
        print(b.Print())
        print('Afetr remove newest b ')
        b.remove_newest()
        print(b)
        b.remove_newest()
        print(b)
        b.remove_newest()
        print(b)
        b.remove_newest()
        print(b)


        '''
        

        
        '''

if __name__ == '__main__':
        test()

