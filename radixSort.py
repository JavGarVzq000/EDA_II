def countingSort(arr, exp1):
    n = len(arr)

    #The output array elements that will have sorted arr
    output = [0]*(n)

    #initializa count array as 0
    count = [0]*(10)

    #Store count of occurrances in count[]
    for i in range(0,n):
        index = arr[i] // exp1
        count[index % 10] += 1
    
    #Change count[i] so that count[i] now contains actual
    #position of this digit in output array
    for i in range(1,10):
        count[i] += count[i - 1]
    
    i = n - 1
    while i >= 0:
        index = arr[i] // exp1
        output[count[index % 10] -1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    
    #Counting the output array to arr[],
    #so that arr now contains sorted numbers
    i = 0
    for i in range(0,len(arr)):
        arr[i] = output[i]

#Method to do Radix Sort
def radixSort(arr):
    #Find the maximum number to know number of digitis
    max1  = max(arr)

    #Do counting sort for every digit. Note that instead
    #of passing digit number, exp is pasesed. exp is 10î
    #where i is current digit number
    exp = 1
    while max1 / exp >= 1:
        countingSort(arr, exp)
        exp *= 10


#Drive code
arr = [170,45,75,90,802,24,2,66]

#Function Call
radixSort(arr)

for i in range(len(arr)):
    print(arr[i],end=" ")