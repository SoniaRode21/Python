_author = 'Soniya Rode'

'''
    The program includes functions to find the median of three,partition the array
    , and quick sort the data.
'''



def median_of_three(array,l,r):
    '''
    Function to the the median value and place it at the pivot postion
    :param array: list containing elements to be sorted
    :param l : left most index of the list
    :param r : right most index of the list
    :return: None
    '''
    #get the index of center element
    center=(l+r)//2

    #Find the median of the three
    if array[center]<array[l]:
        array[center],array[l]=array[l],array[center]

    if array[r]<array[l]:
        array[r],array[l]=array[l],array[r]
    if array[center]>array[r]:
        array[r],array[center]=array[center],array[r]

    #Place the median at the pivot postion
    array[center],array[r]=array[r],array[center]



def partition(array, l, r):
    '''
    Function to partition the array based on pivot value
    :param array: list containing elements to be sorted
    :param l : left most index of the list
    :param r : right most index of the list
    :return: partition index
    '''
    small = (l - 1)
    median_of_three(array,l,r)

    #pivot value is the median of three
    pivot = array[r]

    for _ in range(l, r):

        # If current element is smaller than or
        # equal to pivot
        if array[_] <= pivot:
            # increment index of smaller element
            small = small + 1
            array[small], array[_] = array[_], array[small]

    array[small+ 1], array[r] = array[r], array[small + 1]
    return (small + 1)


def quickSort(array,l,r):
    '''
    Function to sort the data
    :param array: list containing elements to be sorted
    :param l : left most index of the list
    :param r : right most index of the list
    :return: None
    '''
    if l<r:

        q=partition(array,l,r)
        quickSort(array,l,q-1)
        quickSort(array,q+1,r)


