


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


# 3.1 Implement and Test the Bubble Sort
# 1. Implement the algorithm as detailled in the flow chart in figure 1. Write
# your implementation in the module called mysort.
# Figure 1: The Bubble Sort
# 2
# 2. Create a screen shot of your program running correctly with both the
# source code editor and the output screen clearly visible.
# 3. Create a trace for each of the inputs [7,3,9,4,10,2] and [1,2,3,4,5].
# 3.2 Implementing Binary Search
# Create a new module in your sorting.py file called bsearch. The inputs and
# outputs are desribed below along with pseudocode for the algorithm.
# input a list containing your data
# the value you want to search for
# processing SET left to 0
# SET right to length of list - 1
# REPEAT:
# -SET middle to lef t+right
# 2
# , rounded down to the nearest integer
# -IF left > right THEN
# –SET result to -1 and end module
# -IF list item at index middle > the value we are searching for THEN
# –SET left to middle + 1
# -IF list item at index middle < the value we are searching for THEN
# –SET right to middle - 1
# -If list item at index middle = the value we are searching for THEN
# –SET result to middle and end module
# END LOOP
# output if the value is in the list output the index number where the value was found
# otherwise output -1
# 1. Create a flow chart to describe the algorithm.
# 2. Implement the algorithm as described above.
# 3. Use testData[0] as your test array. Prompt the user to input a number.
# Validate the input is a number and then find the index of the element in
# the test data using your bsearch module. If the element is found report
# the position of the element. If it is not found display a message telling the
# user that it was not found, do not report an index of -1.
