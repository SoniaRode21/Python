for i in range(0, height):
    listVertices = []

    for j in range(0, width):

        flag = False

        if Matrix[i][j] is "*":
            string = str(i) + "," + str(j - 1)
            print("string", string)
            listVertices.append(string)
            flag = True
        elif j == width - 1 and not flag:
            string = str(i) + "," + str(j - 1)
            print("string", string)
            listVertices.append(string)

        print("List : for  ", i, " ,", j, " ", listVertices)




def horizontalUp(list,matrix,node,i,j,height,width) :

    if node=="*" :
        #print("Value = *")
        return list
    else:
        if i==0 :
            #print("First row")
            return list
        else:
            k=i-1
            flag=False
            if k==0 :
                if matrix[k][j]=="*":
                    return  list
                else:
                    string = str(0) + "," + str(j)
                    list.append(string)
                    return list

            while k>-1:
                #print("Inside this value of k",k)
                if matrix[k][j]=="*":
                    string=str(k+1)+","+str(j)
                    list.append(string)
                    flag=True
                    #print("Value of k ",k)
                    break
                k=-1
            k+=1
            if not flag :
                if matrix[k][j]=="*":
                    return  list
                else:
                    string=str(k)+","+str(j)
                    list.append(string)
    return list
