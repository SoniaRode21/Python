import sys
def processFile(test) :
    with open(test) as t :
        t.readline()
        lines=[]
        a=[]

        for line in t :

            line=line.strip()
            line=line.split(" ")
            lines+=line
        return lines


def ssort(data) :



    for k in range(0,len(data)) :
        minIndex=k
        for i in range(k+1,len(data)) :
            if (data[minIndex])>((data[i])) :
                minIndex=i


        temp=data[minIndex]
       # print(temp)
        data[minIndex]=data[k]
        #print(data[minIndex])
        data[k]=temp

    return data

def binarySearch(data,l,r) :

    m=(l+r)//2

    if data[m]=="words" :
         return m
    elif data[m] < "words" :

        l=m+1
        m=binarySearch(data,l,r)
    elif data[m] >"words" :
        r=m-1
        m=binarySearch(data,l,r)
    return m





def main():
    test=sys.argv[1]


    list1= processFile(test)
    ans=ssort(list1)
    print(ans)


    ans1=binarySearch(ans,0,len(ans)-1)
    print(ans1)



main()