_author = 'Soniya Rode'
_author = 'Tejas Arya'
'''
    The program will include functions to generate data, validate sorting algorithms, and produce comparative reports.
'''


import random
import time
import instrumented_sort


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
            resutl =False


    return result



def main():

    '''
    Main function
    :return: None
    '''
    with open('output.txt','w') as  o :
        NList=[10,100,1000,10000]
        o.write('ALGORITHMS\t\t Number of elements\t COMPARISONS\t\t TIME TAKEN\n')

        for i in NList :
            #Get the list data
            data =generateData(i)

            #Use the time function to count the time required for execution of the function
            begin=time.time()
            ssortL,count=instrumented_sort.ssort(data)
            end=time.time()
            result=end-begin

            #Write to the file
            o.write('Selection Sort\t\t\t' + str(i) + '\t\t\t' + str(count) + '\t\t\t\t'+str(result)+'\n' )

            begin = time.time()
            msortL=instrumented_sort.mergeSort(data)
            end = time.time()
            result =  end-begin

            o.write('Merge Sort\t\t\t\t' + str(i) + '\t\t\t' + str(msortL[1]) + '\t\t\t\t'+str(result)+'\n' )


main()