_author = 'Soniya Rode'

'''
    The program includes functions to generate data, validate sorting algorithm outputs,
     and produce comparative reports.
'''


import random
import time
import quickSort
import my_choice_quickSort
import numpy as np


def generateData(N):
    '''
    Generates random list of N nos.
    :param N: Number of elements in the list
    :return:  List
    '''
    result = list(range(N))
    random. shuffle(result)

    return result

def checkSorted(listA):
    '''
    Checks if the list is sorted
    :param listA: Sorted list form the sort function
    :return: True or false(True if the list is sorted)
    '''
    result=True
    for i in range(0,len(listA)-1):
        print(listA[i],listA[i+1])
        if listA[i]>listA[i+1]:
            result =False


    return result



def main():

    '''
    Main function
    :return: None
    '''


    #Dataset size
    NList = [10, 100, 1000, 10000, 50000,100000,500000]
    choice=0

    print('ALGORITHMS\t\t Number of elements\t COMPARISONS\t\t TIME TAKEN\n')
    print("SET_1 : Random Lists ")
    for i in NList :
            #Get the list data
            data =generateData(i)

            #Use the time function to count the time required for execution of the function
            begin=time.time()
            sortedList1=quickSort.quickSort(data,0,len(data)-1)
            end=time.time()
            result=end-begin

            #Write to the file
            print('Quick Sort\t\t\t\t' + str(i) + '\t\t\t\t'+str(result)+'\n' )

            begin = time.time()
            msortL=my_choice_quickSort.quickSort(data,0,len(data)-1)
            end = time.time()
            result =  end-begin

            print('My Choice Sort\t\t\t' + str(i) + '\t\t\t\t'+str(result)+'\n' )
    print("SET_2 : Poisson distribution of data values")
    for i in NList :
            #Get the list data
            data =np.random.poisson(i/2, i)

            #Use the time function to count the time required for execution of the function
            begin=time.time()
            sortedList1=quickSort.quickSort(data,0,len(data)-1)
            end=time.time()
            result=end-begin

            #Write to the file
            print('Quick Sort\t\t\t\t' + str(i) + '\t\t\t\t'+str(result)+'\n' )

            begin = time.time()
            msortL=my_choice_quickSort.quickSort(data,0,len(data)-1)
            end = time.time()
            result =  end-begin

            print('My Choice Sort\t\t\t' + str(i) + '\t\t\t\t'+str(result)+'\n' )



main()
