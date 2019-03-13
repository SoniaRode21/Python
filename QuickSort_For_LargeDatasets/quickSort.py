_author = 'Soniya Rode'

'''
    The program includes functions to partition the array
    and quick sort the data.
'''

def partition(arr, l, r):

    '''
    Function to partition the array based on pivot value
    :param array: list containing elements to be sorted
    :param l : left most index of the list
    :param r : right most index of the list
    :return: partition index
    '''
    small = (l - 1)

    #pivot value is the rightmost value of the list
    pivot = arr[r]

    for _ in range(l, r):

        # If current element is smaller than or
        # equal to pivot
        if arr[_] <= pivot:
            # increment index of smaller element
            small = small + 1
            arr[small], arr[_] = arr[_], arr[small]

    arr[small+ 1], arr[r] = arr[r], arr[small + 1]
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


