def mergeSort(arr):
    if len(arr)> 1:
        #Finding the mid of the array
        mid = len(arr)//2
        
        #Dividing the array elements
        L = arr[:mid]
        
        #into 2 halves
        R = arr[mid:]
        
        #Sorting the first half
        mergeSort(L)
        
        #Sorting the first half
        mergeSort(R)
        
        i = j = k = 0
        
        #Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
            
        
        #Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
            
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
        
#Code to print the list

def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ") #this line soes not work in Python 1, only in Python 3
    print()


arr = [38,27,43,3,9,92,10]
print("Given array is: ", end="\n")#this line soes not work in Python 1, only in Python 3
printList(arr)
mergeSort(arr)
print("Sorted array is: ", end="\n")#this line soes not work in Python 1, only in Python 3
printList(arr)







