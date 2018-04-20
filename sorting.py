


def mySort(myList):
    counter = len(myList)
    counter2 = 0

    while (counter>0):
        counter2 = 1
        while counter2 < counter:
            if (myList[counter2-1] > myList[counter2]):
                temp = myList[counter2-1]
                myList[counter2-1] = myList[counter2]
                myList[counter2]=temp
            else:
                counter2+=1
            # print(myList)
        counter-=1

    return myList



def bsearch(myList, value):
    # myList = sorting.mySort(myList)
    left = 0
    right = len(myList)-1
    
    result = -1
    while(left <= right):
        middle = int((left+right) /2) 
        if (myList[middle] > value):
            left = middle + 1            
        elif (myList[middle] < value):
            right = middle - 1
        elif (myList[middle] == value):
           result = middle
           break
        else:
            result = -1
            break
       
    return result


myList = [7,3,9,4,10,2]
print("The list sorted using bubble Sort", mySort(myList))

myList = ['Chip', 'Dale', 'Duey', 'Goofy', 'Huey', 'Luey', 'Mickey', 'Minnie', 'Pluto']
print("The Position for value found by binary Search" ,bsearch(myList, "Pete"))