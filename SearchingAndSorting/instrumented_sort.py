_author = 'Soniya Rode'
_author = 'Tejas Arya'
'''
    The program will include implementation of selection sort and merge sort algorithms which take data from 
    the sorting_experiment file.
'''




counter=0
def ssort(data):

   '''
   Selection sort Algorithm
   :param  data:        List to be sorted
   :return data:        Sorted list
   :return counter:     No. of comparisons required
   '''
   # k is the number of elements sorted so far
   # thus, k is the index where we will put the next one
   count=0
   for k in range(len(data)-1):
       minindex = k
       # initially k'th item is "minimum so far" of remaining elements
       for index in range(k+1,len(data)):
           if data[index] < data[minindex]:
               minindex = index
           count+=1
        # now swap the min value into slot k
       temp = data[k]
       data[k] = data[minindex]
       data[minindex] = temp

   return data,count
    # no return, data is sorted in-place!





def mergeSort(alist):
    '''
    Merge sort Algorithm
    :param  data:        List to be sorted
    :return data:        Sorted list
    :return counter:     No. of comparisons required
    '''

    global counter
    #if the length is 1
    if (len(alist) == 1):
        return alist,counter

    if len(alist)>1:
        #Split the list in 2 parts
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            #Compare the left and right lists
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1
            counter+=1

        while i < len(lefthalf):
            #Append the left half of the remaining list
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            # Append the right half of the remaining list

            alist[k]=righthalf[j]
            j=j+1
            k=k+1

        return alist,counter

def iSort(data) :
    '''
    Insertion sort Algorithm
    :param  data:        List to be sorted
    :return data:        Sorted list
    :return counter:     No. of comparisons required
    '''

    global counter
    counter=0
    for i in range(1,len(data)) :
        current=data[i]
        position=i
        while(position>0 and data[position-1] > current) :

            data[position]=data[position-1]
            position-=1
        data[position]=current
        counter += 1

    return data,counter
