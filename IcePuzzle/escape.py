__author__ = 'Soniya Rode'
__author__ = 'Tejas Arya'


import sys
from graph import  Graph
from searchAlgos import canReachDFS, findPathDFS, findShortestPath


def main():
    '''
        The main function reads the graph file and prints out how quickly you can exit from each node
        and whether an exit is possible or not
    '''

    # Take file input and process it
    print("graph1.txt to see the output \nEnter test1.txt / test2.txt / test3.txt to see the test cases")
    filename =input("Enter the file name :")

    my_file = open(filename, "r")

    #Get the phond size  details
    pondSize=my_file.readline()

    #height of the pond
    height=int(pondSize[0])

    #width of the ponde
    width=int(pondSize[2])


    exitRow=pondSize[4]

    #Create a matrix to store the pond data
    Matrix = [[0 for x in range(width)] for y in range(height)]

    # i and j for iteration
    i=0
    j=0
    for line in my_file :

        #strip off the spaces
        line=line.strip()

        for _ in line:
            Matrix[i][j]=_
            j+=1
        j=0
        i+=1

    #Create an Graph object
    escapeRoutes = Graph()

    #For each node find all the reachable nodes
    for i in range(0,height) :
        listVertices=[]

        for j in range(0,width):
            listVertices = []

            #Functions to get connected nodes
            horizontalUp(listVertices,Matrix,Matrix[i][j],i,j,height,width)
            horizontalDown(listVertices, Matrix, Matrix[i][j], i, j, height, width)
            verticalForward(listVertices,Matrix,Matrix[i][j],i,j,height,width)
            verticalBackward(listVertices, Matrix, Matrix[i][j], i, j, height, width)

            string=str(i) + "," + str(j)

            #Add the connected nodes to the graph
            for _ in listVertices:
                escapeRoutes.addEdge(string,_)


    s = escapeRoutes.getVertices()

    #Exit node
    exit = exitRow + "," + str(width - 1)

    #Get nodes connected to the exit node
    endVertex = escapeRoutes.getVertex(exit)
    maxCount = 0

    if exit not in s:
        print("Exit route not present on the graph")
        sys.exit(0)

    #To get the maximum number of steps required to reach the exit
    for _ in s:

        startVertex = escapeRoutes.getVertex(_)
        path, count = findShortestPath(startVertex,endVertex)
        if maxCount < count:
            maxCount = count


    print("Considering height as x co-ordinate and width as y co-ordinate of the pond.The escape  is at row ", exitRow)
    i = 1

    #Prints the number of steps required from each node
    while i <= maxCount:
        list = []
        for _ in s:
            startVertex = escapeRoutes.getVertex(_)
            path,count = findShortestPath(startVertex, endVertex)
            if count == i:
                list.append(_[::-1])
            if i==1 and _==exit:
                list.append(_[::-1])


        print(i, " : [ ", list, " ]")
        i += 1
    if maxCount == 0:
        print("No EXIT route found")


def horizontalUp(list,matrix,node,i,j,height,width) :
    '''
    This function finds the reachable node above the current node
    :param list: list of nodes connected to the current node
    :param matrix: Matrix containing the graph
    :param node: Current node
    :param i: i th position of the node
    :param j: j th position of the node
    :param height: Height of the pond
    :param width: Widht of the pond
    :return: returns the updated list
    '''

    #If the current node is a stone
    if node=="*" :

        return list
    #For the first row
    if i==0 :

        return list
    #For all other nodes
    else:

            k=i
            flag=False
            while k!=0 and matrix[k][j]!="*":
                k=k-1

                if matrix[k][j]=="*":
                    flag=True

            if flag :

                if matrix[i-1][j]=="*":
                    return list
                else :
                    string = str(k+1) + "," + str(j)
                    list.append(string)
                    return list



            else:
                string=str(k)+","+str(j)
                list.append(string)
    return list


def horizontalDown(list,matrix,node,i,j,height,width) :
    '''
    This function finds the reachable node below the current node
    :param list: list of nodes connected to the current node
    :param matrix: Matrix containing the graph
    :param node: Current node
    :param i: i th position of the node
    :param j: j th position of the node
    :param height: Height of the pond
    :param width: Widht of the pond
    :return: returns the updated list
    '''

    # If the current node is a stone
    if node=="*" :
        #print("Value = *")
        return list

    #For the last row nodes
    if i==height-1 :

        return list

    #For all other nodes
    else:

            k=i
            flag=False
            while k!=height-1 and matrix[k][j]!="*":
                k=k+1

                if matrix[k][j]=="*":
                    flag=True

            if flag :

                if matrix[i+1][j]=="*":
                    return list
                else :
                    string = str(k-1) + "," + str(j)
                    list.append(string)
                    return list



            else:
                string=str(height-1)+","+str(j)
                list.append(string)
    return list



def verticalForward(list,matrix,node,i,j,height,width):
    '''
    This function finds the reachable node to  the right of the  current node
    :param list: list of nodes connected to the current node
    :param matrix: Matrix containing the graph
    :param node: Current node
    :param i: i th position of the node
    :param j: j th position of the node
    :param height: Height of the pond
    :param width: Widht of the pond
    :return: returns the updated list
    '''

    # If the current node is a stone
    if node=="*" :

        return list

    #For the right most nodes
    if j==width-1:

        return list

    #For all other nodes
    else:

            k=j
            flag=False
            while k!=width-1 and matrix[i][k]!="*":
                k=k+1

                if matrix[i][k]=="*":
                    flag=True

            if flag :
                    if matrix[i][j+1]=="*":
                        return list
                    else:
                        string = str(i) + "," + str(k-1)
                        list.append(string)
                        return list



            else:
                string=str(i)+","+str(width-1)
                list.append(string)
    return list


def verticalBackward(list,matrix,node,i,j,height,width):
    '''
    This function finds the reachable to the left the current node
    :param list: list of nodes connected to the current node
    :param matrix: Matrix containing the graph
    :param node: Current node
    :param i: i th position of the node
    :param j: j th position of the node
    :param height: Height of the pond
    :param width: Widht of the pond
    :return: returns the updated list
    '''

    # If the current node is a stone
    if node=="*" :

        return list

    #For the left most nodes
    if j==0:

        return list

    #For all other nodes
    else:


            k=j
            flag=False
            while k!=0 and matrix[i][k]!="*":
                k=k-1

                if matrix[i][k]=="*":
                    flag=True

            if flag :
                    if matrix[i][j-1]=="*":
                        return list
                    else:
                        string = str(i) + "," + str(k+1)
                        list.append(string)
                        return list



            else:
                string=str(i)+","+str(0)
                list.append(string)
    return list

main()